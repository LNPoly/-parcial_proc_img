## Integrantes

Juan Manuel Etchehun, Paula Domínguez, Alejandro Rodriguez

--

## Script
El script en lenguaje Python y utilizando la librería PILLOW aplica una serie de efectos modificadores en una imagen cargada previamente. Dichos efectos son: *Escala de grises*, *Brillo*, *Contraste*, *desenfoque gaussiano*, y una combinación entre escala de grises y contraste.

  * **Escala de grises:**
    Una vez cargada la imagen, esta efecto transforma la imagen en blanco y negro a través del metodo llamado 'filtro_gris' dentro de la clase 'Filtros'. Este metodo llama a Pillow quien aplica mediante la clase ImageOps, su metodo grayscale(image).

  * **Desenfoque gaussiano:**
    Este metodo que está en la clase 'Filtros' se aplica con pillow mediante el módulo ImageFilter y aplica la clase 'GaussianBlur'. El resultado es una imagen        borrosa dependiendo del radio (factor numérico) que se le brinde. Por defecto, el radio de desenfoque gaussiano esta establecido en 2.0.
  
  * **Brillo:**
    Una vez cargada la imagen la clase 'Tonalidad' aplica el metodo 'brillo' que aplica el efecto transformando la imagen (mediante un factor numérico) agregandole luz mediante valores mayores a 1 y los valores que son menores a 1 disminnuyen. Este metodo llama a Pillow para que se encargue mediante el módulo ImageEnhance con la clase Brightness utilicen el método enhance para aplicar el factor numérico de luz.

  * **Contraste:**
    Una vez cargada la imagen la clase 'Tonalidad' aplica el metodo 'contraste' con los mismos parametros que el brillo.
    
## Como usar el Script

Realizar la ejecución mediante el archivo main.py el cual mostrará un menú interactivo inicial.

<img width="656" height="289" alt="menu" src="https://github.com/user-attachments/assets/a8bb21ba-42a8-46ed-ba91-08f0ee2d3dff" />


## Carga de imagen

Para cargar la imagen, elegir la opción 1 para poder establecer la ruta de la imagen. Una vez cargada, se volverá automáticamente al menú inicial para continuar.



<img width="627" height="88" alt="selección de opcion" src="https://github.com/user-attachments/assets/d84fd832-bff0-4bc1-844b-df6dac66a06d" />


## Aplicar efectos

  - Escala de grises: Eligiendo la opcion 2, aplicamos el efecto de escala de grises sobre la imagen cargada previamente con la opcion 1 del menú.
  

<img width="627" height="88" alt="selección de opcion" src="https://github.com/user-attachments/assets/63426d84-1699-4a08-82a4-be66edcb1804" />

- Resultado: La imagen con el efecto aplicado, se guarda con un nuevo nombre en una carpeta llamada 'resultados'.

<img width="324" height="65" alt="guardado_resultado" src="https://github.com/user-attachments/assets/0c607252-2e1f-44dc-9e1e-b3108214f80d" />


  - Pregunta de confirmación: Al finalizar cada operación a excepción de la carga de imagen (**obligatoria** para el funcionamiento del script), se le pregunta al usuario si desea continuar o salir del programa.

    <img width="841" height="75" alt="pregunta_confirmacion" src="https://github.com/user-attachments/assets/f6fd3800-3115-4e19-8b44-3ac3ebe81961" />

## Salir

 - Mediante la selección de la últimaa opción del menú, el programa finaliza

 <img width="626" height="330" alt="salir" src="https://github.com/user-attachments/assets/9bc7a487-509d-47ca-9bff-370eda01be31" />

## Desiciones importantes:
  - Se tomó la decisión de realizar un menú interactivo para agregarle funcionalidad al programa y testearlo de forma segura con posibiidad de mejorarlo a futuro
  - Metodo 'match-case': Con el fin de evitar una cadena larga de IF-ELSE, se utilizó esta estructura equivalente al 'switch' en JAVA. Cada caso dentro del match      responde a una función específica que se elige en el menu interactivo. 
