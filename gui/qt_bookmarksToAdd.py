# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookmarksToAdd.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookmarksToAdd(object):
    def setupUi(self, BookmarksToAdd):
        BookmarksToAdd.setObjectName("BookmarksToAdd")
        BookmarksToAdd.resize(910, 533)
        self.buttonBox = QtWidgets.QDialogButtonBox(BookmarksToAdd)
        self.buttonBox.setGeometry(QtCore.QRect(10, 490, 861, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.addList = QtWidgets.QListWidget(BookmarksToAdd)
        self.addList.setGeometry(QtCore.QRect(320, 60, 256, 361))
        self.addList.setDragEnabled(True)
        self.addList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.addList.setAlternatingRowColors(True)
        self.addList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.addList.setObjectName("addList")
        self.duplicatesList = QtWidgets.QListWidget(BookmarksToAdd)
        self.duplicatesList.setGeometry(QtCore.QRect(30, 60, 256, 361))
        self.duplicatesList.setDragEnabled(True)
        self.duplicatesList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.duplicatesList.setAlternatingRowColors(True)
        self.duplicatesList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.duplicatesList.setObjectName("duplicatesList")
        self.addBtn = QtWidgets.QPushButton(BookmarksToAdd)
        self.addBtn.setGeometry(QtCore.QRect(30, 430, 251, 23))
        self.addBtn.setObjectName("addBtn")
        self.label = QtWidgets.QLabel(BookmarksToAdd)
        self.label.setGeometry(QtCore.QRect(320, 40, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(BookmarksToAdd)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 211, 16))
        self.label_2.setObjectName("label_2")
        self.removeFromAddBtn = QtWidgets.QPushButton(BookmarksToAdd)
        self.removeFromAddBtn.setGeometry(QtCore.QRect(320, 430, 251, 23))
        self.removeFromAddBtn.setObjectName("removeFromAddBtn")
        self.mergeList = QtWidgets.QListWidget(BookmarksToAdd)
        self.mergeList.setGeometry(QtCore.QRect(610, 60, 256, 361))
        self.mergeList.setDragEnabled(True)
        self.mergeList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.mergeList.setAlternatingRowColors(True)
        self.mergeList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.mergeList.setObjectName("mergeList")
        self.mergeBtn = QtWidgets.QPushButton(BookmarksToAdd)
        self.mergeBtn.setGeometry(QtCore.QRect(30, 460, 251, 23))
        self.mergeBtn.setObjectName("mergeBtn")
        self.label_3 = QtWidgets.QLabel(BookmarksToAdd)
        self.label_3.setGeometry(QtCore.QRect(610, 40, 201, 16))
        self.label_3.setObjectName("label_3")
        self.removeFromMergeBtn = QtWidgets.QPushButton(BookmarksToAdd)
        self.removeFromMergeBtn.setGeometry(QtCore.QRect(610, 430, 251, 23))
        self.removeFromMergeBtn.setObjectName("removeFromMergeBtn")
        self.label_4 = QtWidgets.QLabel(BookmarksToAdd)
        self.label_4.setGeometry(QtCore.QRect(300, 0, 321, 20))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(BookmarksToAdd)
        self.buttonBox.accepted.connect(BookmarksToAdd.accept)
        self.buttonBox.rejected.connect(BookmarksToAdd.reject)
        QtCore.QMetaObject.connectSlotsByName(BookmarksToAdd)

    def retranslateUi(self, BookmarksToAdd):
        _translate = QtCore.QCoreApplication.translate
        BookmarksToAdd.setWindowTitle(_translate("BookmarksToAdd", "Dialog"))
        self.duplicatesList.setSortingEnabled(False)
        self.addBtn.setText(_translate("BookmarksToAdd", "Add ->"))
        self.label.setText(_translate("BookmarksToAdd", "Add these bookmarks:"))
        self.label_2.setText(_translate("BookmarksToAdd", "Ignore (already added, etc):"))
        self.removeFromAddBtn.setText(_translate("BookmarksToAdd", "<- Remove"))
        self.mergeBtn.setText(_translate("BookmarksToAdd", "Merge ->"))
        self.label_3.setText(_translate("BookmarksToAdd", "Merge these bookmarks:"))
        self.removeFromMergeBtn.setText(_translate("BookmarksToAdd", "<- Remove"))
        self.label_4.setText(_translate("BookmarksToAdd", "Drag items between groups. Shift or Ctrl click to select multiple."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BookmarksToAdd = QtWidgets.QDialog()
    ui = Ui_BookmarksToAdd()
    ui.setupUi(BookmarksToAdd)
    BookmarksToAdd.show()
    sys.exit(app.exec_())

