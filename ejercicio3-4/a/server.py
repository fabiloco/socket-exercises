# importamos el paquete de sockets
import socket, pickle

from os import system
import sys
import threading
from time import sleep

from student import Student

# paquete de tablas que usaremos para almacenar y mostrar los datos
from prettytable import PrettyTable
table = PrettyTable()
# Columnas
table.field_names = ["Cédula", "Nombre", "Apellido", "Nota 1", "Nota 2", "Nota 3", "Nota 4"]

students = [] # <- Lista en la que se guardaran los estudiantes, la que se enviara al cliente

# Creamos un seridor de sockets UDP
# que con el servidor
# AF_INET       -> socket de internet
# SOCK_DGRAM    -> socket de tipo UDP, es decir, sin conexión
#                  entre el servidor y el cliente. Se mandaran
#                  mensajes independientes
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tenemos que vincular el servidor a una IP y un puerto
# en este caso se hara la practica de forma local,
# ejecutando el cliente y servidor en la misma maquina
server.bind(("localhost", 9000))

server.listen()

def show_students():
	system("cls")
	print(table.get_string(sortby="Apellido"))
	input("\nPresione enter para volver al menu:>_ ")

def add_student():
	system("cls")
	print("Añadiendo un nuevo estudiante")

	cedula = input("Ingrese la cedula: ")
	nombre = input("Ingrese el nombre: ")
	apellido = input("Ingrese el apellido: ")
	nota1 = input("Ingrese a nota 1: ")
	nota2 = input("Ingrese a nota 2: ")
	nota3 = input("Ingrese a nota 3: ")
	nota4 = input("Ingrese a nota 4: ")

	student = Student(cedula, nombre, apellido, nota1, nota2, nota3, nota4)

	students.append(student)

	table.add_row([cedula, nombre, apellido, nota1, nota2, nota3, nota4])

	print("Estudiante agregado con exito...")
	sleep(2)

def show_def_notes():
	note_tables = PrettyTable()
	note_tables.field_names = ["Nombre", "Apellido", "Definitiva"]

	for student in students:
		def_note = float(student.note1) * student.perc1 + float(student.note2) * student.perc2 + float(student.note3) * student.perc3 + float(student.note4) * student.perc4
		note_tables.add_row([student.name, student.lastname, def_note])

	print(note_tables.get_string(sortby="Apellido"))
	input("\nPresione enter para volver al menu:>_ ")

def listen_clients():
	print("Listening client petitions...")
	while True:
		client, address = server.accept()
		data_string = pickle.dumps(students)
		client.send(data_string)

def menu():
	while True:
		system("cls")
		print("Menu")
		print("1) Agregar un estudiante")
		print("2) Mostrar los estudiantes ordenados por apellido")
		print("3) Mostrar definitiva de cada estudiante")
		print("q) Salir del programa")
		choice = input(">_ ")
		choice = choice.strip()
		if (choice == "1"):
			add_student()
		if (choice == "2"):
			show_students()
		if (choice == "3"):
			show_def_notes()
		elif (choice == "q"):
			print("Abortando el programa...")
			server.close()
			sys.exit()
		else:
			print("Opción invalida, por favor intentelo nuevamente")


serverThread = threading.Thread(target=listen_clients)
menuThread = threading.Thread(target=menu)


serverThread.start()
menuThread.start()
