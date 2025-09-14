# Despliegue

Integrantes del Equipo
Luis David Escobedo Ojeda - Melissa Valeria Leilani Quintero Fraustro

Descripción
PNX (Protocolo Noticias Express) es un sistema cliente-servidor que utiliza sockets TCP en Python. Este protocolo permite consultar información en tres categorías específicas: deportes, noticias y clima. El objetivo es facilitar el aprendizaje de protocolos de comunicación personalizados.

Categorías Disponibles
deportes: Resultados y eventos deportivos recientes
noticias: Sismos y eventos relevantes recientes
clima: Condiciones meteorológicas para León, México

Funcionamiento del Protocolo
El cliente establece conexión TCP con el servidor
Envía una solicitud con una categoría válida
El servidor procesa la petición y devuelve la información correspondiente
La conexión permanece activa para múltiples consultas
El comando "salir" finaliza la conexión


Ejemplos de Uso
Cliente: deportes
Servidor: Último partido: Club León 2 - 1 Chivas. Goles: Ángel Mena

Cliente: noticias
Servidor: Se registró un sismo de magnitud 5.8 en Guerrero, México. No se reportan daños graves

Cliente: clima
Servidor: León, México: Mayormente soleado, 28°C. Viento 10 km/h, humedad 60%

Cliente: salir
Servidor: Conexión finalizada

Objetivos de Aprendizaje
Diseño de protocolos de comunicación
Programación de sockets TCP en Python
Gestión de conexiones cliente-servidor
Procesamiento de solicitudes en tiempo real
