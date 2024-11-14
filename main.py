# Por Geoffrey Struss

import re
import json
import matplotlib.pyplot as plt
from collections import Counter

# Expresión regular completa para capturar la IP, la fecha y la hora, y otros datos
pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[([^\]]+)\] "([A-Z]+) ([^\s]+) HTTP\/[0-9\.]+" (\d{3}) (\d+) "(.*?)" "(.*?)"'

# Abre el archivo de logs
with open('apache_logs.txt', 'r') as lines:
    jsonExtract = []
    methods = []  # Lista para almacenar los métodos HTTP
    resources = []  # Lista para almacenar los recursos solicitados

    for line in lines:
        # Busca todas las coincidencias en cada línea
        values = re.finditer(pattern, line)

        for match in values:
            # Crea un diccionario con los datos extraídos de cada línea
            jsonData = {
                "IP": match.group(1),
                "Date": match.group(2),
                "Method": match.group(3),
                "Resource": match.group(4),
                "StatusCode": match.group(5),
                "Size": match.group(6),
                "Referrer": match.group(7),
                "UserAgent": match.group(8)
            }
            # Agrega el diccionario al arreglo de resultados
            jsonExtract.append(jsonData)
            methods.append(match.group(3))  # Agrega el método HTTP
            resources.append(match.group(4))  # Agrega el recurso solicitado

    # Guardamos el JSON generado en un archivo
    with open('logs_output.json', 'w') as json_file:
        json.dump(jsonExtract, json_file, indent=4)

    print("Archivo JSON guardado como 'logs_output.json'")

# Análisis y visualización con matplotlib

# Gráfico de Accesos a Recursos Específicos (Bar Chart)
resource_counts = Counter(resources)  # Contamos las ocurrencias de cada recurso
top_resources = resource_counts.most_common(10)  # Obtenemos los 10 recursos más solicitados

# Dividimos los recursos y las cantidades para el gráfico
resources_labels = [item[0] for item in top_resources]
access_counts = [item[1] for item in top_resources]

# Creamos el gráfico de barras
plt.figure(figsize=(10, 6))
plt.barh(resources_labels, access_counts, color='#ff7f0e')
plt.xlabel('Cantidad de Accesos')
plt.ylabel('Recurso')
plt.title('Accesos a los 10 Recursos Más Solicitados')
plt.gca().invert_yaxis()  # Invertimos el eje Y para mostrar el más solicitado en la parte superior
plt.show()