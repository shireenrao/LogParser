# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/shireenrao/mydev/python/LogParser/logparser/ui/LogParser.ui'
#
# Created: Mon Jul 15 09:31:50 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblPath = QtGui.QLabel(self.centralWidget)
        self.lblPath.setObjectName(_fromUtf8("lblPath"))
        self.gridLayout.addWidget(self.lblPath, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtReToMatch = QtGui.QLineEdit(self.centralWidget)
        self.txtReToMatch.setObjectName(_fromUtf8("txtReToMatch"))
        self.horizontalLayout.addWidget(self.txtReToMatch)
        self.btnParse = QtGui.QPushButton(self.centralWidget)
        self.btnParse.setObjectName(_fromUtf8("btnParse"))
        self.horizontalLayout.addWidget(self.btnParse)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tvResult = QtGui.QTreeWidget(self.centralWidget)
        self.tvResult.setObjectName(_fromUtf8("tvResult"))
        self.tvResult.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout.addWidget(self.tvResult, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_log_file = QtGui.QAction(MainWindow)
        self.actionOpen_log_file.setObjectName(_fromUtf8("actionOpen_log_file"))
        self.actionQuit_1 = QtGui.QAction(MainWindow)
        self.actionQuit_1.setObjectName(_fromUtf8("actionQuit_1"))
        self.actionAbout_3 = QtGui.QAction(MainWindow)
        self.actionAbout_3.setObjectName(_fromUtf8("actionAbout_3"))
        self.actionSample = QtGui.QAction(MainWindow)
        self.actionSample.setObjectName(_fromUtf8("actionSample"))
        self.actionFinish = QtGui.QAction(MainWindow)
        self.actionFinish.setObjectName(_fromUtf8("actionFinish"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_log_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_1)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout_3)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lblPath.setText(_translate("MainWindow", "Please, load a log file", None))
        self.btnParse.setText(_translate("MainWindow", "Parse Log File", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen_log_file.setText(_translate("MainWindow", "Open log file", None))
        self.actionQuit_1.setText(_translate("MainWindow", "Quit App", None))
        self.actionAbout_3.setText(_translate("MainWindow", "About Me", None))
        self.actionSample.setText(_translate("MainWindow", "Sample", None))
        self.actionFinish.setText(_translate("MainWindow", "Finish", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

