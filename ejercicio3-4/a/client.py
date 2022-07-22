# importamos el paquete de sockets
import socket, pickle

from prettytable import PrettyTable

# Creamos un cliente de sockets UDP de la misma manera
# que con el servidor
# AF_INET       -> socket de internet
# SOCK_DGRAM    -> socket de tipo UDP, es decir, sin conexión
#                  entre el servidor y el cliente. Se mandaran
#                  mensajes independientes
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

table = PrettyTable()
# Columnas
table.field_names = ["Nombre", "Apellido", "Definitiva"]

def show_def_notes():
	for student in students:
		def_note = float(student.note1) * student.perc1 + float(student.note2) * student.perc2 + float(student.note3) * student.perc3 + float(student.note4) * student.perc4
		table.add_row([student.name, student.lastname, def_note])

	print(table.get_string(sortby="Apellido"))

client.connect(("localhost", 9000))

encoded_message = client.recv(1024)
students = pickle.loads(encoded_message)

show_def_notes()
