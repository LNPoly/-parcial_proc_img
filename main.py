from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import cv2
import numpy as np
from tonalidad import Tonalidad
from filtros import Filtros
from menu import Menu

class Pipeline:
    
    """Clase base para la edición de imágenes, que maneja la carga y guardado de imágenes procesadas."""
    
    def __init__(self, url:str):
        
        """Inicializa la clase Pipeline con la ruta de la imagen a editar.

        Args:
            url (str): La ruta de la imagen que se desea editar.
            
            La imagen se carga utilizando la biblioteca PIL y se almacena en el atributo _image. El atributo procesamiento_img se inicializa como None y se utilizará para almacenar la imagen después de aplicar los filtros o ajustes de tonalidad.
        """
        
        self._url = url
        self._image = Image.open(url)
        self.procesamiento_img = None
        
        
    def guardar(self, output_path):
        
        """Guarda la imagen procesada en la ruta especificada.
        Args:
            output_path (str): La ruta donde se desea guardar la imagen procesada.
            
            Si el atributo procesamiento_img contiene una imagen procesada, esta se guarda en la ruta especificada. Si no hay una imagen para guardar, se muestra un mensaje indicando que no hay imagen para guardar.
            
        returns: Ninguno.
        
        """
        if self.procesamiento_img:
            self.procesamiento_img.save(output_path)
        else:
            print("No hay imagen para guardar.")
            
class Editor(Pipeline, Filtros, Tonalidad, Menu):
    """Clase que hereda de Pipeline y permite aplicar filtros y ajustes de tonalidad a las imágenes. A partir de esta clase, se pueden aplicar los métodos definidos en las clases filtros y Tonalidad para modificar la imagen cargada."""
    pass

inicio = Editor(Menu(Editor).mostrar_menu())
