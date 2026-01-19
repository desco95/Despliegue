import socket
import threading

HOST = "127.0.0.1" #0.0.0.0
PORT = 65432

alumnos = {}  # {nombre: socket}
avisos = []  # Lista de avisos

def manejar_alumno(conn, addr):
    nombre = None
    print(f"Conexión desde {addr}")
    
    try:
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            
            partes = data.split('|')
            comando = partes[0]
            
            if comando == "UNIRSE":
                nombre = partes[1]
                if nombre in alumnos:
                    conn.send("ERROR|Nombre ya existe".encode('utf-8'))
                    break
                alumnos[nombre] = conn
                conn.send("OK|Conectado".encode('utf-8'))
                print(f"✅ {nombre} se unió")
                
                # Avisar a otros
                for n, s in alumnos.items():
                    if n != nombre:
                        try:
                            s.send(f"UNIO|{nombre}".encode('utf-8'))
                        except:
                            pass
            
            elif comando == "AVISO":
                mensaje = partes[1]
                avisos.append(f"{nombre}: {mensaje}")
                if len(avisos) > 20:
                    avisos.pop(0)
                
                # Enviar a todos menos al remitente
                for n, s in alumnos.items():
                    if n != nombre:
                        try:
                            s.send(f"AVISO|{nombre}|{mensaje}".encode('utf-8'))
                        except:
                            pass
                conn.send("OK|Enviado".encode('utf-8'))
                print(f"📢 {nombre}: {mensaje}")
            
            elif comando == "VER_AVISOS":
                for aviso in avisos:
                    conn.send(f"HIST|{aviso}".encode('utf-8'))
                conn.send("FIN|".encode('utf-8'))
            
            elif comando == "VER_ALUMNOS":
                lista = ",".join(alumnos.keys())
                conn.send(f"ALUMNOS|{lista}".encode('utf-8'))
    
    except:
        pass
    
    finally:
        if nombre and nombre in alumnos:
            del alumnos[nombre]
            print(f"❌ {nombre} salió")
            for s in alumnos.values():
                try:
                    s.send(f"SALIO|{nombre}".encode('utf-8'))
                except:
                    pass
        conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print("="*40)
print("📢 SERVIDOR DE AVISOS DE CLASE")
print("="*40)
print(f"Escuchando en {HOST}:{PORT}\n")

while True:
    conn, addr = server.accept()
    threading.Thread(target=manejar_alumno, args=(conn, addr), daemon=True).start()
