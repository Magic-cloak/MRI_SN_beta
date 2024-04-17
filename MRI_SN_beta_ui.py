# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MRI_SN_beta.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 860)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.view_GroupBox = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.view_GroupBox.sizePolicy().hasHeightForWidth())
        self.view_GroupBox.setSizePolicy(sizePolicy)
        self.view_GroupBox.setMinimumSize(QtCore.QSize(760, 760))
        self.view_GroupBox.setObjectName("view_GroupBox")
        self.ImageShow = QtWidgets.QGridLayout(self.view_GroupBox)
        self.ImageShow.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.ImageShow.setSpacing(0)
        self.ImageShow.setObjectName("ImageShow")
        self.CorgridLayout = QtWidgets.QGridLayout()
        self.CorgridLayout.setObjectName("CorgridLayout")
        self.cor_ScrollBar = QtWidgets.QScrollBar(self.view_GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cor_ScrollBar.sizePolicy().hasHeightForWidth())
        self.cor_ScrollBar.setSizePolicy(sizePolicy)
        self.cor_ScrollBar.setMinimumSize(QtCore.QSize(20, 0))
        self.cor_ScrollBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cor_ScrollBar.setAutoFillBackground(False)
        self.cor_ScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.cor_ScrollBar.setInvertedAppearance(True)
        self.cor_ScrollBar.setInvertedControls(True)
        self.cor_ScrollBar.setObjectName("cor_ScrollBar")
        self.CorgridLayout.addWidget(self.cor_ScrollBar, 0, 1, 1, 1)
        self.cor_Label = QtWidgets.QLabel(self.view_GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cor_Label.sizePolicy().hasHeightForWidth())
        self.cor_Label.setSizePolicy(sizePolicy)
        self.cor_Label.setMinimumSize(QtCore.QSize(0, 20))
        self.cor_Label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.cor_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.cor_Label.setObjectName("cor_Label")
        self.CorgridLayout.addWidget(self.cor_Label, 1, 0, 1, 1)
        self.cor_OpenGLWidget = QtWidgets.QOpenGLWidget(self.view_GroupBox)
        self.cor_OpenGLWidget.setObjectName("cor_OpenGLWidget")
        self.CorgridLayout.addWidget(self.cor_OpenGLWidget, 0, 0, 1, 1)
        self.CorgridLayout.setColumnStretch(0, 1)
        self.CorgridLayout.setColumnStretch(1, 5)
        self.CorgridLayout.setRowStretch(0, 1)
        self.CorgridLayout.setRowStretch(1, 5)
        self.ImageShow.addLayout(self.CorgridLayout, 0, 1, 1, 1)
        self.SaggridLayout = QtWidgets.QGridLayout()
        self.SaggridLayout.setObjectName("SaggridLayout")
        self.sag_Label = QtWidgets.QLabel(self.view_GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sag_Label.sizePolicy().hasHeightForWidth())
        self.sag_Label.setSizePolicy(sizePolicy)
        self.sag_Label.setMinimumSize(QtCore.QSize(0, 20))
        self.sag_Label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sag_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.sag_Label.setObjectName("sag_Label")
        self.SaggridLayout.addWidget(self.sag_Label, 1, 0, 1, 1)
        self.sag_ScrollBar = QtWidgets.QScrollBar(self.view_GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sag_ScrollBar.sizePolicy().hasHeightForWidth())
        self.sag_ScrollBar.setSizePolicy(sizePolicy)
        self.sag_ScrollBar.setMinimumSize(QtCore.QSize(20, 0))
        self.sag_ScrollBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sag_ScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.sag_ScrollBar.setInvertedAppearance(True)
        self.sag_ScrollBar.setInvertedControls(True)
        self.sag_ScrollBar.setObjectName("sag_ScrollBar")
        self.SaggridLayout.addWidget(self.sag_ScrollBar, 0, 2, 1, 1)
        self.sag_OpenGLWidget = QtWidgets.QOpenGLWidget(self.view_GroupBox)
        self.sag_OpenGLWidget.setObjectName("sag_OpenGLWidget")
        self.SaggridLayout.addWidget(self.sag_OpenGLWidget, 0, 0, 1, 1)
        self.SaggridLayout.setColumnStretch(0, 1)
        self.SaggridLayout.setRowStretch(0, 1)
        self.ImageShow.addLayout(self.SaggridLayout, 1, 0, 1, 1)
        self.VolgridLayout = QtWidgets.QGridLayout()
        self.VolgridLayout.setObjectName("VolgridLayout")
        self.vol_OpenGLWidget = QtWidgets.QOpenGLWidget(self.view_GroupBox)
        self.vol_OpenGLWidget.setMinimumSize(QtCore.QSize(300, 300))
        self.vol_OpenGLWidget.setObjectName("vol_OpenGLWidget")
        self.VolgridLayout.addWidget(self.vol_OpenGLWidget, 0, 0, 1, 1)
        self.vol_Label = QtWidgets.QLabel(self.view_GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vol_Label.sizePolicy().hasHeightForWidth())
        self.vol_Label.setSizePolicy(sizePolicy)
        self.vol_Label.setMinimumSize(QtCore.QSize(0, 20))
        self.vol_Label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.vol_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.vol_Label.setObjectName("vol_Label")
        self.VolgridLayout.addWidget(self.vol_Label, 1, 0, 1, 1)
        self.vol_Label_Nan = QtWidgets.QLabel(self.view_GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vol_Label_Nan.sizePolicy().hasHeightForWidth())
        self.vol_Label_Nan.setSizePolicy(sizePolicy)
        self.vol_Label_Nan.setMinimumSize(QtCore.QSize(20, 0))
        self.vol_Label_Nan.setText("")
        self.vol_Label_Nan.setObjectName("vol_Label_Nan")
        self.VolgridLayout.addWidget(self.vol_Label_Nan, 0, 1, 1, 1)
        self.VolgridLayout.setRowStretch(0, 1)
        self.ImageShow.addLayout(self.VolgridLayout, 1, 1, 1, 1)
        self.AxigridLayout = QtWidgets.QGridLayout()
        self.AxigridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.AxigridLayout.setContentsMargins(0, -1, 0, 0)
        self.AxigridLayout.setSpacing(6)
        self.AxigridLayout.setObjectName("AxigridLayout")
        self.axi_ScrollBar = QtWidgets.QScrollBar(self.view_GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axi_ScrollBar.sizePolicy().hasHeightForWidth())
        self.axi_ScrollBar.setSizePolicy(sizePolicy)
        self.axi_ScrollBar.setMinimumSize(QtCore.QSize(20, 0))
        self.axi_ScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.axi_ScrollBar.setInvertedAppearance(True)
        self.axi_ScrollBar.setInvertedControls(True)
        self.axi_ScrollBar.setObjectName("axi_ScrollBar")
        self.AxigridLayout.addWidget(self.axi_ScrollBar, 0, 1, 1, 1)
        self.axi_OpenGLWidget = QtWidgets.QOpenGLWidget(self.view_GroupBox)
        self.axi_OpenGLWidget.setObjectName("axi_OpenGLWidget")
        self.AxigridLayout.addWidget(self.axi_OpenGLWidget, 0, 0, 1, 1)
        self.axi_Label = QtWidgets.QLabel(self.view_GroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axi_Label.sizePolicy().hasHeightForWidth())
        self.axi_Label.setSizePolicy(sizePolicy)
        self.axi_Label.setMinimumSize(QtCore.QSize(0, 20))
        self.axi_Label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.axi_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.axi_Label.setObjectName("axi_Label")
        self.AxigridLayout.addWidget(self.axi_Label, 1, 0, 1, 1)
        self.AxigridLayout.setColumnStretch(0, 1)
        self.AxigridLayout.setRowStretch(0, 1)
        self.ImageShow.addLayout(self.AxigridLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.view_GroupBox, 0, 1, 2, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.show_image = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.show_image.setGeometry(QtCore.QRect(30, 240, 231, 51))
        self.show_image.setObjectName("show_image")
        self.view_test = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.view_test.setGeometry(QtCore.QRect(30, 310, 231, 51))
        self.view_test.setObjectName("view_test")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.stackedWidgetPage1)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 700, 261, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Sag_pos = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.Sag_pos.setMinimumSize(QtCore.QSize(60, 20))
        self.Sag_pos.setMaximumSize(QtCore.QSize(60, 20))
        self.Sag_pos.setAlignment(QtCore.Qt.AlignCenter)
        self.Sag_pos.setObjectName("Sag_pos")
        self.horizontalLayout_4.addWidget(self.Sag_pos)
        self.Cor_pos = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.Cor_pos.setMinimumSize(QtCore.QSize(60, 20))
        self.Cor_pos.setMaximumSize(QtCore.QSize(60, 20))
        self.Cor_pos.setAlignment(QtCore.Qt.AlignCenter)
        self.Cor_pos.setObjectName("Cor_pos")
        self.horizontalLayout_4.addWidget(self.Cor_pos)
        self.Axi_pos = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.Axi_pos.setMinimumSize(QtCore.QSize(60, 20))
        self.Axi_pos.setMaximumSize(QtCore.QSize(60, 20))
        self.Axi_pos.setAlignment(QtCore.Qt.AlignCenter)
        self.Axi_pos.setObjectName("Axi_pos")
        self.horizontalLayout_4.addWidget(self.Axi_pos)
        self.Cursor_pos = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.Cursor_pos.setGeometry(QtCore.QRect(50, 670, 200, 20))
        self.Cursor_pos.setMinimumSize(QtCore.QSize(200, 20))
        self.Cursor_pos.setMaximumSize(QtCore.QSize(200, 20))
        self.Cursor_pos.setAlignment(QtCore.Qt.AlignCenter)
        self.Cursor_pos.setObjectName("Cursor_pos")
        self.file_list_widget = QtWidgets.QListWidget(self.stackedWidgetPage1)
        self.file_list_widget.setGeometry(QtCore.QRect(20, 50, 261, 171))
        self.file_list_widget.setObjectName("file_list_widget")
        self.label = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label.setGeometry(QtCore.QRect(120, 30, 54, 12))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QtWidgets.QWidget()
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.pushButton_3 = QtWidgets.QPushButton(self.stackedWidgetPage2)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 30, 241, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 50, 231, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 20, 241, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 2, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1218, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAdd_Data = QtWidgets.QAction(MainWindow)
        self.actionAdd_Data.setObjectName("actionAdd_Data")
        self.actionSave_Data = QtWidgets.QAction(MainWindow)
        self.actionSave_Data.setObjectName("actionSave_Data")
        self.actionUse_Sample_Data = QtWidgets.QAction(MainWindow)
        self.actionUse_Sample_Data.setObjectName("actionUse_Sample_Data")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_MRI_SN = QtWidgets.QAction(MainWindow)
        self.actionAbout_MRI_SN.setObjectName("actionAbout_MRI_SN")
        self.actionView = QtWidgets.QAction(MainWindow)
        self.actionView.setObjectName("actionView")
        self.actionFiber = QtWidgets.QAction(MainWindow)
        self.actionFiber.setObjectName("actionFiber")
        self.actionVessel = QtWidgets.QAction(MainWindow)
        self.actionVessel.setObjectName("actionVessel")
        self.actionFusion = QtWidgets.QAction(MainWindow)
        self.actionFusion.setObjectName("actionFusion")
        self.toolBar.addAction(self.actionView)
        self.toolBar.addAction(self.actionFusion)
        self.toolBar.addAction(self.actionVessel)
        self.toolBar.addAction(self.actionFiber)
        self.menuFile.addAction(self.actionAdd_Data)
        self.menuFile.addAction(self.actionSave_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUse_Sample_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_MRI_SN)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cor_Label.setText(_translate("MainWindow", "Coronal"))
        self.sag_Label.setText(_translate("MainWindow", "Saggital"))
        self.vol_Label.setText(_translate("MainWindow", "3D View"))
        self.axi_Label.setText(_translate("MainWindow", "Axial"))
        self.show_image.setText(_translate("MainWindow", "show image"))
        self.view_test.setText(_translate("MainWindow", "test View11"))
        self.Cursor_pos.setText(_translate("MainWindow", "Cursor Position (Sag,Cor,Axi)"))
        self.label.setText(_translate("MainWindow", "file_list"))
        self.pushButton_3.setText(_translate("MainWindow", "test Fusion"))
        self.pushButton_4.setText(_translate("MainWindow", "test Vessel"))
        self.pushButton_5.setText(_translate("MainWindow", "test Fiber"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAdd_Data.setText(_translate("MainWindow", "Add Data"))
        self.actionAdd_Data.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionSave_Data.setText(_translate("MainWindow", "Save Data"))
        self.actionSave_Data.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionUse_Sample_Data.setText(_translate("MainWindow", "Use Sample Data"))
        self.actionUse_Sample_Data.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout_MRI_SN.setText(_translate("MainWindow", "About MRI_SN_beta"))
        self.actionView.setText(_translate("MainWindow", "View"))
        self.actionView.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionFiber.setText(_translate("MainWindow", "Fiber"))
        self.actionFiber.setShortcut(_translate("MainWindow", "Ctrl+4"))
        self.actionVessel.setText(_translate("MainWindow", "Vessel"))
        self.actionVessel.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionFusion.setText(_translate("MainWindow", "Fusion"))
        self.actionFusion.setShortcut(_translate("MainWindow", "Ctrl+2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())