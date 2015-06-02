#!python3.4
# Made by Matthew Dirks (2015)

import sys
print(sys.version)

from PyQt5 import QtCore, QtGui, QtWidgets

import os
import csv
from time import time
import argparse
import string
import datetime
import copy

from gui import *
from data import bookmark, files, sqlite
import colorama
from colorama import Fore, Back, Style
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

from gui.viewer import Viewer

def stripQuotes(s):
	if (s.startswith('"') and s.endswith('"')) or (s.startswith('\'') and s.endswith('\'')):
		return s[1:-1]
	else:
		return s

def doCommandLineArgs():
	global args

	for i, arg in enumerate(sys.argv[1:]):
		sys.argv[i+1] = stripQuotes(arg)

	parser = argparse.ArgumentParser(description='PyLinkCloud made by Matthew Dirks')

	# parser.add_argument('--convolution', dest='convolution', help='Enable convolution module', action='store_true', default=False)
	# fileOrProjectGroup = parser.add_mutually_exclusive_group(required=False)
	# fileOrProjectGroup.add_argument('-files', dest='files', type=str, nargs='+', help='CSV filename.', default=None)
	# fileOrProjectGroup.add_argument('-project', dest='project', type=str, help='Project filepath', default=None)

	args = parser.parse_args()

#####################################################################################
################################### MAIN ############################################
#####################################################################################
class Controller():
	def __init__(self):
		self.bookmarksDir = 'C:/MD/cloud/Dropbox/website-bookmarks-database/bookmarks'

		print(Fore.MAGENTA + '*** PyLinkCloud ***\n\tCreated by Matthew Dirks (skylogic.ca)' + Fore.RESET)
		self.db = sqlite.SqliteHelper('C:/MD/cloud/Dropbox/website-bookmarks-database/my-bookmarks.sqlite3')


		self.gui = Viewer(None, self)
		self.gui.show()

		print(Fore.RED + '''
			TODO: 
			- DONE: tags from folder paths
			- DONE: GUI with list of all bookmarks in the DB, and click to open in browser. Make in QT?
			- handle case when duplicate found
			- manual tags
			- manual description
			- search (tags, name, etc)
		''' + Fore.RESET)

		self.bookmarks = self.db.getBookmarks()
		self.gui.showBookmarks(self.db.getTagNames(), self.bookmarks)

	#####################################################################################
	################################ MAIN FUNCTIONS #####################################
	#####################################################################################
	def scanAndSaveToDB(self):
		self.bookmarks = self.db.getBookmarks()
		files.scanAndSaveToDB(self.bookmarksDir, self.db, self.bookmarks)

		# Reload DB
		self.bookmarks = self.db.getBookmarks()
		self.gui.showBookmarks(self.db.getTagNames(), self.bookmarks)







#####################################################################################
#####################################################################################
#####################################################################################
if __name__ == '__main__':
	doCommandLineArgs()
	colorama.init(autoreset=True) # enables colors in Windows CMD

	app = QtWidgets.QApplication(sys.argv)
	controller = Controller()
	sys.exit(app.exec_())