import json
import os
import cv2
import sys
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QLineEdit, QFileDialog#,QVBoxLayout,QApplication
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import  QRegExp, Qt
from PyQt5.uic import loadUi

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi("Principal.ui",self)
        self.setup()

    def asignarControlador(self, c):
        self.__mi_controlador = c

    def setup(self):
        self.boton_aceptar.clicked.connect(self.ingresarMenu)
        self.boton_salir.clicked.connect(lambda:self.close())
        self.nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.contrasena.setValidator(QIntValidator())
        self.contrasena.setEchoMode(QLineEdit.Password)

    def ingresarMenu(self):
        user = self.nombre.text()
        password = self.contrasena.text()

        if user != "" or password != "":
            with open("usuarios.json") as file:
                data = json.load(file)
                if user in data and data[user] == password:
                    ventana_menu = VentanaMenu(self)
                    self.hide()
                    ventana_menu.asignarControlador(self.__mi_controlador)
                    ventana_menu.show()
                else:
                    msg = QMessageBox(self)
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Usuario y/o contraseña incorrecta")
                    msg.setWindowTitle("Error")
                    msg.show()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Por favor, ingrese un usuario y/o contraseña.")
            msg.setWindowTitle("Error")
            msg.show()

class VentanaMenu(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        loadUi("Menu.ui",self)
        self.__ventana_padre=parent
        self.setup()

    def asignarControlador(self, c):
        self.__mi_controlador = c

    def setup(self):
        self.boton_imagenes.clicked.connect(self.rutaImagenes)
        self.boton_volver.clicked.connect(self.volverBoton)
        self.boton_salir.clicked.connect(lambda:self.close())

    def rutaImagenes(self):
        ventMenu =  VentanaRuta(self)
        ventMenu.show()
        self.hide()

    def volverBoton(self):
        self.__ventana_padre.show()
        self.hide()

class VentanaRuta(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        loadUi("Proceso_Imagenes.ui",self)
        self.__ventana_padre=parent
        self.setup()

    def asignarControlador(self,c):
        self.__mi_controlador = c

    def setup(self):
        self.examinar.clicked.connect(self.rutaImagenes)
        self.boton_volver.clicked.connect(self.volverBoton)

    def rutaImagenes(self):
        pass

    def volverBoton(self):
        self.__ventana_padre.show()
        self.hide()

class VentanaImagenDCM(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        loadUi("NOMBRE VENTANA QUE MUESTRA EL 3D DICOM",self)
        self.__ventana_padre=parent
        self.setup()

class VentanaImagenNifti(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        loadUi("NOMBRE VENTANA QUE MUESTRA EL 3D Nifti",self)
        self.__ventana_padre=parent
        self.setup()





        