# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\EMatt\OneDrive - Nova Scotia Community College\w0420789-MatthewsE\Programming\Git Repository\w0420789-MatthewsE\Assignments\Final_Project_Ethan_Matthews\Final_Project.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") 
        MainWindow.resize(809, 745)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCountryListTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelCountryListTitle.setGeometry(QtCore.QRect(20, 30, 331, 21))
        self.labelCountryListTitle.setObjectName("labelCountryListTitle")
        self.verticalScrollBarCountryLists = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBarCountryLists.setGeometry(QtCore.QRect(340, 60, 21, 621))
        self.verticalScrollBarCountryLists.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBarCountryLists.setObjectName("verticalScrollBarCountryLists")
        self.listWidgetCountry = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetCountry.setGeometry(QtCore.QRect(20, 60, 341, 621))
        self.listWidgetCountry.setObjectName("listWidgetCountry")
        self.frame_hider = QtWidgets.QFrame(self.centralwidget)
        self.frame_hider.setGeometry(QtCore.QRect(360, 0, 431, 691))
        self.frame_hider.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_hider.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_hider.setObjectName("frame_hider")
        self.labelPercentPop = QtWidgets.QLabel(self.frame_hider)
        self.labelPercentPop.setGeometry(QtCore.QRect(40, 630, 161, 21))
        self.labelPercentPop.setObjectName("labelPercentPop")
        self.lineEditPopulation = QtWidgets.QLineEdit(self.frame_hider)
        self.lineEditPopulation.setGeometry(QtCore.QRect(120, 375, 261, 31))
        self.lineEditPopulation.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"")
        self.lineEditPopulation.setObjectName("lineEditPopulation")
        self.labelPopulation = QtWidgets.QLabel(self.frame_hider)
        self.labelPopulation.setGeometry(QtCore.QRect(40, 374, 81, 31))
        self.labelPopulation.setAutoFillBackground(False)
        self.labelPopulation.setStyleSheet("")
        self.labelPopulation.setObjectName("labelPopulation")
        self.groupBoxPopulationDensity = QtWidgets.QGroupBox(self.frame_hider)
        self.groupBoxPopulationDensity.setGeometry(QtCore.QRect(40, 535, 341, 71))
        self.groupBoxPopulationDensity.setObjectName("groupBoxPopulationDensity")
        self.radioButtonSquareMile = QtWidgets.QRadioButton(self.groupBoxPopulationDensity)
        self.radioButtonSquareMile.setGeometry(QtCore.QRect(10, 20, 131, 17))
        self.radioButtonSquareMile.setStyleSheet("color: rgb(0, 0, 0);")
        self.radioButtonSquareMile.setObjectName("radioButtonSquareMile")
        self.radioButtonSquareKM = QtWidgets.QRadioButton(self.groupBoxPopulationDensity)
        self.radioButtonSquareKM.setGeometry(QtCore.QRect(10, 40, 131, 17))
        self.radioButtonSquareKM.setStyleSheet("color: rgb(0, 0, 0);")
        self.radioButtonSquareKM.setObjectName("radioButtonSquareKM")
        self.labelSquareAreaDisplay = QtWidgets.QLabel(self.groupBoxPopulationDensity)
        self.labelSquareAreaDisplay.setGeometry(QtCore.QRect(220, 25, 101, 30))
        self.labelSquareAreaDisplay.setText("")
        self.labelSquareAreaDisplay.setObjectName("labelSquareAreaDisplay")
        self.labelFlagImage = QtWidgets.QLabel(self.frame_hider)
        self.labelFlagImage.setGeometry(QtCore.QRect(90, 95, 241, 201))
        self.labelFlagImage.setText("")
        self.labelFlagImage.setObjectName("labelFlagImage")
        self.pushButtonUpdatePopulation = QtWidgets.QPushButton(self.frame_hider)
        self.pushButtonUpdatePopulation.setGeometry(QtCore.QRect(240, 425, 141, 31))
        self.pushButtonUpdatePopulation.setObjectName("pushButtonUpdatePopulation")
        self.labelTotalArea = QtWidgets.QLabel(self.frame_hider)
        self.labelTotalArea.setGeometry(QtCore.QRect(40, 485, 80, 31))
        self.labelTotalArea.setObjectName("labelTotalArea")
        self.labelPercentPopDisplay = QtWidgets.QLabel(self.frame_hider)
        self.labelPercentPopDisplay.setGeometry(QtCore.QRect(260, 629, 111, 21))
        self.labelPercentPopDisplay.setText("")
        self.labelPercentPopDisplay.setObjectName("labelPercentPopDisplay")
        self.labelVarCountryName = QtWidgets.QLabel(self.frame_hider)
        self.labelVarCountryName.setGeometry(QtCore.QRect(30, 20, 111, 31))
        self.labelVarCountryName.setText("")
        self.labelVarCountryName.setObjectName("labelVarCountryName")
        self.comboBoxMilesToKM = QtWidgets.QComboBox(self.frame_hider)
        self.comboBoxMilesToKM.setGeometry(QtCore.QRect(120, 491, 69, 20))
        self.comboBoxMilesToKM.setObjectName("comboBoxMilesToKM")
        self.labelVarTotalAreaIn = QtWidgets.QLabel(self.frame_hider)
        self.labelVarTotalAreaIn.setGeometry(QtCore.QRect(250, 485, 111, 31))
        self.labelVarTotalAreaIn.setText("")
        self.labelVarTotalAreaIn.setObjectName("labelVarTotalAreaIn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 26))
        self.menubar.setObjectName("menubar")
        self.menuFiel = QtWidgets.QMenu(self.menubar)
        self.menuFiel.setObjectName("menuFiel")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_File = QtWidgets.QAction(MainWindow)
        self.actionLoad_File.setObjectName("actionLoad_File")
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFiel.addAction(self.actionLoad_File)
        self.menuFiel.addAction(self.actionSave_File)
        self.menuFiel.addAction(self.actionExit)
        self.menubar.addAction(self.menuFiel.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelCountryListTitle.setText(_translate("MainWindow", "Choose A Country From the List:"))
        self.labelPercentPop.setText(_translate("MainWindow", "Percentage of World Population:"))
        self.labelPopulation.setText(_translate("MainWindow", " Population:"))
        self.groupBoxPopulationDensity.setTitle(_translate("MainWindow", "Population Density"))
        self.radioButtonSquareMile.setText(_translate("MainWindow", "Per Square Mile"))
        self.radioButtonSquareKM.setText(_translate("MainWindow", "Per Sqaure KM"))
        self.pushButtonUpdatePopulation.setText(_translate("MainWindow", "Update Population"))
        self.labelTotalArea.setText(_translate("MainWindow", "Total Area in:"))
        self.menuFiel.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_File.setText(_translate("MainWindow", "Load Countries"))
        self.actionSave_File.setText(_translate("MainWindow", "Save to File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

