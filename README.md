Sistema de Avisos de Clase

Integrantes del Equipo 
Luis David Escobedo Ojeda - 
Melissa Valeria Leilani Quintero Fraustro -> https://github.com/valeria-quintero/Aplicaci-n-cliente-servidor-de-mensajes

Descripción
Sistema simple de avisos para alumnos usando sockets TCP. Permite publicar y consultar avisos de clase en tiempo real mediante una arquitectura cliente-servidor con conexión persistente.


Características
Publicar avisos visibles para todos los alumnos
Consultar avisos anteriores (últimos 20)
Ver alumnos conectados
Notificaciones cuando un alumno entra o sale del sistema


Protocolo de Comunicación

Formato general:
COMANDO|PARÁMETRO1|PARÁMETRO2

Cliente → Servidor
| Comando     | Formato          | Descripción                 |
| ----------- | ---------------- | --------------------------- |
| UNIRSE      | `UNIRSE\|nombre` | Conectarse al sistema       |
| AVISO       | `AVISO\|mensaje` | Publicar un aviso           |
| VER_AVISOS  | `VER_AVISOS\|`   | Consultar avisos anteriores |
| VER_ALUMNOS | `VER_ALUMNOS\|`  | Ver alumnos conectados      |

| Comando | Formato                  | Descripción         |
| ------- | ------------------------ | ------------------- |
| OK      | `OK\|mensaje`            | Operación exitosa   |
| ERROR   | `ERROR\|mensaje`         | Error               |
| AVISO   | `AVISO\|alumno\|mensaje` | Aviso recibido      |
| HIST    | `HIST\|mensaje`          | Aviso del historial |
| FIN     | `FIN\|`                  | Fin del historial   |
| ALUMNOS | `ALUMNOS\|lista`         | Lista de alumnos    |
| UNIO    | `UNIO\|nombre`           | Alumno conectado    |
| SALIO   | `SALIO\|nombre`          | Alumno desconectado |



Uso
Servidor
python servidor_corregido.py
Cliente
python cliente_corregido.py


Ejemplo:
Tu nombre: Ana
✅ Conectado como Ana
Comandos:
  aviso <mensaje>  - Publicar aviso
  avisos           - Ver avisos
  alumnos          - Ver alumnos
  salir            - Salir

Ejemplos de Comunicación
Publicar Aviso
Cliente: AVISO|Mañana hay examen
Servidor → Otros: AVISO|Ana|Mañana hay examen

Ver Avisos
Cliente: VER_AVISOS|
Servidor: HIST|Ana: Mañana hay examen
Servidor: HIST|Carlos: Estudien sockets
Servidor: FIN|

Ver Alumnos
Cliente: VER_ALUMNOS|
Servidor: ALUMNOS|Ana,Carlos,María


Objetivos
Uso de sockets TCP en Python
Implementación de protocolo de comunicación personalizado
Manejo de múltiples clientes mediante threading
Comunicación cliente-servidor en tiempo real
