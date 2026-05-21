from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import cv2
import numpy as np


class Filtros():
    
    """Clase que proporciona métodos para aplicar diferentes filtros a las imágenes, como escala de grises y desenfoque."""
    
    def filtro_gris(self, image):
        
        """Aplica un filtro de escala de grises a la imagen.
        Args:
            image (_type_): La imagen a la que se le aplicará el filtro.
        Returns:
            _type_: La imagen con el filtro de escala de grises aplicado.
        """
        return ImageOps.grayscale(image)

    def blur_gaussiano(self, image, radius: float = 2.0):
        
        """Aplica un filtro de desenfoque gaussiano a la imagen.
        Args:
            image (_type_): La imagen a la que se le aplicará el filtro.
            radius (float, optional): El radio del desenfoque, por default 2.0.
        Returns:
            _type_: La imagen con el filtro de desenfoque aplicado.
        """
        return image.filter(ImageFilter.GaussianBlur(radius=radius))

