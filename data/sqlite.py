import sqlite3
import numpy as np
import os
from data.bookmark import Bookmark
from colorama import Fore, Back, Style
import time

OVERWRITE_DB = False

class SqliteHelper():
	bookmarksColumns = [
		('bookmarkId', 'INTEGER PRIMARY KEY'),
		('linkTitle', 'TEXT'),
		('linkURL', 'TEXT'),
		('linkDirPath', 'TEXT'),
		('linkFilename', 'TEXT'),
	]

	tagNamesColumns = [ # TODO is this valid SQL?
		('tagId', 'INTEGER PRIMARY KEY AUTOINCREMENT'),
		('tag', 'TEXT NOT NULL UNIQUE'),
	]

	bookmarkTagsColumns = [
		('tagId', 'INTEGER NOT NULL'),
		('bookmarkId', 'INTEGER NOT NULL'),
		('PRIMARY KEY', '(tagId, bookmarkId)')
		# ('FOREIGN KEY(tagId)', 'REFERENCES tagNames(tagId) ON DELETE CASCADE')
	]

	tables = {
		'bookmarks': bookmarksColumns,
		'tagNames': tagNamesColumns,
		'bookmarkTags': bookmarkTagsColumns,
	}


	def __init__(self, dbPath):
		self.conn = None
		self.cursor = None
		self.dbPath = dbPath
		self.createDbIfNeeded()

	def insertTagNames(self, tagNames):
		"""
		:tagNames list: list of strings, representing bookmark tags
		"""

		insertCount = 0
		dupCount = 0
		for tagName in tagNames:
			try:
				self.cursor.execute('INSERT INTO tagNames (tag) VALUES (?)', (tagName,))
			except sqlite3.IntegrityError as ie:
				dupCount += 1
			else:
				insertCount += 1


		# self.conn.commit()
		# print(Fore.BLACK + Back.CYAN + 'sqlite: Done inserting tag names (tag count: %d, duplicates %d, inserted %d)' % (len(tagNames), dupCount, insertCount), Back.RESET, Fore.RESET)

	def linkBookmarkToTag(self, bid, tags):
		""" Creates a query like the following:
			INSERT INTO bookmarkTags (tagId, bookmarkId) VALUES
				((select tagId FROM tagNames WHERE tag is 'ai'), 1234),
				((select tagId FROM tagNames WHERE tag is 'dev'), 1234)

		:bid: Bookmark ID from database
		:tags: list of strings
		"""

		query = 'INSERT INTO bookmarkTags (tagId, bookmarkId) VALUES '
		valuesSql = ['((SELECT tagId FROM tagNames WHERE tag IS ?), ?)'] * len(tags)
		query += ', '.join(valuesSql)

		values = [(tagName, bid) for tagName in tags]
		values = list(sum(values, ())) # hackish way of flattening the list

		self.cursor.execute(query, values)

	def insertBookmarks(self, bookmarks):
		"""
		:bookmarks list: list of Bookmark
		"""

		st = time.time()

		for bm in bookmarks:
			bmTuple = (bm.linkTitle, bm.linkURL, bm.linkDirPath, bm.linkFilename)
			self.cursor.execute('INSERT INTO bookmarks (linkTitle, linkURL, linkDirPath, linkFilename) VALUES (?,?,?,?)', bmTuple)

			bid = self.cursor.lastrowid

			# Tags?
			tags = bm.getTags()
			if (tags is not None):
				self.insertTagNames(tags)
				self.linkBookmarkToTag(bid, tags)


		self.conn.commit()
		print(Fore.BLACK + Back.CYAN + 'sqlite: Done inserting bookmarks (count: %d). Time: %0.3f s' % (len(bookmarks), (time.time()-st)), Back.RESET, Fore.RESET)

	def getBookmarkRows(self):
		sql = 'SELECT * FROM bookmarks'
		self.cursor.execute(sql)
		return self.cursor.fetchall()

	def getBookmarks(self):
		print('sqlite: reading bookmarks from DB, and creating Bookmark objects')
		header = [x[0] for x in self.bookmarksColumns]

		bookmarks = []
		for bookmarkRow in self.getBookmarkRows():
			props = {}
			for idx, col in enumerate(header):
				props[col] = bookmarkRow[idx]

			# Get tags
			bid = bookmarkRow[0]
			self.cursor.execute('SELECT tag FROM tagNames, bookmarkTags WHERE bookmarkTags.bookmarkId = ? AND bookmarkTags.tagId = tagNames.tagId', [bid])
			tags = [row[0] for row in self.cursor.fetchall()]
			props['tags'] = tags

			bookmarks.append(Bookmark(props))

		return bookmarks

	def getTagNames(self):
		""" Get all tag names in the database """
		self.cursor.execute('SELECT tag from tagNames')
		return [row[0] for row in self.cursor.fetchall()]

	def getSqliteDtypeFromNumpy(self, npDtype):
		if (npDtype == object):
			return 'TEXT'
		elif (npDtype in  [np.float32, np.float, np.float64, np.double]):
			return 'REAL'
		elif (npDtype in [np.int32, np.int, np.number]):
			return 'INT'

	def createTableNp(self, tableName, dtypes, header):
		'''Creates a SQLite table with columns as specified in header list
		and corresponding numpy datatypes in dtypes list.'''

		sql = 'CREATE TABLE %s (' % (tableName)
			
		for i in range(0, len(dtypes)):
			npDtype = dtypes[i]
			name = header[i]

			sql = sql + name + ' ' + self.getSqliteDtypeFromNumpy(npDtype)
			   
			if (i < len(dtypes)-1):
				sql = sql + ', '

		sql = sql + ')'

		self.cursor.execute(sql)

		
	def createTable(self, tableName, columns):
		'''Creates a SQLite table with columns as a list of (columnName, sqlDatatype).'''

		sql = 'CREATE TABLE %s (' % (tableName)
			
		for i, pair in enumerate(columns):
			sql += '%s %s' % pair
			   
			if (i < len(columns)-1):
				sql = sql + ', '

		sql = sql + ')'

		print(sql)

		self.cursor.execute(sql)


	def dropAllTables(self):
		[self.cursor.execute(('DROP TABLE IF EXISTS %s' % name)) for name in self.tables]

	def createDbIfNeeded(self, overwriteDb = OVERWRITE_DB):
		print('------------ createDbIfNeeded ------------')

		print('\tChecking for DB at: ', self.dbPath)
		if (os.path.exists(self.dbPath) and not overwriteDb):
			print('\tUsing existing DB.')
			self.conn = sqlite3.connect(self.dbPath)
			self.cursor = self.conn.cursor()
		else:
			print('\tCreating new DB...')
			
			self.conn = sqlite3.connect(self.dbPath)
			self.cursor = self.conn.cursor()

			res = self.conn.execute('pragma foreign_keys')
			if (res.fetchone()[0] == 0):
				print('sqlite foreign keys not available')
			else:
				print('sqlite foreign keys ENABLED')

			self.dropAllTables()

			for name, columnSql in self.tables.items():
				self.createTable(name, columnSql)
			print('\tTables created')
			

			# executemany requires python datatype, not numpy. Must use np.asscalar on np.float32 objects. CANNOT use asscalar on str however.
			#self.cursor.executemany('INSERT INTO weights_31 VALUES (?,?)', [(np.asscalar(row[colName]) for colName in weights_header) for row in weights_31])
			#self.cursor.executemany('INSERT INTO weights_31 VALUES (?,?)', [(row['Sample'], np.asscalar(np.float32(15.234))) for row in weights_31])

			# print('\tInserting data...')
			#print(xrf_31[0] #69 columns)

			# self.cursor.executemany('INSERT INTO xrf_31 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', map(tuple, xrf_31.tolist()))
			# self.cursor.executemany('INSERT INTO assay_31 VALUES (?,?,?,?,?,?,?,?)', map(tuple, assay_31.tolist()))
			# self.cursor.executemany('INSERT INTO weights_31 VALUES (?,?)', map(tuple, weights_31.tolist()))
			# self.cursor.executemany('INSERT INTO cond_31 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', map(tuple, cond_31.tolist()))
			
			# print('\tData insertion complete')

			self.conn.commit()


	def close(self):
		print('Closing db')
		self.conn.close()

	def __del__(self):
		print('SqliteHelper destructing...')
		self.close()