import json
import os
from vedo import Volume, show
from vedo.applications import RayCastPlotter
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QLineEdit, QTableWidgetItem
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import  QRegExp, Qt
from PyQt5.uic import loadUi

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi("Principal.ui",self)
        self.setup()

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

    def asignarControlador(self, c):
        self.__mi_controlador = c

class VentanaMenu(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        loadUi("Menu.ui",self)
        self.__ventana_padre=parent
        self.setup()

    def setup(self):
        self.boton_imagenes.clicked.connect(self.rutaImagenesDCM)
        self.boton_nifti.clicked.connect(self.rutaImagenesNifti)
        self.boton_salir.clicked.connect(lambda:self.close())

    def asignarControlador(self, c):
        self.__mi_controlador = c

    def rutaImagenesDCM(self):
        ventMenu =  VentanaRutaDCM(self)
        ventMenu.asignarControlador(self.__mi_controlador)
        ventMenu.show()
        self.hide()

    def rutaImagenesNifti(self):
        ventMenu1 =  VentanaRutaNifti(self)
        ventMenu1.asignarControlador(self.__mi_controlador)
        ventMenu1.show()
        self.hide()

    def volverBoton(self):
        self.__ventana_padre.show()
        self.hide()

class VentanaRutaDCM(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        loadUi("Proceso_Imagenes.ui",self)
        self.__ventana_padre=parent
        self.setup()

    def setup(self):
        self.examinar.clicked.connect(self.rutaImagenDCM)
        self.boton_volver.clicked.connect(self.volverBoton)

    def rutaImagenDCM(self):
        self.ruta = self.nombre_dcm.text()
        self.cargo = self.__mi_controlador.cargarDCM(self.ruta)
        self.convierto = self.__mi_controlador.convertir(self.ruta)
        self.carpetaNueva = './nifti'
        for archivo in os.listdir(self.carpetaNueva):
          if archivo.endswith('.nii.gz'):
            self.ruta = os.path.join(self.carpetaNueva,archivo)
            malla = Volume(self.ruta)
            malla.mode(1).cmap("jet") 
            plt = RayCastPlotter(malla, axes=7)
            show(malla, zoom=1.2, bg="black", viewup="z").close() 
            self.hide()

    def asignarControlador(self,c):
        self.__mi_controlador = c
    
    def volverBoton(self):
        self.__ventana_padre.show()
        self.hide()

class VentanaRutaNifti(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        loadUi("Proceso_Imagenes_Nifti.ui",self)
        self.__ventana_padre=parent
        self.setup()

    def asignarControlador(self,c):
        self.__mi_controlador = c

    def setup(self):
        self.examinar.clicked.connect(self.rutaImagenNifti)
        self.boton_volver.clicked.connect(self.volverBoton)

    def rutaImagenNifti(self):
        self.ruta = self.nombre_nifti.text()
        malla = Volume(self.ruta)
        malla.mode(1).cmap("jet") 
        plt = RayCastPlotter(malla, axes=7)
        show(malla, zoom=1.2, bg="black", viewup="z").close() 

    def volverBoton(self):
        self.__ventana_padre.show()
        self.hide()

#sacamos la información de estas fuentes:
#https://github.com/amine0110/vedo-tutorials/blob/main/visualization.py
#https://github.com/marcomusy/vedo/blob/master/examples/volumetric/app_isobrowser.py
#https://vedo.embl.es/
#https://www.youtube.com/watch?v=lPoZJFrYtL0











        