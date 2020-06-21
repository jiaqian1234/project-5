# -*- coding: utf-8 -*-

# Dialog implementation generated from reading ui file 'RayTracing.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTextEdit, QMainWindow, QAction
from PyQt5.QtGui import QIcon
import numpy as np
from LayoutCanvas import *
from pylayers.gis.layout import *
from simulation.PyLayersSimulation import *
from simulation.UWBSimulationInternalClock import *
from IPython.display import Image
from pylayers.antprop.slab import *
from pylayers.simul.link import *
import os
from pylayers.location.geometric.constraints.cla import *
from pylayers.location.geometric.constraints.toa import *
from math import sqrt
from pylayers.location.geometric.constraints.cla import *
import pylayers.util.pyutil as pyu
from pylayers.location.geometric.constraints.toa import *
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
from MessageBox import showMessageBox
import numpy as np

class Ui_RayTracing(object):
    def __init__(self, Layout= Layout()):
        self.L = Layout
        self.L._filename = os.path.basename(self.L._filename)
        self.L.build()
        self.anchors =  np.array([[],[]]) #np.array([[7,0,3],[1.5,0,5]]) 
        self.trajectory = np.array([[],[]]) #np.array([[0.5,2,3,4], [1,2,3,1.5]]) #
        
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1457, 875)
        #####
        self.layout_widget = QtWidgets.QWidget(Dialog)
        self.layout_widget.setGeometry(QtCore.QRect(450, 20, 901, 581))
        self.layout_widget.setObjectName("layout_widget")
        
        self.widget_plot = LayoutCanvas(self.layout_widget, width=10, height=10, dpi=100)
        self.widget_plot.setGeometry(QtCore.QRect(0, 100, 781, 500))
        self.widget_plot.setObjectName("Layout Plot")
        #self.widget_3.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        
        self.widget_naviToolbar = NavigationToolbar(self.widget_plot, self.layout_widget)
        self.widget_naviToolbar.setGeometry(QtCore.QRect(0, 20, 771, 71))
        self.widget_naviToolbar.setObjectName("widget_2")
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widget_plot)
        layout.addWidget(self.widget_naviToolbar)
        
        self.layout_widget.setLayout(layout)
        #####
        self.layoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_4.setGeometry(QtCore.QRect(40, 380, 311, 311))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_anchorsTable = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_anchorsTable.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_anchorsTable.setObjectName("gridLayout_anchorsTable")
        self.label_editAnchor = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_editAnchor.setObjectName("label_editAnchor")
        self.gridLayout_anchorsTable.addWidget(self.label_editAnchor, 0, 0, 1, 1)
        self.tableWidget_anchors = QtWidgets.QTableWidget(self.layoutWidget_4)
        self.tableWidget_anchors.setObjectName("tableWidget_anchors")
        self.tableWidget_anchors.setColumnCount(3)
        self.tableWidget_anchors.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anchors.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anchors.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()###
        self.tableWidget_anchors.setHorizontalHeaderItem(2, item)###
        self.gridLayout_anchorsTable.addWidget(self.tableWidget_anchors, 1, 0, 1, 2)
        self.pushButton_loadAnchors = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_loadAnchors.setObjectName("pushButton_loadAnchors")
        self.gridLayout_anchorsTable.addWidget(self.pushButton_loadAnchors, 2, 0, 1, 1)
        self.pushButton_newEntryAnchorsTable = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_newEntryAnchorsTable.setObjectName("pushButton_newEntryAnchorsTable")
        self.gridLayout_anchorsTable.addWidget(self.pushButton_newEntryAnchorsTable, 2, 1, 1, 1)
        self.layoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_5.setGeometry(QtCore.QRect(40, 20, 311, 331))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gridLayout_trajectoryTable = QtWidgets.QGridLayout(self.layoutWidget_5)
        self.gridLayout_trajectoryTable.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_trajectoryTable.setObjectName("gridLayout_trajectoryTable")
        self.label_edit_trajectory = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_edit_trajectory.setObjectName("label_edit_trajectory")
        self.gridLayout_trajectoryTable.addWidget(self.label_edit_trajectory, 0, 0, 1, 1)
        self.pushButton_loadTrajectory = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_loadTrajectory.setObjectName("pushButton_loadTrajectory")
        self.gridLayout_trajectoryTable.addWidget(self.pushButton_loadTrajectory, 2, 0, 1, 1)
        self.pushButton_newEntryTrajectory = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_newEntryTrajectory.setObjectName("pushButton_newEntryTrajectory")
        self.gridLayout_trajectoryTable.addWidget(self.pushButton_newEntryTrajectory, 2, 1, 1, 1)
        self.tableWidget_trajectory = QtWidgets.QTableWidget(self.layoutWidget_5)
        self.tableWidget_trajectory.setObjectName("tableWidget_trajectory")
        self.tableWidget_trajectory.setColumnCount(3)
        self.tableWidget_trajectory.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trajectory.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trajectory.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()###
        self.tableWidget_trajectory.setHorizontalHeaderItem(2, item)####

        self.gridLayout_trajectoryTable.addWidget(self.tableWidget_trajectory, 1, 0, 1, 2)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(498, 640, 314, 22))
        self.widget.setObjectName("widget")
        self.gridLayout_interpolation = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_interpolation.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_interpolation.setObjectName("gridLayout_interpolation")
        self.checkBox_smoothTrajextory = QtWidgets.QCheckBox(self.widget)
        self.checkBox_smoothTrajextory.setObjectName("checkBox_smoothTrajextory")
        self.gridLayout_interpolation.addWidget(self.checkBox_smoothTrajextory, 0, 0, 1, 1)
        self.label_interpolationPoints = QtWidgets.QLabel(self.widget)
        self.label_interpolationPoints.setObjectName("label_interpolationPoints")
        self.gridLayout_interpolation.addWidget(self.label_interpolationPoints, 0, 1, 1, 1)
        self.spinBox_interpolationPoints = QtWidgets.QSpinBox(self.widget)
        self.spinBox_interpolationPoints.setObjectName("spinBox_interpolationPoints")
        self.gridLayout_interpolation.addWidget(self.spinBox_interpolationPoints, 0, 2, 1, 1)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(501, 670, 475, 22))
        self.widget1.setObjectName("widget1")
        self.gridLayout_rayTracing = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_rayTracing.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_rayTracing.setObjectName("gridLayout_rayTracing")
        self.label_fGHz = QtWidgets.QLabel(self.widget1)
        self.label_fGHz.setObjectName("label_fGHz")
        self.gridLayout_rayTracing.addWidget(self.label_fGHz, 0, 0, 1, 1)
        self.doubleSpinBox_fGHz = QtWidgets.QDoubleSpinBox(self.widget1)
        self.doubleSpinBox_fGHz.setObjectName("doubleSpinBox_fGHz")
        self.gridLayout_rayTracing.addWidget(self.doubleSpinBox_fGHz, 0, 1, 1, 1)
        self.label_BWGHz = QtWidgets.QLabel(self.widget1)
        self.label_BWGHz.setObjectName("label_BWGHz")
        self.gridLayout_rayTracing.addWidget(self.label_BWGHz, 0, 2, 1, 1)
        self.doubleSpinBox_BWGHz = QtWidgets.QDoubleSpinBox(self.widget1)
        self.doubleSpinBox_BWGHz.setObjectName("doubleSpinBox_BWGHz")
        self.gridLayout_rayTracing.addWidget(self.doubleSpinBox_BWGHz, 0, 3, 1, 1)
        self.label_cutoff = QtWidgets.QLabel(self.widget1)
        self.label_cutoff.setObjectName("label_cutoff")
        self.gridLayout_rayTracing.addWidget(self.label_cutoff, 0, 4, 1, 1)
        self.spinBox_cutoff = QtWidgets.QSpinBox(self.widget1)
        self.spinBox_cutoff.setObjectName("spinBox_cutoff")
        self.gridLayout_rayTracing.addWidget(self.spinBox_cutoff, 0, 5, 1, 1)
        self.checkBox_default = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_default.setChecked(True)
        self.checkBox_default.setObjectName("checkBox_default")
        self.gridLayout_rayTracing.addWidget(self.checkBox_default, 0, 6, 1, 1)
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(500, 710, 516, 22))
        self.widget2.setObjectName("widget2")
        self.gridLayout_simulationMode = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_simulationMode.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_simulationMode.setObjectName("gridLayout_simulationMode")
        self.label_simulationmode = QtWidgets.QLabel(self.widget2)
        self.label_simulationmode.setObjectName("label_simulationmode")
        self.gridLayout_simulationMode.addWidget(self.label_simulationmode, 0, 0, 1, 1)
        self.comboBox_simulationMode = QtWidgets.QComboBox(self.widget2)
        self.comboBox_simulationMode.setObjectName("comboBox_simulationMode")
        self.comboBox_simulationMode.addItem("")
        self.comboBox_simulationMode.addItem("")
        self.gridLayout_simulationMode.addWidget(self.comboBox_simulationMode, 0, 1, 1, 1)
        self.label_rootanchor = QtWidgets.QLabel(self.widget2)
        self.label_rootanchor.setObjectName("label_rootanchor")
        self.gridLayout_simulationMode.addWidget(self.label_rootanchor, 0, 2, 1, 1)
        self.comboBox_root = QtWidgets.QComboBox(self.widget2)
        self.comboBox_root.setObjectName("comboBox_root")
        self.gridLayout_simulationMode.addWidget(self.comboBox_root, 0, 3, 1, 1)
        self.label_noisevariance = QtWidgets.QLabel(self.widget2)
        self.label_noisevariance.setObjectName("label_noisevariance")
        self.gridLayout_simulationMode.addWidget(self.label_noisevariance, 0, 4, 1, 1)
        self.doubleSpinBox_noisevariance = QtWidgets.QDoubleSpinBox(self.widget2)
        self.doubleSpinBox_noisevariance.setObjectName("doubleSpinBox_noisevariance")
        self.gridLayout_simulationMode.addWidget(self.doubleSpinBox_noisevariance, 0, 5, 1, 1)
        self.widget3 = QtWidgets.QWidget(Dialog)
        self.widget3.setGeometry(QtCore.QRect(100, 710, 162, 71))
        self.widget3.setObjectName("widget3")
        self.gridLayout_display = QtWidgets.QGridLayout(self.widget3)
        self.gridLayout_display.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_display.setObjectName("gridLayout_display")
        self.checkBox_showTrajectory = QtWidgets.QCheckBox(self.widget3)
        self.checkBox_showTrajectory.setObjectName("checkBox_showTrajectory")
        self.gridLayout_display.addWidget(self.checkBox_showTrajectory, 0, 0, 1, 2)
        self.checkBox_showAnchors = QtWidgets.QCheckBox(self.widget3)
        self.checkBox_showAnchors.setObjectName("checkBox_showAnchors")
        self.gridLayout_display.addWidget(self.checkBox_showAnchors, 1, 0, 1, 2)
        self.pushButton_updateLayout = QtWidgets.QPushButton(self.widget3)
        self.pushButton_updateLayout.setObjectName("pushButton_updateLayout")
        self.gridLayout_display.addWidget(self.pushButton_updateLayout, 2, 0, 1, 1)
        self.pushButton_Reset = QtWidgets.QPushButton(self.widget3)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.gridLayout_display.addWidget(self.pushButton_Reset, 2, 1, 1, 1)
        self.widget4 = QtWidgets.QWidget(Dialog)
        self.widget4.setGeometry(QtCore.QRect(499, 741, 731, 54))
        self.widget4.setObjectName("widget4")
        self.gridLayout_raytracingexecution = QtWidgets.QGridLayout(self.widget4)
        self.gridLayout_raytracingexecution.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_raytracingexecution.setObjectName("gridLayout_raytracingexecution")
        self.pushButton_start = QtWidgets.QPushButton(self.widget4)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_raytracingexecution.addWidget(self.pushButton_start, 0, 0, 1, 1)
        self.progressBar_raytracingprogress = QtWidgets.QProgressBar(self.widget4)
        self.progressBar_raytracingprogress.setProperty("value", 0)
        self.progressBar_raytracingprogress.setObjectName("progressBar_raytracingprogress")
        self.gridLayout_raytracingexecution.addWidget(self.progressBar_raytracingprogress, 0, 1, 1, 1)
        self.pushButton_saveresult = QtWidgets.QPushButton(self.widget4)
        self.pushButton_saveresult.setObjectName("pushButton_saveresult")
        self.gridLayout_raytracingexecution.addWidget(self.pushButton_saveresult, 1, 0, 1, 1)
        self.comboBox_saveResultMode = QtWidgets.QComboBox(self.widget4)
        self.comboBox_saveResultMode.setObjectName("comboBox_saveResultMode")
        self.gridLayout_raytracingexecution.addWidget(self.comboBox_saveResultMode, 1, 1, 1, 1)
        
        self.comboBox_saveResultMode.addItem("")
        self.comboBox_saveResultMode.addItem("")
        self.comboBox_saveResultMode.addItem("")
        self.comboBox_saveResultMode.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_editAnchor.setText(_translate("Dialog", "Edit anchor nodes"))
        item = self.tableWidget_anchors.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "x-coordinate"))
        item = self.tableWidget_anchors.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "y-coordinate"))
        item = self.tableWidget_anchors.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", ""))
        self.pushButton_loadAnchors.setText(_translate("Dialog", "Load Anchors From File"))
        self.pushButton_newEntryAnchorsTable.setText(_translate("Dialog", "New entry"))
        self.label_edit_trajectory.setText(_translate("Dialog", "Edit Trajectory"))
        self.pushButton_loadTrajectory.setText(_translate("Dialog", "Load Trajetory From File"))
        self.pushButton_newEntryTrajectory.setText(_translate("Dialog", "New entry"))
        item = self.tableWidget_trajectory.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "x-coordinate"))
        item = self.tableWidget_trajectory.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "y-coordinate"))
        item = self.tableWidget_trajectory.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", ""))
        self.checkBox_smoothTrajextory.setText(_translate("Dialog", "Smooth trajectory? "))
        self.label_interpolationPoints.setText(_translate("Dialog", "Number of interpolation points"))
        self.label_fGHz.setText(_translate("Dialog", "Frequency in GHz"))
        self.label_BWGHz.setToolTip(_translate("Dialog", "<html><head/><body><p>TODO</p><p><br/></p></body></html>"))
        self.label_BWGHz.setText(_translate("Dialog", "Bandwidth GHz"))
        self.label_cutoff.setText(_translate("Dialog", "Cutoff"))
        self.spinBox_cutoff.setToolTip(_translate("Dialog", "<html><head/><body><p>TODO</p><p><br/></p></body></html>"))
        self.checkBox_default.setText(_translate("Dialog", "Use default value"))
        self.label_simulationmode.setText(_translate("Dialog", "Simulation mode"))
        self.comboBox_simulationMode.setItemText(0, _translate("Dialog", "Intersection Box - pylayers"))
        self.comboBox_simulationMode.setItemText(1, _translate("Dialog", "Internal clocks"))
        self.label_rootanchor.setText(_translate("Dialog", "Root anchor"))
        self.label_noisevariance.setText(_translate("Dialog", "Noise variance"))
        self.checkBox_showTrajectory.setText(_translate("Dialog", "Show Trajectory"))
        self.checkBox_showAnchors.setText(_translate("Dialog", "Show Anchors"))
        self.pushButton_updateLayout.setText(_translate("Dialog", "Update Layout"))
        self.pushButton_Reset.setText(_translate("Dialog", "Reset"))
        self.pushButton_start.setText(_translate("Dialog", "Start"))
        self.pushButton_saveresult.setText(_translate("Dialog", "Save Result"))
        
        self.comboBox_saveResultMode.setItemText(0, _translate("Dialog", "trajectory_real"))
        self.comboBox_saveResultMode.setItemText(1, _translate("Dialog", "trajectory_estimated"))
        self.comboBox_saveResultMode.setItemText(2, _translate("Dialog", "anchors"))
        self.comboBox_saveResultMode.setItemText(3, _translate("Dialog", "time of arrival"))

        
        #######
        self.pushButton_updateLayout.clicked.connect(self.onUpdateLayoutButtonClicked) 
        self.pushButton_start.clicked.connect(self.onStartRayTracingButtonClicked) 
        self.pushButton_newEntryAnchorsTable.clicked.connect(self.onNewAnchorEntryClicked)
        self.pushButton_newEntryTrajectory.clicked.connect(self.onNewTrajectoryEntryClicked)
        self.pushButton_saveresult.clicked.connect(self.onSaveButtonClicked)
        self.pushButton_loadTrajectory.clicked.connect(self.onLoadTrajectory)
        self.pushButton_loadAnchors.clicked.connect(self.onLoadAnchor)
        self.pushButton_Reset.clicked.connect(self.onResetButtonClicked)
        self.comboBox_simulationMode.currentIndexChanged.connect(self.showLocalizationChoices)
        self.displayLayout()
        self.hideLocalizationChoices()
        #self.tableWidget.cellChanged.connect(self.onAnchorCellChanged)
        #self.tableWidget_2.cellChanged.connect(self.onAnchorCellChanged)
        
        
        ###
    #@QtCore.pyqtSlot()
    def showLocalizationChoices(self,mode):
        print("########",type(mode))
        if (mode  == 1):
            self.comboBox_root.setVisible(True)
            self.doubleSpinBox_noisevariance.setVisible(True)
            self.label_rootanchor.setVisible(True)
            self.label_noisevariance.setVisible(True)
            self.fillRootComboBox()
        else:
            self.hideLocalizationChoices()
    
    def fillRootComboBox(self):
        self.comboBox_root.clear()
        
        for i in range (1, self.tableWidget_anchors.rowCount() + 1):
            self.comboBox_root.addItem(str(i))

    def hideLocalizationChoices(self):
        self.comboBox_root.setVisible(False)
        self.doubleSpinBox_noisevariance.setVisible(False)
        self.label_rootanchor.setVisible(False)
        self.label_noisevariance.setVisible(False)
    def loadData(self):
        try:
            fileName_tup = QFileDialog.getOpenFileName(None, "Open file", "", "*.csv")
            fileName = fileName_tup[0]
            data = np.genfromtxt(fileName,delimiter=',')
        except Exception as e:
            showMessageBox('No file was loaded', True)
            return
        return data
    
    def onLoadTrajectory(self):
        self.tableWidget_trajectory.setRowCount(0)
        data = self.loadData()
        for row in range(len(data)):
            numRows = self.tableWidget_trajectory.rowCount()
            self.tableWidget_trajectory.insertRow(numRows)
            for column in range(len(data[row])):
                self.tableWidget_trajectory.setItem(numRows, column, QtWidgets.QTableWidgetItem(str(data[row][column])))
                
    def onLoadAnchor(self):
        self.tableWidget_anchors.setRowCount(0)
        data = self.loadData()
        for row in range(len(data)):
            numRows = self.tableWidget_anchors.rowCount()
            self.tableWidget_anchors.insertRow(numRows)
            for column in range(len(data[row])):
                self.tableWidget_anchors.setItem(numRows, column, QtWidgets.QTableWidgetItem(str(data[row][column])))
            
    def onSaveButtonClicked(self):
        self.updateSimulationData()
        try:
            #name of csv file
            fileName_tup = QFileDialog.getSaveFileName(None, "Save file", "", ".csv")
            fileName = ''.join(fileName_tup)
        except:
            showMessageBox('File was not saved',True)
        #fileName = dataname+".csv"
        # my data rows as dictionary objects 
        dataname = self.comboBox_saveResultMode.currentText()
        chosen_data = self.readData(dataname)  
        toa_header = ''
        for i in range(len(self.anchors[0])):
            toa_header = toa_header+'anchor'+str(i+1)+','
        toa_header = toa_header[:-1]

        # header names  
        headers = {'trajectory_real':'x_coordinary,y_coordinary',
                  'trajectory_estimated':'x_coordinary,y_coordinary',
                  'anchors':'x_coordinary,y_coordinary',
                  'time of arrival':toa_header}  

        # writing to csv file  
        np.savetxt(fileName,chosen_data,fmt='%f', delimiter=',', newline='\n', header=headers[dataname])
    
    
    def readData(self,dataname):
        traj_real = np.transpose(self.trajectory)
        traj_estimated = np.transpose(self.est)
        anchors = np.transpose(self.anchors)
        toas = self.toas
        datadict = {'trajectory_real':traj_real,
                   'trajectory_estimated':traj_estimated,
                   'anchors':anchors,
                   'time of arrival':toas}  
        data = datadict[dataname]
        return data
    
    def smoothTrajectory(self, trajectory, interpolation = 2):
        
        x = trajectory[0]
        y = trajectory[1]
        print('######', x)
        print(y)
        try:
            spl = splrep(x, y, k=2)
            x2 = np.array([])
            for i in range(len(x)-1):
                x1 = np.linspace(x[i], x[i+1], interpolation)
                x2 = np.append(x2,x1)
            print('x2:',x2)
            y2 = splev(x2, spl)
            smooth = [x2,y2]
        except Exception as e:
            smooth = [x,y]
            showMessageBox('fail to smooth trajectory because of the chosen points: ' + str(e))
        
        return smooth

    def displayLayout(self, show_anchors = False, show_traj = False):
        # TODO: check if the graph is consistent before printing
        # clear
        self.widget_plot.axes.cla()
        f,a = self.L.showG('s', ax = self.widget_plot.axes)
        
        if show_anchors:
            for i in range(0, len(self.anchors[0])):
                self.widget_plot.axes.plot(self.anchors[0][i],self.anchors[1][i], 'or', color = 'red')
        if show_traj:
            if self.tableWidget_trajectory.rowCount() <= 2:
                self.widget_plot.axes.plot(self.trajectory[0],self.trajectory[1], 'or',ls = '--', color = 'green')
            else: 
                if (self.checkBox_smoothTrajextory.isChecked()):
                    self.smoothed_trajectory = self.smoothTrajectory(self.trajectory, self.spinBox_interpolationPoints.value())
                else:
                    self.smoothed_trajectory = self.trajectory
                #self.smoothed_trajectory = self.smoothTrajectory(self.trajectory)
                #print('smooth',self.smoothed_trajectory[0],self.smoothed_trajectory[1])
                self.widget_plot.axes.plot(self.smoothed_trajectory[0],self.smoothed_trajectory[1], ls = '--', color = 'green')
                self.widget_plot.axes.plot(self.trajectory[0],self.trajectory[1], 'o', color = 'green')
        self.widget_plot.axes.legend(loc='best')
        # update
        self.widget_plot.draw()
    
    def onUpdateLayoutButtonClicked(self):
        self.updateSimulationData()
        show_anchors =  self.checkBox_showAnchors.isChecked()
        show_traj = self.checkBox_showTrajectory.isChecked()
        self.displayLayout(show_anchors, show_traj)
    
    def onResetButtonClicked(self):
        self.anchors =  np.array([[],[]])
        self.trajectory = np.array([[],[]])
        self.tableWidget_trajectory.setRowCount(0)
        self.tableWidget_anchors.setRowCount(0)
        self.displayLayout()
        
    def onStartRayTracingButtonClicked(self):
        self.updateSimulationData()
        self.displayLayout(True, True)
        if not self.checkBox_default.isChecked():
            fGHz = self.doubleSpinBox_fGHz.value()
            BWGHz = self.doubleSpinBox_BWGHz.value()
            cutoff = self.spinBox_cutoff.value()
    
            if fGHz == 0 or BWGHz == 0:
                showMessageBox('Frequencies are not valid. Try again')
                return
            if cutoff == 0:
                showMessageBox('Cutoff value is invalid. Try again')
                return
        else:
            fGHz = 0.9
            BWGHz = 0.5
            cutoff = 1
        if len(self.anchors[0]) == 0: 
            showMessageBox('No anchors found. Try again')
            return
        if len(self.trajectory[0]) == 0:
            showMessageBox('No trajectory found. Try again')
            return
        #try: 
        if (self.checkBox_smoothTrajextory.isChecked()):
            smoothed_trajectory = self.smoothTrajectory(self.trajectory, self.spinBox_interpolationPoints.value())
        else:
            smoothed_trajectory = self.trajectory
        print (self.comboBox_simulationMode.currentText())
        print (type(self.comboBox_simulationMode.currentText()))
        if self.comboBox_simulationMode.currentText() == 'Intersection Box - pylayers':
            self.est =  self.pylayersSimulation(smoothed_trajectory, fGHz,BWGHz, cutoff)
        else:
            self.est =  self.internalClockSimulation(smoothed_trajectory, self.doubleSpinBox_noisevariance.value(), fGHz,BWGHz, cutoff)
        #except Exception as e:
       #     showMessageBox('Error from pylayers library: ' +  str(e))
         #   return
        self.displayLayout(True, True)
      
        self.widget_plot.axes.plot(self.est[0],self.est[1], ls = '--', color = 'blue', label = 'Estimated Trajectory')
        self.widget_plot.axes.plot(self.est[0],self.est[1], 'o', color = 'blue')
        self.widget_plot.draw()
        
    def pylayersSimulation(self, smoothed_trajectory, fGHz,BWGHz, cutoff):
        try:
            sim = PyLayersUWBRayTracingSimulation (self.L, self.anchors, smoothed_trajectory, fGHz,BWGHz, cutoff)
            [self.est,self.toas] = sim.TrajectorySimulation(self.widget_plot, self.progressBar_raytracingprogress)###
        except Exception as e:
            showMessageBox("Errors during simulaytion: try another cutoff value or another interpolation points number:" + str(e), True)
        return self.est
    def internalClockSimulation(self, smoothed_trajectory, noise_var, fGHz,BWGHz, cutoff):
        r = int(self.comboBox_root.currentText())
        root = [self.anchors[0][r],self.anchors[1][r]]
        anchors = self.anchors
        # remove root from anchors list
        np.delete(anchors, r, 1)
        sim = UWBSimulationInternalClock(self.L, root, anchors,smoothed_trajectory, noise_var, cutoff, fGHz, BWGHz)
        return sim.trajectorySimulationInternalClocks()
    def onNewAnchorEntryClicked(self):
        self.updateSimulationData()
        self.displayLayout(True, True)
        self.tableWidget_anchors.insertRow(self.tableWidget_anchors.rowCount())
        ######
        deleteButton = QtWidgets.QPushButton("delete")
        self.tableWidget_anchors.setCellWidget(self.tableWidget_anchors.rowCount()-1, 2,deleteButton)
        deleteButton.clicked.connect(self.deleteAnchorClicked)

        
    def onNewTrajectoryEntryClicked(self):
        self.updateSimulationData()
        self.displayLayout(True, True)
        self.tableWidget_trajectory.insertRow(self.tableWidget_trajectory.rowCount())
        deleteButton = QtWidgets.QPushButton("delete")
        self.tableWidget_trajectory.setCellWidget(self.tableWidget_trajectory.rowCount()-1, 2, deleteButton)
        deleteButton.clicked.connect(self.deleteTrajectoryClicked)
   
        
    #@QtCore.pyqtSlot()
    def deleteAnchorClicked(self):
        button = self.Dialog.sender()
        if button:
            row = self.tableWidget_anchors.indexAt(button.pos()).row()
            self.tableWidget_anchors.removeRow(row)
            
    #@QtCore.pyqtSlot()
    def deleteTrajectoryClicked(self):
        button = self.Dialog.sender()
        if button:
            row = self.tableWidget_trajectory.indexAt(button.pos()).row()
            self.tableWidget_trajectory.removeRow(row)
    
    #def onAnchorCellChanged(self):
        #self.cell = self.tableWidget_2.currentItem()
    
    def updateSimulationData(self):
        trajectory = self.handleInputTable(self.tableWidget_trajectory)
        self.trajectory = trajectory
        anchors = self.handleInputTable(self.tableWidget_anchors)
        self.anchors = anchors
        
        
    def handleInputTable(self, table):
        input_array = np.array([[],[]])
        try:
            for i in range(table.rowCount()):
                item_1 = float(table.item(i,0).text())
                item_2 = float(table.item(i,1).text())
                new_item = [[item_1],[item_2]]
                input_array = np.append(input_array, new_item, axis = 1)
        except:
            showMessageBox('Please make sure that the input data is valid')
            #eturn
        return input_array
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    L = Layout('testLayout.lay')
    ui = Ui_RayTracing(L)
    ui.anchors = np.array([[1,2,3,4],[4,3,4,2]])
    ui.trajectory = np.array([[1,4],[2,3]])
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

