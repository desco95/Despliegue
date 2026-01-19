import socket
import threading

HOST = "127.0.0.1" #192.168.100.43
PORT = 65432

cliente = None
conectado = False

def recibir():
    global conectado
    while conectado:
        try:
            msg = cliente.recv(1024).decode('utf-8')
            if not msg:
                break
            
            partes = msg.split('|')
            cmd = partes[0]
            
            if cmd == "AVISO":
                print(f"\n📢 {partes[1]}: {partes[2]}")
                print("> ", end="", flush=True)
            elif cmd == "UNIO":
                print(f"\n✅ {partes[1]} se unió")
                print("> ", end="", flush=True)
            elif cmd == "SALIO":
                print(f"\n❌ {partes[1]} salió")
                print("> ", end="", flush=True)
            elif cmd == "ALUMNOS":
                print(f"\n👥 Alumnos: {partes[1]}")
                print("> ", end="", flush=True)
            elif cmd == "HIST":
                print(f"   {partes[1]}")
            elif cmd == "FIN":
                print("> ", end="", flush=True)
            elif cmd == "ERROR":
                print(f"\n⚠️  {partes[1]}")
                print("> ", end="", flush=True)
        except:
            break

print("="*40)
print("📢 AVISOS DE CLASE")
print("="*40)

try:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))
    
    nombre = input("Tu nombre: ")
    cliente.send(f"UNIRSE|{nombre}".encode('utf-8'))
    
    resp = cliente.recv(1024).decode('utf-8')
    if resp.startswith("ERROR"):
        print(f"❌ {resp.split('|')[1]}")
        exit()
    
    print(f"✅ Conectado como {nombre}\n")
    conectado = True
    
    threading.Thread(target=recibir, daemon=True).start()
    
    print("Comandos:")
    print("  aviso <mensaje>  - Publicar aviso")
    print("  avisos           - Ver avisos")
    print("  alumnos          - Ver alumnos")
    print("  salir            - Salir\n")
    
    cliente.send("VER_AVISOS|".encode('utf-8'))
    
    while conectado:
        entrada = input("> ")
        
        if entrada.startswith("aviso "):
            msg = entrada[6:]
            cliente.send(f"AVISO|{msg}".encode('utf-8'))
        
        elif entrada == "avisos":
            print("\n📋 Avisos anteriores:")
            cliente.send("VER_AVISOS|".encode('utf-8'))
        
        elif entrada == "alumnos":
            cliente.send("VER_ALUMNOS|".encode('utf-8'))
        
        elif entrada == "salir":
            conectado = False
            break
        
        else:
            print("⚠️  Comando no válido")

except Exception as e:
    print(f"Error: {e}")

finally:
    if cliente:
        cliente.close()
    print("✅ Desconectado")
