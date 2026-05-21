from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import cv2
import numpy as np

class Tonalidad():
    
    """Clase que proporciona métodos para ajustar la tonalidad de las imágenes, como brillo y contraste."""
    
    def brillo(self, image, factor):
        
        """Ajusta el brillo de la imagen.
        Args:
            image (_type_): La imagen a la que se le ajustará el brillo.
            factor (_type_): El factor de ajuste del brillo, donde valores mayores a 1 aumentan el brillo y valores menores a 1 lo disminuyen.
        Returns:
            Image: La imagen con el brillo ajustado.
        """
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(factor)
    
    def contraste(self, image, factor):
        
        """Ajusta el contraste de la imagen.
        Args:
            image (_type_): La imagen a la que se le ajustará el contraste.
            factor (_type_): El factor de ajuste del contraste, donde valores mayores a 1 aumentan el contraste y valores menores a 1 lo disminuyen.
        Returns:
            Image: La imagen con el contraste ajustado.
        """
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(factor)