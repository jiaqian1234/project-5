# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CurrentSlabDBDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pylayers.antprop.slab import *
import sys
from pylayers.gis.layout import *
from pylayers.antprop.slab import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTextEdit, QMainWindow, QAction
from PyQt5.QtGui import QIcon
from pathlib import Path
class Ui_CurrentSlabDialog(object):
    def __init__(self, slabDB):
        self.S = slabDB
        
    def setupUi(self, CurrentSlabDialog):
        CurrentSlabDialog.setObjectName("CurrentSlabDialog")
        CurrentSlabDialog.resize(800, 600)
        self.label = QtWidgets.QLabel(CurrentSlabDialog)
        self.label.setGeometry(QtCore.QRect(170, 0, 551, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(CurrentSlabDialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 80, 700, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        #self.tableWidget.resizeColumnsToContents()
        self.retranslateUi(CurrentSlabDialog)
        QtCore.QMetaObject.connectSlotsByName(CurrentSlabDialog)
        self.displayContents()

    def retranslateUi(self, CurrentSlabDialog):
        _translate = QtCore.QCoreApplication.translate
        CurrentSlabDialog.setWindowTitle(_translate("CurrentSlabDialog", "Dialog"))
        self.label.setText(_translate("CurrentSlabDialog", "Here is an overview of the slab database of the current layout:"))
        self.tableWidget.setToolTip(_translate("CurrentSlabDialog", "<html><head/><body><p>TODO Material</p><p><br/></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("CurrentSlabDialog", "Slab name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("CurrentSlabDialog", "Materials"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("CurrentSlabDialog", "Color"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("CurrentSlabDialog", "Thickness"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("CurrentSlabDialog", "Material details"))
        
    def displayContents(self):
        dic = dict(self.S)
        self.tableWidget.setRowCount(len(dic))
        numRows = 0
        for k,v in list(dic.items()):
            self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(v['name']))
            self.tableWidget.setItem(numRows, 1,  QtWidgets.QTableWidgetItem(str(v['lmatname'])))
            self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem( v['color']))
            self.tableWidget.setItem(numRows, 3, QtWidgets.QTableWidgetItem(str(v['lthick'])))
            self.tableWidget.setItem(numRows, 4, QtWidgets.QTableWidgetItem(str(v['lmat'])))
            numRows = numRows + 1
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrentSlabDialog = QtWidgets.QDialog()
    S = SlabDB("slabDB.ini")
    ui = Ui_CurrentSlabDialog(S)
   
    ui.setupUi(CurrentSlabDialog)
    CurrentSlabDialog.show()
    sys.exit(app.exec_())

