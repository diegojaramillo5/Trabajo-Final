from Modelo import Dicom, Imagen3D
from Vista import VentanaPrincipal
from PyQt5.QtWidgets import QApplication
import sys

class Controlador(object):
    def __init__(self, vista, dicom):
        self.__mi_vista = vista
        self.__mi_dicom = dicom
        
    def cargarDCM(self, ruta): 
        return self.__mi_dicom.cargarArchivoDCM(ruta)

    def asignarInfo(self,archivo):
        return self.__mi_dicom.asignarInformacion(archivo)
    
    def convertir(self, dicom):
        self.__mi_dicom.convertirDCM(dicom)

    def visualizarNii(self):
        return self.__mi_dicom.visualizarNifti()

class Principal(object):
    def __init__(self): 
        self.__app = QApplication(sys.argv)
        self.__mi_vista = VentanaPrincipal()
        self.__mi_dicom = Dicom()
        self.__mi_controlador = Controlador(self.__mi_vista, self.__mi_dicom)
        self.__mi_vista.asignarControlador(self.__mi_controlador)

    def main(self):
        self.__mi_vista.show()
        sys.exit(self.__app.exec_())  

p=Principal()
p.main()