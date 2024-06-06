from Modelo import Dicom, Imagen3D
from Vista import VentanaPrincipal
from PyQt5.QtWidgets import QApplication
import sys

class Controlador(object):
    def __init__(self, vista, dicom, imagen3D):
        self.vista = vista  
        self.dicom = dicom
        self.imagen3D = imagen3D
        
    def cargarArchivoDicom(self, data):
        self.dicom.cargar_archivo_dcm(data)
        
class Coordinador(object):
    def __init__(self, vista, imagen):
        self.__mi_vista = vista  
        self.__mi_imagen = imagen 
        
    def recibirDatosImg(self,img):
        self.__mi_imagen.asignarDatos(img)
        return self.__mi_imagen.verDatos()
    
def main():
    app = QApplication(sys.argv)  
    vista = VentanaPrincipal() 
    dicom = Dicom()
    imagen = Imagen3D()
    controlador = Controlador(vista, dicom, imagen)  
    vista.asignarControlador(controlador)
    vista.show()
    sys.exit(app.exec_())   

if __name__ == '__main__':
    main()