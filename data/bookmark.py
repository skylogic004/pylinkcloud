import os
from colorama import Fore, Back, Style

class Bookmark():
	tags = None

	def __init__(self, properties):
		try:
			self.bookmarkId = properties['bookmarkId']
		except:
			self.bookmarkId = None # occurs when bookmark isn't yet inserted into DB

		try:
			self.tags = properties['tags']
		except:
			self.tags = None

		self.linkURL = properties['linkURL']
		self.linkDirPath = properties['linkDirPath']
		self.linkFilename = properties['linkFilename']
		self.linkTitle = properties['linkTitle']

	def scrapeTagsFromPath(self):
		self.tags = self.linkDirPath.split(os.sep)

	def getTags(self):
		if (self.tags is None):
			self.scrapeTagsFromPath()

		return self.tags

	def truncateString(self, s, len=12):
		return s[:len] + (s[len:] and '..')

	def toString(self):
		s = Fore.CYAN + self.linkDirPath
		s += ' ' + Fore.WHITE + self.truncateString(self.linkTitle)
		s += ' ' + Fore.GREEN + self.truncateString(self.linkFilename)
		s += ' ' + Fore.YELLOW + self.truncateString(self.linkURL, 24)
		if (self.tags is not None):
			s += ' ' + Fore.GREEN + ','.join(self.tags)
		s += Fore.RESET
		return s

