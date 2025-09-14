import socket
import requests
from config import API_KEY

# Configuración del servidor
HOST = "127.0.0.1" #0.0.0.0
PORT = 65432

def obtener_deportes():
    try:
        url = "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/news"
        r = requests.get(url)
        data = r.json()
        noticia = data["articles"][0]["headline"]
        return f"Última noticia deportiva: {noticia} "
    except:
        return "Error al obtener noticias deportivas."

def obtener_noticias():
    try:
        url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=1&orderby=time"
        r = requests.get(url)
        data = r.json()
        sismo = data["features"][0]["properties"]
        lugar = sismo["place"]
        magnitud = sismo["mag"]
        return f"Último terremoto: Magnitud {magnitud} en {lugar} "
    except:
        return "Error al obtener datos de terremotos."

def obtener_clima():
    try:
        ciudad = "León"
        api_key = API_KEY 
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},MX&appid={api_key}&units=metric&lang=es"
        r = requests.get(url)
        data = r.json()
        temp = data["main"]["temp"]
        clima = data["weather"][0]["description"]
        return f"Clima en {ciudad}: {clima}, {temp}°C "
    except:
        return "Error al obtener datos del clima."

# Crear socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor PNC con API escuchando en {HOST}:{PORT}...")

while True:
    conn, addr = server_socket.accept()
    print(f"Conexión establecida con {addr}")

    data = conn.recv(1024).decode().lower()
    if not data:
        break

    print(f"Categoría solicitada: {data}")

    if data == "deportes":
        respuesta = obtener_deportes()
    elif data == "noticias":
        respuesta = obtener_noticias()
    elif data == "clima":
        respuesta = obtener_clima()
    else:
        respuesta = "Categoría no reconocida. Usa: deportes, noticias o clima."

    conn.sendall(respuesta.encode())
    conn.close()
