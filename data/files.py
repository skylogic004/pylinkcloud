import os
from colorama import Fore, Back, Style
import re # regular expressions

from data.bookmark import Bookmark
from gui.bookmarksToAdd import BookmarksToAdd

winUrlPattern = re.compile('^URL\=(.*)$')

h1 = Fore.BLACK + Back.CYAN
reset = Fore.RESET + Back.RESET

def scanAndSaveToDB(bookmarksDir, db, bookmarks, gui):
	print(h1 + 'files: scanning files and creating Bookmark objects' + reset)
	newBookmarks = []

	for (dirpath, dirnames, filenames) in os.walk(bookmarksDir):
		for filename in filenames:
			filepath = os.path.join(dirpath, filename)

			props = {}
			props['linkURL'] = readFile(filepath)
			props['linkDirPath'] = os.path.relpath(dirpath, bookmarksDir)
			props['linkFilename'] = filename
			props['linkTitle'] = os.path.splitext(filename)[0]
			b = Bookmark(props)
			# print(b.toString())

			newBookmarks.append(b)

	nodup, dup = listDuplicates(bookmarks, newBookmarks)
	d = BookmarksToAdd(parent=gui, nodup=nodup, dup=dup, callback=finish_scanAndSaveToDB)
	d.show()

	# OLD CODE - REMOVE THIS LATER:::

	newBookmarks = removeDuplicates(bookmarks, newBookmarks)


	print(h1 + 'files: get tags from Bookmarks' + reset)
	for bookmark in newBookmarks:
		bookmark.scrapeTagsFromPath()
		print('INSERTING: ', bookmark.toString())

	db.insertBookmarks(newBookmarks)

def finish_scanAndSaveToDB(result):
	print('finish_scanAndSaveToDB TODO', result)

def readFile(filepath):
	# ext = filepath[filepath.rfind('.'):]
	ext = os.path.splitext(filepath)[1]
	ext = ext.lower()

	if (ext == '.url'):
		return readDotURL(filepath)
	elif (ext == '.desktop'):
		return readDotURL(filepath) #TODO
    	
def readDotURL(filepath):
	fileOb = open(filepath, 'r')

	for line in fileOb:
		reResult = winUrlPattern.match(line)

		if (reResult is not None):
			sp = reResult.span(1)
			url = line[sp[0]:sp[1]]
			return url

	# Read entire file but did not find a URL
	print(Fore.RED + 'ERROR: file does not contain a URL')
	return ''


def listDuplicates(bookmarks, newBookmarks):
	# TODO dont think this is working - returns empty lists!
	"""Detect duplices"""

	nodup = []
	dup = []

	for bmNew in newBookmarks:
		foundDup = False
		for bm in bookmarks:
			numDiff = bmNew.howSimilar(bm)
			if (numDiff < 3):
				dup.append((bmNew, bm, numDiff))
				foundDup = True
				break

		if (not foundDup):
			nodup.append(bmNew)

	return nodup, dup

def removeDuplicates(bookmarks, newBookmarks):
	"""Creates and returns a new list of bookmarks
	without any duplicates"""

	nodup = []

	for bmNew in newBookmarks:
		foundDup = False
		for bm in bookmarks:
			if (bm.linkURL == bmNew.linkURL):
				foundDup = True
				break

		if (not foundDup):
			nodup.append(bmNew)

	return nodup


# EXAMPLES
# .desktop:
# 	[Desktop Entry]
# 	Encoding=UTF-8
# 	Name=Link to Ask Ubuntu
# 	Type=Link
# 	URL=http://www.askubuntu.com/
# 	Icon=text-html

# .url:
# 	[InternetShortcut]
# 	URL=http://thegoodchristianmusicblog.com/category/blues/
# 	IDList=
# 	HotKey=0
# 	IconFile=C:\Users\Matthew\AppData\Local\Mozilla\Firefox\Profiles\twqe9ana.default\shortcutCache\KAaaSPxwsbjgaIrmOTA9eg==.ico
# 	IconIndex=0