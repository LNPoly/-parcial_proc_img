from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import cv2
import numpy as np
from tonalidad import Tonalidad
from filtros import Filtros


class Menu():
    """Clase que proporciona un menú interactivo.
    Args:        editor (Editor): Una instancia de la clase Editor que se utilizará para aplicar los filtros y ajustes de tonalidad a las imágenes.  
    Returns:        Ninguno.
    """
        
    def __init__(self, editor):
        
        """Inicializa la clase Menu con una instancia de Editor.
        Args:
            editor (Editor): Una instancia de la clase Editor que se utilizará para aplicar los filtros y ajustes de tonalidad a las imágenes.  
        returns: Ninguno.
        """
        self.editor = editor
        
    def mostrar_menu(self) -> str:
        """Muestra el menú de opciones al usuario y solicita la selección de una opción.
        
        Args:
            Ninguno.
        Returns: 
            La opción seleccionada por el usuario como una cadena.
        """
        
        print("""
              Bienvenido al editor de imágenes"
                "Seleccione una opción:\n"
                "1. Cargar imagen"
                "2. Aplicar filtro de escala de grises"
                "3. Aplicar filtro de desenfoque"
                "4. Ajustar brillo"
                "5. Ajustar contraste"
                "6. Combinar (gris + contraste)"
                "7. Salir""")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        return self.ejecutar_opcion(opcion)

    def ejecutar_opcion(self, opcion)-> int:  
         
        """Ejecuta la opción seleccionada por el usuario.

        Args:
            opcion (str): La opción seleccionada por el usuario, que debe ser un número del 1 al 7.
        Returns:
            int: El código de la opción seleccionada.
            
        """
        
        # Se utiliza en este caso una estructura match-case para manejar las diferentes opciones seleccionadas por el usuario y asi evitar una cadena larga de IF-ELSE. Cada caso corresponde a una opción del menú y ejecuta la acción correspondiente, como aplicar un filtro o ajustar la tonalidad de la imagen. Después de ejecutar la acción, se llama al método confirmacion() para preguntar al usuario si desea realizar otra operación o salir del programa.
        
        match opcion:
            
            case "1":
                
                editor = self.editor(input("Ingrese la ruta de la imagen a editar: ").strip().lower())
                print("Imagen cargada exitosamente.")
                self.editor = editor.mostrar_menu()
                    
            case "2":
                
                filtro_gris = Filtros().filtro_gris(self._image)
                self.procesamiento_img = filtro_gris
                
                self.guardar("./resultados/imagen_grises.jpg")
                print("Filtro de escala de grises aplicado y guardado como 'imagen_grises.jpg'")
                self.confirmacion()
                
            case "3":
                
                entrada = input("Introduce el radio de desenfoque (ej. 2 o 5.5): ")
                radio = float(entrada)
                
                filtro_blur = Filtros().blur_gaussiano(self._image, radius=radio)
                self.procesamiento_img = filtro_blur
                
                self.guardar("./resultados/imagen_blurGaussinno.jpg")
                print(f"Filtro de desenfoque aplicado con radio {radio} y guardado como 'imagen_blurGaussinno.jpg'")
                self.confirmacion()                    
                
            case "4":
                
                brillo = Tonalidad().brillo(self._image, factor=1.5)
                self.procesamiento_img = brillo
                
                self.guardar("./resultados/imagen_brillo.jpg")
                print("Brillo ajustado y guardado como 'imagen_brillo.jpg'")
                self.confirmacion()
                
            case "5":
                
                contraste = Tonalidad().contraste(self._image, factor=1.5)
                self.procesamiento_img = contraste
                
                self.guardar("./resultados/imagen_contraste.jpg")
                print("Contraste ajustado y guardado como 'imagen_contraste.jpg'") 
                self.confirmacion()

            case "6":
                
                if not self.procesamiento_img:
                    
                    print("Primero debes aplicar un filtro de escala de grises o desenfoque para combinarlo.")
                    self.confirmacion()
                    
                else:
                    
                    imagen_gris = Image.open("./resultados/imagen_grises.jpg").copy()
                    imagen_contraste = Image.open("./resultados/imagen_contraste.jpg").copy()
                
                    imagen_combinada = Tonalidad().contraste(imagen_gris, factor=1.5)             
                    self.procesamiento_img = imagen_combinada
                    
                    self.guardar("./resultados/imagen_combinada_gris_contraste.jpg")
                    print("Imágenes combinadas y guardadas como 'imagen_combinada_gris_contraste.jpg'")
                    self.confirmacion()
                
            case "7":
                
                print("Saliendo del programa...")
                exit()

            case default:
                
                print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
                self.mostrar_menu()
                
    def confirmacion(self):
        """Permite al usuario decidir si desea realizar otra operación o salir del programa después de ejecutar una acción. Si el usuario elige realizar otra operación, se muestra nuevamente el menú. Si elige salir, el programa termina.
        
        Args: Ninguno.
        Returns: Ninguno.
        """
        #Se utilizó un bloque try-except para manejar posibles errores en la entrada del usuario y asegurar que el programa no se caiga debido a entradas no válidas. Si el usuario ingresa algo diferente a 's' o 'n', se le pedirá que ingrese una opción válida.
        
        try:
            confirmacion = input("¿Desea realizar otra operación? (s/n): ").strip().lower()
            
            if confirmacion == "s":
                
                self.mostrar_menu()
                
            elif confirmacion == "n":
                
                print("Saliendo del programa...")
                exit()
                
            else:
                
                print("Entrada no válida. Por favor, ingrese 's' para sí o 'n' para no.")
                self.confirmacion()
                
        except Exception as e:
            
            print(f"Ocurrió un error: {e}")
            self.confirmacion()
            