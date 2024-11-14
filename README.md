# Tarea: Extracción y Visualización de Información de Logs en Formato JSON

### Objetivo: 
Aprender a identificar y manejar datos malformados obtenidos de internet, transformándolos en estructuras JSON utilizables mediante expresiones regulares y visualizando la información mediante gráficos con matplotlib.

## Descripción de la Actividad

### Búsqueda de Datos:

Busca en fuentes en línea logs o archivos de datos malformados de libre acceso. Algunos ejemplos incluyen logs de servidores web, archivos de texto de errores de aplicaciones, o registros de eventos de sistemas.
Especifica que los datos deben contener información como fechas, direcciones IP, métodos de solicitud (GET, POST), recursos solicitados y códigos de error, u otros datos relevantes dependiendo del tipo de archivo.

### Extracción de Información:

Crea un script en Python para leer y analizar el archivo malformado utilizando expresiones regulares para extraer los datos clave. Ejemplos de patrones de datos que podrías necesitar identificar:
Dirección IP: (\d{1,3}\.){3}\d{1,3}
Fecha y hora: \d{2}/\w{3}/\d{4}(:\d{2}){3}
Métodos HTTP: GET|POST|PUT|DELETE
Transforma la información extraída en un formato JSON manejable.
Guarda el JSON generado en un archivo local para su posterior análisis.

### Visualización de Datos:

Utiliza matplotlib para representar gráficamente algunos patrones de los datos obtenidos. Puedes elegir entre varias opciones, como:
Distribución de métodos de solicitud HTTP (barras o pie chart)
Frecuencia de errores por día o IP (histograma)
Accesos a recursos específicos (gráfico de líneas o barras)
Asegúrate de etiquetar adecuadamente los ejes y el título de cada gráfico para una fácil interpretación.

### Entrega:

Entregar el código Python junto con el archivo JSON generado y los gráficos de matplotlib.
Adjunta un breve informe explicando el proceso seguido, las expresiones regulares utilizadas y una interpretación de los gráficos.

### Criterios de Evaluación:

Eficiencia en la extracción de datos malformados mediante expresiones regulares.
Corrección y claridad en la estructura JSON generada.
Claridad y relevancia de los gráficos generados en matplotlib.
Calidad del informe y de la interpretación de resultados.

### Recursos Sugeridos:

Documentación de Python para manejo de expresiones regulares (re).
Tutoriales de matplotlib para visualización de datos.
Ejemplos de logs de servidores (disponibles en línea para prácticas).
