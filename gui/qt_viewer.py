# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewer.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyLinkCloud(object):
    def setupUi(self, PyLinkCloud):
        PyLinkCloud.setObjectName("PyLinkCloud")
        PyLinkCloud.resize(1130, 480)
        self.centralwidget = QtWidgets.QWidget(PyLinkCloud)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scanBtn = QtWidgets.QPushButton(self.centralwidget)
        self.scanBtn.setObjectName("scanBtn")
        self.horizontalLayout.addWidget(self.scanBtn)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.headerItem().setText(1, "2")
        self.treeWidget.headerItem().setText(2, "3")
        self.horizontalLayout.addWidget(self.treeWidget)
        PyLinkCloud.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyLinkCloud)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 21))
        self.menubar.setObjectName("menubar")
        self.menuHello = QtWidgets.QMenu(self.menubar)
        self.menuHello.setObjectName("menuHello")
        PyLinkCloud.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyLinkCloud)
        self.statusbar.setObjectName("statusbar")
        PyLinkCloud.setStatusBar(self.statusbar)
        self.actionTODO = QtWidgets.QAction(PyLinkCloud)
        self.actionTODO.setObjectName("actionTODO")
        self.menuHello.addAction(self.actionTODO)
        self.menubar.addAction(self.menuHello.menuAction())

        self.retranslateUi(PyLinkCloud)
        QtCore.QMetaObject.connectSlotsByName(PyLinkCloud)

    def retranslateUi(self, PyLinkCloud):
        _translate = QtCore.QCoreApplication.translate
        PyLinkCloud.setWindowTitle(_translate("PyLinkCloud", "PyLinkCloud"))
        self.scanBtn.setText(_translate("PyLinkCloud", "Scan"))
        self.treeWidget.setSortingEnabled(True)
        self.menuHello.setTitle(_translate("PyLinkCloud", "File"))
        self.actionTODO.setText(_translate("PyLinkCloud", "TODO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyLinkCloud = QtWidgets.QMainWindow()
    ui = Ui_PyLinkCloud()
    ui.setupUi(PyLinkCloud)
    PyLinkCloud.show()
    sys.exit(app.exec_())

