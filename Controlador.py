from Modelo import Dicom, Imagen3D
from Vista import VentanaPrincipal, VentanaRutaDCM
from PyQt5.QtWidgets import QApplication
import sys

class Controlador(object):
    def __init__(self, vista, vistaRuta, dicom, imagen3D):
        self.__mi_vista = vista
        self.__mi_vistaRuta = vistaRuta
        self.__mi_dicom = dicom
        self.__mi_imagen3D = imagen3D
        
    def cargarDCM(self, ruta): 
        return self.__mi_dicom.cargarArchivoDCM(ruta)

    def asignarInfo(self,archivo):
        return self.__mi_dicom.asignarInformacion(archivo)
    
    def convertir(self, dicom):
        self.__mi_dicom.convertirDCM(dicom)

    def visualizarNii(self):
        return self.__mi_dicom.visualizarNifti()

class Coordinador(object):
    def __init__(self, usuario, contrasena):
        self.__mi_usuario = usuario
        self.__mi_contrasena = contrasena

# validar usuario

def main():
    app = QApplication(sys.argv)
    vista = VentanaPrincipal()
    vistaRuta = VentanaRutaDCM()
    dicom = Dicom()
    imagen = Imagen3D()
    controlador = Controlador(vista, vistaRuta, dicom, imagen)
    vista.asignarControlador(controlador)
    vistaRuta.asignarControlador(controlador)
    vista.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()