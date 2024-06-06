import os
import nilearn
import pydicom
import dicom2nifti
from nilearn import plotting

class Dicom():
  def __init__(self):
    self.__nombre = None
    self.__iD = None
    self.__fecha = None
    self.__modalidad = None
    self.__descripcion = None

  def cargarArchivoDCM(self, rutaCarpeta):
    for archivo in os.listdir(rutaCarpeta):
      if archivo.endswith('.dcm'):
        self.ruta = os.path.join(rutaCarpeta,archivo)
        self.leer = pydicom.dcmread(self.ruta)
        return self.leer
      else:
        return False

  def asignarInformacion(self):
    self.__nombre = self.leer[0x0010, 0x0010].value
    self.__iD = self.leer[0x0010, 0x0020].value
    self.__fecha = self.leer[0x0008,0x0020].value
    self.__modalidad = self.leer[0x0008,0x0060].value
    self.__descripcion = self.leer[0x0008,0x1030].value

    self.lista = [self.__nombre, self.__iD, self.__fecha, self.__modalidad, self.__descripcion]
    return self.lista

  def convertirDCM(self,dicom):
    self.dicom = dicom
    existencia = os.path.exists('./nifti')
    if existencia is False:
      carpeta = os.mkdir('./nifti')
      self.carpetaNueva = os.path.dirname(carpeta)
      return self.carpetaNueva
    else:
      self.carpetaNueva = './nifti'
    self.conversion = dicom2nifti.convert_directory(self.dicom,self.carpetaNueva)

  def visualizarNifti(self):
    for archivo in os.listdir(self.carpetaNueva):
          if archivo.endswith('.nii.gz'):
            self.ruta = os.path.join(self.carpetaNueva,archivo)
            self.read = nilearn.image.load_img(self.ruta)
            self.imagen = plotting.plot_anat(self.read, display_mode = 'ortho', title = 'Planos Axial, Sagital y Coronal', colorbar = True, cmap = 'inferno')
            return self.imagen
          else:
            return False

class Imagen3D:
     pass