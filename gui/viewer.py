#!python3.4
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.qt_viewer import Ui_PyLinkCloud
import webbrowser

class Viewer(QtWidgets.QMainWindow, Ui_PyLinkCloud):
	def __init__(self, parent = None, controller = None):
		QtWidgets.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.scanBtn.clicked.connect(controller.scanAndSaveToDB)

		self.controller = controller

		self.treeWidgetColumns = [
			{'name': 'Tag', 'width': 150},
			{'name': 'Title', 'width': 400},
			{'name': 'URL', 'width': 300}
		]
		self.treeWidget.setHeaderLabels([c['name'] for c in self.treeWidgetColumns]);
		for idx, c in enumerate(self.treeWidgetColumns):
			self.treeWidget.setColumnWidth(idx, c['width'])

		self.treeWidget.itemDoubleClicked.connect(self.onClickItem)

	# def addInputTextToListbox(self):
	# 	txt = self.myTextInput.text()
	# 	self.listWidget.addItem(txt)

	def getTreeWidgetColIdx(self, colName):
		for idx, c in enumerate(self.treeWidgetColumns):
			if (c['name'] == colName):
				return idx

	def onClickItem (self, item):
		#item.treeWidget()
		# item.setText(0, 'testing')
		url = item.text(self.getTreeWidgetColIdx('URL'))
		webbrowser.open_new_tab(url)

	def showBookmarks(self, tagNames, bookmarks):
		# http://doc.qt.io/qt-5/qtreewidgetitem.html

		for tagName in tagNames:
			tagFolder = QtWidgets.QTreeWidgetItem(self.treeWidget, [tagName, '', ''], 0)

			for bm in bookmarks:
				if (tagName in bm.tags):
					bmWidget = QtWidgets.QTreeWidgetItem(['', bm.linkTitle, bm.linkURL])
					tagFolder.addChild(bmWidget)
					# bmWidget.clicked.connect(lambda: print('double clicked ', bm.linkURL))

		# self.treeWidget.insertTopLevelItem(0, widget)
		# treeWidget.expandItem(parent);

# Not used - just an example of how to instantitate this GUI
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	prog = Viewer()
	prog.show()
	sys.exit(app.exec_())