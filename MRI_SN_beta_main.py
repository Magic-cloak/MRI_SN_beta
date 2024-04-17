import sys
import numpy as np
import vtkmodules.all as vtk
from PyQt5.QtWidgets import QMainWindow, QApplication


from MRI_SN_beta_ui import Ui_MainWindow
from MRI_SN_beta_ui_setting import UiSetting
from MRI_SN_beta_view_2d import View


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        """
        data 
        """

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui_setting = UiSetting(self.ui)

        self.View = View(self.ui)

    def closeEvent(self, QCloseEvent):
        super().closeEvent(QCloseEvent)
        self.View.sag_plane.widget.Finalize()
        self.View.cor_plane.widget.Finalize()
        self.View.axi_plane.widget.Finalize()
        self.View.vol_plane.widget.Finalize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("MRI_SN_beta_V1")
    win.show()
    sys.exit(app.exec_())
