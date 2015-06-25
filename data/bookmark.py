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

	def howSimilar(self, otherBookmark):
		""" How similar is this bookmark to another bookmark? """

		numDiff = 3

		if (self.linkURL == otherBookmark.linkURL):
			numDiff -= 1
			
		if (self.linkFilename == otherBookmark.linkFilename):
			numDiff -=1
		
		if (self.linkTitle == otherBookmark.linkTitle):
			numDiff -= 1

		return numDiff

	def explainDifference(self, otherBookmark, thisNickname='New', otherNickname='Old'):
		out = ''

		# Is the URL the same?
		if (self.linkURL == otherBookmark.linkURL):
			out += 'Both have URL: %s' % self.linkURL
		else:
			out += '%s URL: %s\n%s URL: %s' % (thisNickname, self.linkURL, otherNickname, otherBookmark.linkURL)

		out += '\n'

		# Is the filename the same?
		if (self.linkFilename == otherBookmark.linkFilename):
			out += 'Both have filename: %s' % self.linkFilename
		else:
			out += '%s filename: %s\n%s filename: %s' % (thisNickname, self.linkFilename, otherNickname, otherBookmark.linkFilename)

		out += '\n'

		# Is the title the same?
		if (self.linkTitle == otherBookmark.linkTitle):
			out += 'Both have title: %s' % self.linkTitle
		else:
			out += '%s title: %s\n%s title: %s' % (thisNickname, self.linkTitle, otherNickname, otherBookmark.linkTitle)

		return out