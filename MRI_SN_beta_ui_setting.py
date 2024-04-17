"""
set ui function
like: button connect, menu connect, trigger function, etc.
"""

from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from MRI_SN_beta_view_2d import View


class UiSetting(QMainWindow):
    def __init__(self, ui, parent=None):
        super(UiSetting, self).__init__(parent)
        self.ui = ui
        self.initUiSetting()

    def initUiSetting(self):
        # Qmenu
        self.ui.actionAdd_Data.triggered.connect(self.addData)
        self.ui.actionSave_Data.triggered.connect(self.saveData)
        self.ui.actionUse_Sample_Data.triggered.connect(self.useSampleData)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionAbout_MRI_SN.triggered.connect(self.aboutMRI_SN)

        # QToolBar
        self.ui.actionView.triggered.connect(self.switchFuncArea)
        self.ui.actionFusion.triggered.connect(self.switchFuncArea)
        self.ui.actionVessel.triggered.connect(self.switchFuncArea)
        self.ui.actionFiber.triggered.connect(self.switchFuncArea)

        # QButton
        self.ui.view_test.clicked.connect(View.test)

    def addData(self):
        View.add_data(self)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        return super().mouseMoveEvent(a0)

    def saveData(self):
        print("save data")

    def useSampleData(self):
        print("use sample data")

    def exit(self):
        print("exit")

    def aboutMRI_SN(self):
        print("about MRI_SN")

    def switchFuncArea(self):
        """
        switch the stackedWidget to display different function area
        """
        try:
            action = self.sender()
            if action == self.ui.actionView:
                self.ui.stackedWidget.setCurrentIndex(0)
            elif action == self.ui.actionFusion:
                self.ui.stackedWidget.setCurrentIndex(1)
            elif action == self.ui.actionVessel:
                self.ui.stackedWidget.setCurrentIndex(2)
            elif action == self.ui.actionFiber:
                self.ui.stackedWidget.setCurrentIndex(3)
            else:
                pass
        except:
            print("Switch the stackedWidget error")
            meg_box = QMessageBox(QMessageBox.Critical, "ERROR", "Switch the stackedWidget error!")
            meg_box.exec_()
