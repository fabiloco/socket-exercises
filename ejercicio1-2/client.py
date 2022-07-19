# importamos el paquete de sockets
import socket, pickle

from prettytable import PrettyTable

# Creamos un cliente de sockets UDP de la misma manera
# que con el servidor
# AF_INET       -> socket de internet
# SOCK_DGRAM    -> socket de tipo UDP, es decir, sin conexión
#                  entre el servidor y el cliente. Se mandaran
#                  mensajes independientes
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

table = PrettyTable()
# Columnas
table.field_names = ["Cédula", "Nombre", "Horas trabajadas", "Valor por horas", "Deducción de porcentaje"]


client.sendto("Hello server".encode("utf-8"), ("localhost", 9000))

(encoded_message, address )= client.recvfrom(2048)
employees = pickle.loads(encoded_message)

for employee in employees:
	table.add_row([employee.id, employee.name, employee.hours_worked, employee.val_per_hour, employee.deduction_per])

print(table)
