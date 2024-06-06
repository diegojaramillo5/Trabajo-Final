import matplotlib.pyplot as plt
import cv2
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut

class Dicom:
  def __init__(self):
        self.__dataset = None
        self.__imagen = None
        self.__nombre = ""
        self.__id = ""
        self.__fechaNacimiento = ""
        self.__genero = ""
        self.__edad = ""
        self.__infoPaciente = None

  def asignarDataset(self, archivo):
        self.__dataset = archivo

  def cargar_archivo_dcm(self, nombre):
        self.__dataset = pydicom.dcmread(nombre+".dcm")
        self.__imagen = apply_voi_lut(self.__dataset.pixel_array, self.__dataset)
        return self.__dataset,self.__imagen

  def cargar_imagen_dcm(self):
        self.__imagen = self.__dataset.pixel_array
        
  def asignarInformacion(self):
        data_elements = ["PatientName", "PatientID","PatientBirthDate", "PatientSex", "PatientAge"]
        datos = []
        for i in data_elements:
          dato = self.__dataset.data_element(i).value
          datos.append(dato)
        self.__nombre = datos[0]
        self.__id = datos[1]
        self.__fechaNacimiento = datos[2]
        self.__genero = datos[3]
        self.__edad = datos[4]

  def asignarInfoPaciente(self):
        self.__infoPaciente = [self.__nombre, self.__id, self.__fechaNacimiento, self.__genero, self.__edad]

  def verDataset(self):
        print(self.__dataset)

  # def verImagen(self):
  #       return plt.imshow(self.__imagen, cmap='gray', vmin=0, vmax=255)
  
  def verInformacion(self):
        a = self.__infoPaciente
        print("La información encontrada sobre la imagen fue: ")
        print(f"Nombre del paciente: {a[0]}")
        print(f"ID del paciente: {a[1]}")
        print(f"Fecha de nacimineto del paciente: {a[2]}")
        print(f"Género del paciente: {a[3]}")
        print(f"Edad del paciente: {a[4]}")

  def anonimizar_dcm(self, url_anonimo):
      dataset = self.__dataset
      datos_sensibles = ["PatientName","PatientID", "PatientBirthDate","PatientSex"]
      for i in datos_sensibles:
        dataset.data_element(i).value="N/A"
      return pydicom.dcmwrite(url_anonimo,dataset)

class Imagen3D:
     pass
