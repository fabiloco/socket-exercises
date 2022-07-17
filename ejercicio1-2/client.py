# importamos el paquete de sockets
import socket

# Creamos un cliente de sockets UDP de la misma manera
# que con el servidor
# AF_INET       -> socket de internet
# SOCK_DGRAM    -> socket de tipo UDP, es decir, sin conexión
#                  entre el servidor y el cliente. Se mandaran
#                  mensajes independientes
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Hello server".encode("utf-8"), ("localhost", 9000))
print(client.recvfrom(1024)[0].decode("utf-8"))
