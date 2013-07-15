# -*- coding: utf-8 -*-
from PyQt4.QtGui import QMainWindow,  QFileDialog,  QTreeWidgetItem
from PyQt4.QtCore import pyqtSignature,  QString

from Ui_LogParser import Ui_MainWindow

from Parser import Parser

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_LogParser import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_btnParse_clicked(self):
        """
        Slot documentation goes here.
        """
        self.tvResult.clear()
        fName = self.lblPath.text()
        pattern = self.txtReToMatch.displayText()
        parser = Parser.Parser(fName)
        parser.parseLogFile(pattern)
        
        if 0<len(parser.lastError):
            self.lblPath.setText(parser.lastError)
        else:
            for ip_k in parser.parsedRecords.keys():
                item = QTreeWidgetItem(self.tvResult)
                item.setText(0,  ip_k)
                self.tvResult.addTopLevelItem(item)
                for ua_k in parser.parsedRecords[ip_k].keys():
                    item2 = QTreeWidgetItem(item)
                    item2.setText(0,  ua_k)
                    item.addChild(item2)
                    for logEntry in parser.parsedRecords[ip_k][ua_k]:
                        item3 = QTreeWidgetItem(item2)
                        item3.setText(0,  logEntry.urlReq)
                        item3.setText(1,  logEntry.dateTime)
                        item2.addChild(item3)
    
    @pyqtSignature("")
    def on_actionOpen_log_file_triggered(self):
        """
        Slot documentation goes here.
        """
        fName = QFileDialog.getOpenFileName(None, self.trUtf8("Select a W3SVC log file to parse"), QString(), self.trUtf8("*.log"), None)
        self.lblPath.setText(fName)
    
    @pyqtSignature("")
    def on_actionQuit_triggered(self):
        """
        Slot documentation goes here.
        """
        self.close()
    
    @pyqtSignature("")
    def on_actionAbout_triggered(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.information(self, "About", "IIS log files parser")
