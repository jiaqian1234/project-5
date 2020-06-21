# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#import import_ipynb
from LayoutCanvas import *
from Slab import *
from LayoutCanvas import *
from raytracingGUI import *
from simulation import *
from CurrentSlabDBDialog import *
from MessageBox import showMessageBox
class Ui_MainWindow(object):
    
    def __init__(self):
        self.L=Layout()
        
        self.boundaryAdded = False
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ######Gridlayout
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 70, 511, 591))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 11, 6, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 4, 1, 3)
        self.line_7 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 21, 3, 1, 4)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 5, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 5, 6, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 4, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 5, 1, 1)
        self.pushButton_more = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_more.setObjectName("pushButton_more")
        self.gridLayout.addWidget(self.pushButton_more, 0, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 4, 3, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 4, 2, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 10, 3, 1, 4)
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 3, 1, 4)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 3, 1, 4)
        self.spinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 12, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 6, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 3, 1, 1)
        self.pushButton_deleteNode = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_deleteNode.setObjectName("pushButton_deleteNode")
        self.gridLayout.addWidget(self.pushButton_deleteNode, 9, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 5, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 7, 4, 1, 3)
        self.spinBox_3 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_3.setMinimum(-100)
        self.spinBox_3.setMaximum(0)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout.addWidget(self.spinBox_3, 8, 6, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 4, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 11, 5, 1, 1)
        self.label_SegmentIndex = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_SegmentIndex.setObjectName("label_SegmentIndex")
        self.gridLayout.addWidget(self.label_SegmentIndex, 16, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 12, 5, 1, 1)
        self.label_deleteSegment = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_deleteSegment.setObjectName("label_deleteSegment")
        self.gridLayout.addWidget(self.label_deleteSegment, 16, 4, 1, 1)
        
        self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 15, 4, 1, 3)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 13, 5, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 13, 6, 1, 1)
        self.pushButton_addSegment = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_addSegment.setObjectName("pushButton_addSegment")
        self.gridLayout.addWidget(self.pushButton_addSegment, 14, 6, 1, 1)
        self.spinBox_deleteSegmentIndex = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_deleteSegmentIndex.setObjectName("spinBox_deleteSegmentIndex")
        self.gridLayout.addWidget(self.spinBox_deleteSegmentIndex, 16, 6, 1, 1)
        self.pushButton_deleteSegment = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_deleteSegment.setObjectName("pushButton_deleteSegment")
        self.gridLayout.addWidget(self.pushButton_deleteSegment, 17, 6, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 11, 4, 4, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 11, 3, 7, 1)
        
        #### Furniture
        self.label_furniture = QtWidgets.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_furniture, 22, 3, 7, 1)
        self.label_furniture.setObjectName("label_furniture")
        
        self.label_addfurniture = QtWidgets.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_addfurniture, 22, 4, 1, 1)
        self.label_addfurniture.setObjectName("label_addfurniture")
        
        self.label_origin = QtWidgets.QLabel(self.centralwidget)
        self.label_origin.setGeometry(QtCore.QRect(330, 660, 101, 16))
        self.gridLayout.addWidget(self.label_origin, 22,5, 2, 1)
        self.label_origin.setObjectName("label_origin")
        
        self.doubleSpinBox_originx = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.gridLayout.addWidget(self.doubleSpinBox_originx, 22, 6, 1, 1)
        self.doubleSpinBox_originx.setObjectName("doubleSpinBox_originx")
        
        self.doubleSpinBox_originy = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.gridLayout.addWidget(self.doubleSpinBox_originy, 23, 6, 1, 1)
        self.doubleSpinBox_originy.setObjectName("doubleSpinBox_originy")
        
        self.label_furangle = QtWidgets.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_furangle, 26, 5, 1, 1)
        self.label_furangle.setObjectName("label_furangle")
        
        self.label_furlength = QtWidgets.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_furlength, 24, 5, 1, 1)
        self.label_furlength.setObjectName("label_furlength")
        
        self.label_furwidth = QtWidgets.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_furwidth, 25, 5, 1, 1)
        self.label_furwidth.setObjectName("label_furwidth")
        
        self.doubleSpinBox_furlength = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.gridLayout.addWidget(self.doubleSpinBox_furlength, 24, 6, 1, 1)
        self.doubleSpinBox_furlength.setObjectName("doubleSpinBox_furlength")
        
        self.doubleSpinBox_furwidth = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.gridLayout.addWidget(self.doubleSpinBox_furwidth, 25, 6, 1, 1)
        self.doubleSpinBox_furwidth.setObjectName("doubleSpinBox_furwidth")
        
        self.doubleSpinBox_furangle = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.gridLayout.addWidget(self.doubleSpinBox_furangle, 26, 6, 1, 1)
        self.doubleSpinBox_furangle.setObjectName("doubleSpinBox_furangle")
        
        self.label_furmaterial = QtWidgets.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_furmaterial, 27, 5, 1, 1)
        self.label_furmaterial.setObjectName("label_furmaterial")
        
        self.comboBox_furmat = QtWidgets.QComboBox(self.centralwidget)
        self.gridLayout.addWidget(self.comboBox_furmat, 27, 6, 1, 1)
        self.comboBox_furmat.setObjectName("comboBox_furmat")
        
        self.pushButton_loadfurfile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadfurfile.setObjectName("pushButton_loadfurfile")
        self.gridLayout.addWidget(self.pushButton_loadfurfile, 28, 6, 1, 1)
        
        self.pushButton_addfur = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addfur.setObjectName("pushButton_addfur")
        self.gridLayout.addWidget(self.pushButton_addfur, 29, 6, 1, 1)
        
        self.line_fur = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_fur.setFrameShape(QtWidgets.QFrame.HLine)
        #self.line_fur.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_fur.setObjectName("line_fur")
        self.gridLayout.addWidget(self.line_fur, 30, 3, 7, 1)
        ####
        self.pushButton_displayLayout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_displayLayout.setGeometry(QtCore.QRect(510, 680, 80, 26))
        self.pushButton_displayLayout.setObjectName("pushButton_displayLayout")
        self.spinBox_2.setMinimum(-100)
        self.spinBox_2.setMaximum(0)
        self.spinBox.setMinimum(-100)
        self.spinBox.setMaximum(0)
        
        ######Table
        self.tableWidget_1 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_1.setGeometry(QtCore.QRect(720, 70, 211, 151))
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(2)
        self.tableWidget_1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, item)
        
        
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(990, 70, 300, 151))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(120)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        
        ###Menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1256, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSlab_definition = QtWidgets.QMenu(self.menubar)
        self.menuSlab_definition.setObjectName("menuSlab_definition")
        self.menuRaytracing = QtWidgets.QMenu(self.menubar)
        self.menuRaytracing.setObjectName("menuRaytracing")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew_2 = QtWidgets.QAction(MainWindow)
        self.actionNew_2.setObjectName("actionNew_2")
        self.actionInitial_SlabDB = QtWidgets.QAction(MainWindow)
        self.actionInitial_SlabDB.setObjectName("actionInitial_SlabDB")
        self.actionSimulation = QtWidgets.QAction(MainWindow)
        self.actionSimulation.setObjectName("actionSimulation")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuSlab_definition.addAction(self.actionNew_2)
        self.menuSlab_definition.addAction(self.actionInitial_SlabDB)
        self.menuRaytracing.addAction(self.actionSimulation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSlab_definition.menuAction())
        self.menubar.addAction(self.menuRaytracing.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        MainWindow.setMenuBar(self.menubar)
        #####
        
        
        #####Display
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(700, 250, 591, 501)) 
        self.widget.setObjectName("widget")		
        self.widget_3 = LayoutCanvas(self.widget, width=10, height=10, dpi=100)
        self.widget_3.setGeometry(QtCore.QRect(0, 100, 591, 380))
        self.widget_3.setObjectName("widget_3")
        #self.widget_3.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.widget_2 = NavigationToolbar(self.widget_3, self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 591, 61))
        self.widget_2.setObjectName("widget_2")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widget_3)
        layout.addWidget(self.widget_2)
        self.widget.setLayout(layout)
        
        
           
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        ####
        self.menuFile.setTitle(_translate("MainWindow", "Layout"))
        self.menuSlab_definition.setTitle(_translate("MainWindow", "Slab Database"))
        self.menuRaytracing.setTitle(_translate("MainWindow", "Ray Tracing"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionNew_2.setText(_translate("MainWindow", "New"))
        self.actionInitial_SlabDB.setText(_translate("MainWindow", "Initial SlabDB"))
        self.actionSimulation.setText(_translate("MainWindow", "Simulation"))
        
        
        
        self.comboBox.setItemText(0, _translate("MainWindow", "indoor"))
        self.comboBox.setItemText(1, _translate("MainWindow", "outdoor"))
        self.label_8.setText(_translate("MainWindow", "secondNode"))
        self.pushButton_addSegment.setText(_translate("MainWindow", "Confirm"))
        self.label_11.setText(_translate("MainWindow", "addSegment"))
        self.label_7.setText(_translate("MainWindow", "Y"))
        self.lineEdit.setText(_translate("MainWindow", "slabDB.ini"))
        self.label_6.setText(_translate("MainWindow", "X"))
        self.pushButton_more.setText(_translate("MainWindow", "more"))
        self.label_2.setText(_translate("MainWindow", "addNode"))
        self.pushButton.setText(_translate("MainWindow", "Confirm"))
        self.label.setText(_translate("MainWindow", "Type"))
        self.label_3.setText(_translate("MainWindow", "deleteNode"))
        self.label_SegmentIndex.setText(_translate("MainWindow", "Index"))
        self.label_5.setText(_translate("MainWindow", "Segment"))
        self.pushButton_deleteSegment.setText(_translate("MainWindow", "Confirm"))
        self.label_4.setText(_translate("MainWindow", "Node"))
        self.label_14.setText(_translate("MainWindow", "SlabDatabase"))
        self.label_deleteSegment.setText(_translate("MainWindow", "deleteSegment"))
        self.pushButton_deleteNode.setText(_translate("MainWindow", "Confirm"))
        self.label_10.setText(_translate("MainWindow", "Index"))
        self.label_15.setText(_translate("MainWindow", "Slab"))
        self.label_9.setText(_translate("MainWindow", "firstNode"))
        self.pushButton_displayLayout.setText(_translate("MainWindow", "Display"))
        
        
        item = self.tableWidget_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Node Index"))
        item = self.tableWidget_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Position"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Segment Index"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Center point"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Slab"))
        
        
        # Furniture
        self.label_furniture.setText(_translate("MainWindow", "Furnniture"))
        self.label_addfurniture.setText(_translate("MainWindow", "add Furniture"))
        self.label_origin.setText(_translate("MainWindow", "Origin point (x,y)"))
        self.label_furangle.setText(_translate("MainWindow", "Angle"))
        self.label_furlength.setText(_translate("MainWindow", "Length"))
        self.label_furwidth.setText(_translate("MainWindow", "Width"))
        self.label_furmaterial.setText(_translate("MainWindow", "Material"))
        self.pushButton_addfur.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_loadfurfile.setText(_translate("MainWindow", "Load furnitures from File"))
        ###set content to slab comboBox
        self.S = SlabDB("slabDB.ini")
        Slab_list = list(self.S.keys())
        self.comboBox_3.insertItems(0, Slab_list)
        
        ###set content to material comboBox
        self.setmaterialComboBox()
        ###connect
        self.pushButton.clicked.connect(self.add_node)
        self.pushButton_deleteNode.clicked.connect(self.delete_node)
        self.pushButton_addSegment.clicked.connect(self.add_segment)
        self.pushButton_displayLayout.clicked.connect(self.displayLayout)
        self.pushButton_more.clicked.connect(self.Button_more)
        self.actionSimulation.triggered.connect(self.onSimulationButtonClick)
        self.actionSave.triggered.connect(self.onSaveToolBarButtonClick)
        self.actionOpen.triggered.connect(self.onOpenToolBarButtonClick)
        self.actionNew.triggered.connect(self.onNewToolBarButtonClick)
        self.actionNew_2.triggered.connect(self.slab_definition)
        self.actionInitial_SlabDB.triggered.connect(self.onCurrentSlabDBButtonClick)
        self.pushButton_deleteSegment.clicked.connect(self.delete_segment)
        self.pushButton_addfur.clicked.connect(self.onAddFurnitureButtonClick)
        
        self.pushButton_loadfurfile.clicked.connect(self.onLoadFurnitureFromFile)
    
    def onLoadFurnitureFromFile(self):
        fileName_tup = QFileDialog.getOpenFileName(None, "Open file", "", "*.ini")
        fileName = fileName_tup[0]
        self.L.add_furniture_file(_filefur=fileName)
    
        
    def setmaterialComboBox(self):
        self.comboBox_furmat.clear()
        self.matDB = MatDB('matDB.ini')
        self.comboBox_furmat.insertItems(0, list(self.matDB.keys()))
           
            
    def reloadSlab(self):
        Slab_list = list(self.S.keys())
        self.comboBox_3.clear()
        self.comboBox_3.insertItems(0, Slab_list)
    
    def slab_definition(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Slab()
        ui.setupUi(Dialog)
        
        Dialog.show()
        Dialog.exec_()   
    def onCurrentSlabDBButtonClick(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_CurrentSlabDialog(self.S)
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()  
    
    def onAddFurnitureButtonClick(self):
        origin = (self.doubleSpinBox_originx.value(), self.doubleSpinBox_originy.value())
        width = self.doubleSpinBox_furwidth.value()
        length = self.doubleSpinBox_furlength.value()
        angle = self.doubleSpinBox_furangle.value()
        mat   = self.comboBox_furmat.currentText()
        self.L.add_furniture(mat_name = mat, origin = origin, width = width, length = length, height = 3, angle = angle) 
        old_name = self.L._filename
        self.L._filename = 'templayoutwithfur.lay'
        self.L.save()
        self.L = Layout('templayoutwithfur.lay')
        self.L._filename = old_name
        
    def onNewToolBarButtonClick(self, s):
        self.L = Layout()
        #self.label_graphic.setPixmap(QtGui.QPixmap() )
        self.widget_3.axes.cla()
        self.widget_3.draw()
        self.S = SlabDB("slabDB.ini")
        self.boundaryAdded = False
        self.reloadSlab()
        self.showSegmentsTable()
        self.showNodesTable()
        
    def onSaveToolBarButtonClick(self, s):
        fileName_tup = QFileDialog.getSaveFileName(None, "Save file", "", ".lay")
        fileName = ''.join(fileName_tup)
        # TODO: Check that the filename was actually given: if fileName != "....lay"
        if not fileName_tup[1]:
            showMessageBox('File was not saved', True)
            return
        if not self.boundaryAdded:
            self.L.boundary()
            self.boundaryAdded = True
        self.L._filename = fileName
        self.L.save()
    
    def onOpenToolBarButtonClick(self, s):
        fileName_tup = QFileDialog.getOpenFileName(None, "Open file", "", "*.lay")
        fileName = fileName_tup[0]
        self.L =  Layout(fileName)
        self.S = self.L.sl
        self.boundaryAdded = True
        self.reloadSlab()
        self.lineEdit.setText(" ")
        self.displayLayout()
        self.showSegmentsTable()
        self.showNodesTable()
    
    
    def add_node(self):
        position = (self.doubleSpinBox.value(),self.doubleSpinBox_2.value())
        self.L.add_fnod(position)
        self.doubleSpinBox.setProperty("value", 0.0)
        self.doubleSpinBox_2.setProperty("value", 0.0)
        self.displayLayout()
        self.showNodesTable()
    
    def showNodesTable(self):
        dic = dict(self.L.Gs.pos)
        self.tableWidget_1.setRowCount(0)
        for k,v in list(dic.items()):
             if k<0:
                node = (k,v)
                print(node)
                node = str(node)
                node = node[1:]
                node = node[:-1]
                node = node.split(',')
                numRows = self.tableWidget_1.rowCount()
                print(numRows)
                self.tableWidget_1.insertRow(numRows)     
                item_1 = QtWidgets.QTableWidgetItem(node[0])
                item_2 = QtWidgets.QTableWidgetItem(node[1]+','+node[2])
                self.tableWidget_1.setItem(numRows, 0, item_1)
                self.tableWidget_1.setItem(numRows, 1, item_2)

    def delete_node(self):
        index = self.spinBox_3.value()
        if index not in self.L.Gs.node:
            showMessageBox('Index node is invalid, try again')
            return
        self.L.del_points ([index])
        self.spinBox_3.setProperty("value",0)    
        self.displayLayout()
        self.showNodesTable()
        
    def showSegmentsTable(self):
        dic = dict(self.L.Gs.pos)
        self.tableWidget_2.setRowCount(0)
        for k,v in list(dic.items()):
             if k>0:
                node = (k,v)
                #print(type(node[0]))
                node = str(node)
                node = node[1:]
                node = node[:-1]
                node = node.split(',')
                numRows = self.tableWidget_2.rowCount()
                #print(numRows)
                self.tableWidget_2.insertRow(numRows)     
                item_1 = QtWidgets.QTableWidgetItem(node[0])
                item_2 = QtWidgets.QTableWidgetItem(node[1]+','+node[2])
                item_3 = QtWidgets.QTableWidgetItem(str(self.L.Gs.node[int(node[0])]['name']))
                self.tableWidget_2.setItem(numRows, 0, item_1)
                self.tableWidget_2.setItem(numRows, 1, item_2)
                self.tableWidget_2.setItem(numRows, 2, item_3)
    def add_segment(self):
        node_1 = self.spinBox.value()
        node_2 = self.spinBox_2.value()
        if node_1 not in self.L.Gs.node:
            showMessageBox('Node index is invalid, try again')
            return 
        if node_2 not in self.L.Gs.node:
            showMessageBox('Node index is invalid, try again')
            return 
        slab_name = self.comboBox_3.currentText()
        self.L.add_segment(node_1,node_2, name = slab_name)
        self.spinBox.setProperty("value", 0.0)
        self.spinBox.setProperty("value", 0.0)
        self.spinBox_2.setProperty("value", 0.0)
        self.spinBox_2.setProperty("value", 0.0)
        self.showSegmentsTable()
        self.displayLayout()

        
    def delete_segment(self):
        segmentIndex =  self.spinBox_deleteSegmentIndex.value()
        if segmentIndex not in self.L.Gs.node:
            showMessageBox('Segment index is invalid, try again')
            return
        self.L.del_segment(segmentIndex)
        self.displayLayout()
        self.showSegmentsTable()
    
    def Button_more(self):
        fileName_tup = QFileDialog.getOpenFileName(None, "Open file", "", "*.ini")
        fileAddress = fileName_tup[0]
        fileName = fileAddress.split('/')[-1]
        self.lineEdit.setText(fileName)
        S = SlabDB(fileAddress)
        self.L=Layout(fileslabini =fileAddress)
        Slab_list = list(S.keys())
        self.comboBox_3.clear()    
        self.comboBox_3.insertItems(0, Slab_list)
        
        
    def onSimulationButtonClick(self):
        try:
            Dialog = QtWidgets.QDialog()
            uiForm = Ui_RayTracing(self.L)
            uiForm.setupUi(Dialog)
            uiForm.displayLayout()
            Dialog.show()
            Dialog.exec_()
        except Exception as e:
            showMessageBox('Raytracing cannot be started: ' + str(e))
        
    def displayLayout(self):
        # TODO: check if the graph is consistent before printing
        self.widget_3.axes.cla()
        f,a = self.L.showG('s',nodes=True,labels=True,node_color='g', ax = self.widget_3.axes)
        self.widget_3.draw()
    
    def loadFurnitureFromFile(self):
        #todo
        return

if __name__ == "__main__":
    import sys
    from pylayers.gis.layout import *
    from pylayers.antprop.slab import *
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTextEdit, QMainWindow, QAction
    from PyQt5.QtGui import QIcon
    from pathlib import Path
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())