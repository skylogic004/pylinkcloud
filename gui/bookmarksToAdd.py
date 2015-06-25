#!python3.4
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from gui.qt_bookmarksToAdd import Ui_BookmarksToAdd


class BookmarksToAdd(QtWidgets.QMainWindow, Ui_BookmarksToAdd):
	degStrs = ['[=] ', '[~] ', '[!] '] # this could be done more nicely... TODO

	def __init__(self, parent, nodup, dup, callback):
		QtWidgets.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.callback = callback

		# Sort duplicate bookmarks by degree of difference
		dup.sort(key=lambda tup: tup[2]) # idx 2 contains degree

		# Populate lists with bookmarks
		for bmTuple in dup:
			bmNew, bmOld, numDiff = bmTuple
			degStr = BookmarksToAdd.degStrs[numDiff]
			self.duplicatesList.addItem(degStr + bmNew.explainDifference(bmOld))
		for bm in nodup:
			self.addList.addItem(bm.linkURL)

	def accept(self):
		print('accept!')
		resultData = [1,2,3]
		self.close()
		self.callback(resultData)


	def reject(self):
		print('reject!')
		resultData = None
		self.close()
		self.callback(resultData)

# Not used - just an example of how to instantitate this GUI
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	prog = BookmarksToAdd()
	prog.show()
	sys.exit(app.exec_())