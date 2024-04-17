"""
2d/3d view of the MRI data
"""

import SimpleITK as sitk
import vtkmodules.all as vtk
from PyQt5.QtWidgets import QFileDialog, QListWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject, pyqtSignal
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class Plane:
    def __init__(self, ui, name):
        names = ["sag", "cor", "axi", "vol"]
        frames = [
            ui.sag_OpenGLWidget,
            ui.cor_OpenGLWidget,
            ui.axi_OpenGLWidget,
            ui.vol_OpenGLWidget,
        ]
        index = names.index(name)
        self.ren = vtk.vtkRenderer()
        self.ren.SetBackground(1, 1, 1)  # set background color
        self.frame = frames[index]
        self.widget = QVTKRenderWindowInteractor(self.frame)
        self.renWin = self.widget.GetRenderWindow()
        self.renWin.AddRenderer(self.ren)
        self.iren = self.renWin.GetInteractor()
        if index == 3:
            self.style = vtk.vtkInteractorStyleTrackballCamera()  # 3d
        else:
            self.style = vtk.vtkInteractorStyleImage()  # 2d
        self.iren.SetInteractorStyle(self.style)
        self.renWin.Render()


class MyInteractorStyle(vtk.vtkInteractorStyleImage):
    def __init__(self, mode=None, renderer=None, view=None):
        super(MyInteractorStyle, self).__init__()
        self.mode = mode
        self.AddObserver("MouseMoveEvent", self.mouseMoveEvent)
        self.AddObserver("MouseWheelForwardEvent", self.mouseWheelForwardEvent)
        self.AddObserver("MouseWheelBackwardEvent", self.mouseWheelBackwardEvent)
        self.pointPicker = vtk.vtkPointPicker()
        self.render = renderer
        self.view = view

    def mouseMoveEvent(self, obj, event):
        self.OnMouseMove()
        x, y = self.GetInteractor().GetEventPosition()
        picker = vtk.vtkPointPicker()
        success = picker.Pick(x, y, 0, self.render)
        if success:
            picked_point = picker.GetPickPosition()
            
            if self.mode == "sag":
                point_3d = [
                        self.view.origin[0] + self.view.spacing[0] * int(self.view.extent[0] + self.view.slicer_index[0]),
                        self.view.center[1] - picked_point[0],
                        self.view.center[2] - picked_point[1],
                    ]
            if self.mode == "cor":
                point_3d = [
                        self.view.center[0] + picked_point[0],
                        self.view.origin[1] + self.view.spacing[1] * int(self.view.extent[2] + self.view.slicer_index[1]),
                        self.view.center[2] - picked_point[1],
                    ]
            if self.mode == "axi":
                point_3d = [
                        self.view.center[0] + picked_point[0],
                        self.view.center[1] + picked_point[1],
                        self.view.origin[2] + self.view.spacing[2] * int(self.view.extent[4] + self.view.slicer_index[2]),
                    ]
            self.view.mouse_move_signal.emit(point_3d)
            print(f"Picked point: {picked_point}")

    def mouseWheelForwardEvent(self, obj, event):
        if self.mode == "sag":
            View.slicer_index[0] -= 1
        if self.mode == "cor":
            View.slicer_index[1] -= 1
        if self.mode == "axi":
            View.slicer_index[2] -= 1
        self.view.show_slice(mode="reslice")
        print("mouse wheel forward: ", self.view.slicer_index)

    def mouseWheelBackwardEvent(self, obj, event):
        if self.mode == "sag":
            View.slicer_index[0] += 1
        if self.mode == "cor":
            View.slicer_index[1] += 1
        if self.mode == "axi":
            View.slicer_index[2] += 1
        self.view.show_slice(mode="reslice")
        print("mouse wheel backward: ", self.view.slicer_index)

    #     self._previous_mouse_position = self._current_mouse_position

    #     self.GetInteractor().GetRenderWindow().Render()


class View(QObject):
    data = None
    list_widget = None
    file_path = None
    sag_plane = None
    cor_plane = None
    axi_plane = None
    vol_plane = None

    origin = [0, 0, 0]
    center = [0, 0, 0]
    extent = [0, 0, 0, 0, 0, 0]
    direction = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    slicer_index = [0, 0, 0]

    sag_elments = None
    cor_elments = None
    axi_elments = None

    interactor_point = None
    mouse_move_signal = pyqtSignal(list)

    def __init__(self, ui):
        super(View, self).__init__()
        self.ui = ui
        View.list_widget = self.ui.file_list_widget
        View.file_path = None
        View.data = None
        
        View.sag_plane = Plane(ui=self.ui, name="sag")
        View.cor_plane = Plane(ui=self.ui, name="cor")
        View.axi_plane = Plane(ui=self.ui, name="axi")
        View.vol_plane = Plane(ui=self.ui, name="vol")

        View.sag_elements = [0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
        View.cor_elements = [0, -1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]
        View.axi_elements = [1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]

        View.interactor_point = vtk.vtkPointPicker()

        renderer_sag = View.sag_plane.iren.GetRenderWindow().GetRenderers().GetFirstRenderer()
        renderer_cor = View.cor_plane.iren.GetRenderWindow().GetRenderers().GetFirstRenderer()
        renderer_axi = View.axi_plane.iren.GetRenderWindow().GetRenderers().GetFirstRenderer()

        interactor_style_2d_axi = MyInteractorStyle(mode="axi", renderer=renderer_sag, view=self)
        interactor_style_2d_cor = MyInteractorStyle(mode="cor", renderer=renderer_cor, view=self)
        interactor_style_2d_sag = MyInteractorStyle(mode="sag", renderer=renderer_axi, view=self)
        interactor_style_3d = vtk.vtkInteractorStyleTrackballCamera()

        View.sag_plane.iren.SetInteractorStyle(interactor_style_2d_sag)
        View.cor_plane.iren.SetInteractorStyle(interactor_style_2d_cor)
        View.axi_plane.iren.SetInteractorStyle(interactor_style_2d_axi)
        View.vol_plane.iren.SetInteractorStyle(interactor_style_3d)

        self.initUiSetting()

    def initUiSetting(self):
        """
        link the button to the function
        """
        self.ui.show_image.clicked.connect(lambda: self.show_slice("init"))
        self.ui.view_test.clicked.connect(self.test)
        self.mouse_move_signal.connect(self.changeCursorPositionSignal)
        self.ui.file_list_widget.clicked.connect(self.fileListWidgetClicked)
        self.ui.sag_ScrollBar.valueChanged.connect(lambda value: self.changeScrollBar(value, mode="sag"))
        self.ui.cor_ScrollBar.valueChanged.connect(lambda value: self.changeScrollBar(value, mode="cor"))
        self.ui.axi_ScrollBar.valueChanged.connect(lambda value: self.changeScrollBar(value, mode="axi"))

    def fileListWidgetClicked(self):
        item = View.list_widget.currentItem()
        View.file_path = item.text()
        print("file path", self.file_path)

    def changeCursorPositionSignal(self, cursor_position):
        self.ui.Sag_pos.setText(str(round(cursor_position[0])))
        self.ui.Cor_pos.setText(str(round(cursor_position[1])))
        self.ui.Axi_pos.setText(str(round(cursor_position[2])))

    def changeScrollBar(self, value, mode=None):
        if mode == "sag":
            View.slicer_index[0] = value
        if mode == "cor":
            View.slicer_index[1] = value
        if mode == "axi":
            View.slicer_index[2] = value
        self.show_slice(mode="reslice")
        print("scroll bar value: ", View.slicer_index)

    def readNiftiFile(self):
        file_path = View.file_path
        reader = vtk.vtkNIFTIImageReader()
        reader.SetDataByteOrderToBigEndian()
        reader.SetFileName(file_path)
        reader.Update()

        image = sitk.ReadImage(file_path)
        data = vtk.vtkImageData()
        data.DeepCopy(reader.GetOutput())

        data.SetOrigin(image.GetOrigin())
        View.origin = data.GetOrigin()
        data.SetSpacing(image.GetSpacing())
        View.spacing = data.GetSpacing()
        data.SetDirectionMatrix(image.GetDirection())
        View.extent = data.GetExtent()
        #View.direction = vtk.vtkMatrix4x4()
        #View.direction.DeepCopy(data.GetDirectionMatrix())
        print("data origin", data.GetOrigin())
        print("data spacing", data.GetSpacing())
        print("data direction", data.GetDirectionMatrix())

        return data,reader

    def add_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "OpenFile", "", "Nii(*.nii.gz)", options=options)
        if file_path:
            View.list_widget.addItem(file_path)
            print("File path saved: ", file_path)

        else:
            print("NO file selected!")
            return

    def show_slice(self, mode="init"):
        if View.file_path is None:
            print("No file selected!")
            return
        else:
            if mode == "init":
                sag_resliceAxes = vtk.vtkMatrix4x4()
                sag_reslice = vtk.vtkImageReslice()
                sag_actor = vtk.vtkImageActor()

                cor_resliceAxes = vtk.vtkMatrix4x4()
                cor_reslice = vtk.vtkImageReslice()
                cor_actor = vtk.vtkImageActor()

                axi_resliceAxes = vtk.vtkMatrix4x4()
                axi_reslice = vtk.vtkImageReslice()
                axi_actor = vtk.vtkImageActor()

                direction_martixs = View.direction
                elements = [View.sag_elements, View.cor_elements, View.axi_elements]
                resliceAxes = [sag_resliceAxes, cor_resliceAxes, axi_resliceAxes]
                reslices = [sag_reslice, cor_reslice, axi_reslice]
                actors = [sag_actor, cor_actor, axi_actor]
                planes = [View.sag_plane, View.cor_plane, View.axi_plane]

                _, reader = self.readNiftiFile()
                View.slicer_index = [
                int((View.extent[1] + 1) / 2),
                int((View.extent[3] + 1) / 2),
                int((View.extent[5] + 1) / 2),
                ]
                self.ui.sag_ScrollBar.setRange(View.extent[0], View.extent[1])
                self.ui.cor_ScrollBar.setRange(View.extent[2], View.extent[3])
                self.ui.axi_ScrollBar.setRange(View.extent[4], View.extent[5])
                extent = View.extent
                spacing = View.spacing
                print("extent", extent)

                center = [0, 0, 0]
                for j in range(3):
                    center[j] = int(spacing[j] * 0.5 * (extent[2 * j] + extent[2 * j + 1]))
                print("center", center)
                for i in range(3):
                    #slice_direction_matrix = vtk.vtkMatrix4x4()
                    #vtk.vtkMatrix4x4.Multiply4x4(direction_martixs, elements[i], slice_direction_matrix)

                    resliceAxes[i].DeepCopy(elements[i])
                    resliceAxes[i].SetElement(0, 3, center[0])
                    resliceAxes[i].SetElement(1, 3, center[1])
                    resliceAxes[i].SetElement(2, 3, center[2])

                    # reslices[i].SetInputData(data)
                    reslices[i].SetInputConnection(reader.GetOutputPort())
                    reslices[i].SetOutputDimensionality(2)
                    reslices[i].SetResliceAxes(resliceAxes[i])
                    reslices[i].SetInterpolationModeToLinear()

                    colors = vtk.vtkImageMapToWindowLevelColors()
                    colors.SetInputConnection(reslices[i].GetOutputPort())
                    colors.SetWindow(351)
                    colors.SetLevel(176)

                    actors[i].GetMapper().SetInputConnection(colors.GetOutputPort())
                    actors[i].GetMapper().Update()

                    planes[i].ren.RemoveAllViewProps()
                    planes[i].ren.AddViewProp(actors[i])
                    planes[i].ren.GetActiveCamera().Zoom(1.0)
                    planes[i].ren.ResetCamera()
                    planes[i].renWin.Render()
                    print("show slice", i)
            if mode == "reslice":
                data = View.data
                sag_resliceAxes = vtk.vtkMatrix4x4()
                sag_reslice = vtk.vtkImageReslice()
                sag_actor = vtk.vtkImageActor()

                cor_resliceAxes = vtk.vtkMatrix4x4()
                cor_reslice = vtk.vtkImageReslice()
                cor_actor = vtk.vtkImageActor()

                axi_resliceAxes = vtk.vtkMatrix4x4()
                axi_reslice = vtk.vtkImageReslice()
                axi_actor = vtk.vtkImageActor()
                
                elements = [View.sag_elements, View.cor_elements, View.axi_elements]
                resliceAxes = [sag_resliceAxes, cor_resliceAxes, axi_resliceAxes]
                reslices = [sag_reslice, cor_reslice, axi_reslice]
                actors = [sag_actor, cor_actor, axi_actor]
                planes = [View.sag_plane, View.cor_plane, View.axi_plane]

                center = View.slicer_index
                reader = self.readNiftiFile()
                
                for i in range(3):
                    resliceAxes[i].DeepCopy(elements[i])
                    resliceAxes[i].SetElement(0, 3, center[0])
                    resliceAxes[i].SetElement(1, 3, center[1])
                    resliceAxes[i].SetElement(2, 3, center[2])

                    reslices[i].SetInputConnection(reader.GetOutputPort())
                    reslices[i].SetOutputDimensionality(2)
                    reslices[i].SetResliceAxes(resliceAxes[i])
                    reslices[i].SetInterpolationModeToLinear()

                    colors = vtk.vtkImageMapToWindowLevelColors()
                    colors.SetInputConnection(reslices[i].GetOutputPort())
                    colors.SetWindow(351)
                    colors.SetLevel(176)

                    actors[i].GetMapper().SetInputConnection(colors.GetOutputPort())
                    actors[i].GetMapper().Update()

                    planes[i].ren.RemoveAllViewProps()
                    planes[i].ren.AddViewProp(actors[i])
                    planes[i].ren.GetActiveCamera().Zoom(1.0)
                    planes[i].ren.ResetCamera()
                    planes[i].renWin.Render()
                    print("show slice", i)


            if mode == None:
                print("mode is not set , it is", mode)


    def test(self):
        colors = vtk.vtkNamedColors()
        cylinder = vtk.vtkCylinderSource()
        cylinder.SetResolution(8)
        cylinderMapper = vtk.vtkPolyDataMapper()
        cylinderMapper.SetInputConnection(cylinder.GetOutputPort())
        cylinderActor = vtk.vtkActor()
        cylinderActor.SetMapper(cylinderMapper)
        cylinderActor.GetProperty().SetColor(colors.GetColor3d("Tomato"))
        cylinderActor.RotateX(60.0)
        cylinderActor.RotateY(-45.0)

        View.vol_plane.ren.AddActor(cylinderActor)
        View.vol_plane.ren.SetBackground(colors.GetColor3d("BkgColor"))

        View.vol_plane.renWin.Render()
