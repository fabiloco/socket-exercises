# importamos el paquete de sockets
import socket, pickle

from os import system
import sys
import threading
from time import sleep

from employee import Employee

# paquete de tablas que usaremos para almacenar y mostrar los datos
from prettytable import PrettyTable
table = PrettyTable()
# Columnas
table.field_names = ["Cédula", "Nombre", "Horas trabajadas", "Valor por horas", "Deducción de porcentaje"]

employees = [] # <- Lista en la que se guardaran los trabajadores, la que se enviara al cliente

# Creamos un seridor de sockets UDP
# que con el servidor
# AF_INET       -> socket de internet
# SOCK_DGRAM    -> socket de tipo UDP, es decir, sin conexión
#                  entre el servidor y el cliente. Se mandaran
#                  mensajes independientes
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Tenemos que vincular el servidor a una IP y un puerto
# en este caso se hara la practica de forma local,
# ejecutando el cliente y servidor en la misma maquina
server.bind(("localhost", 9000))


# Podemos usar dos métodos para recibir mensajes de un cliente
# recv      ->  este método solo devuelve el mensaje del cliente,
#               Pero no devuelve la dirección, por lo que no
#               podemos contestarle al cliente.
#
# recvfrom  ->  este método devuelve la dirección y el mensaje

def showEmployees():
	system("cls")
	print(table)
	input("\nPresione enter para volver al menu:>_ ")

def addEmployee():
	system("cls")
	print("Añadiendo un nuevo trabajador")

	cedula = input("Ingrese la cedula: ")
	nombre = input("Ingrese el nombre: ")
	horas_trabajadas = input("Ingrese la cantidad de horas trabajadas: ")
	valor_por_hora = input("Ingrese el valor por horas: ")
	deduccion_porcentaje = input("Ingrese el porcentaje de deducción: ")

	employee = Employee(cedula, nombre, horas_trabajadas, valor_por_hora, deduccion_porcentaje)

	employees.append(employee)

	table.add_row([cedula, nombre, horas_trabajadas, valor_por_hora, deduccion_porcentaje])

	print("Trabajador agregado con exito...")
	sleep(2)


def listenClients():
	print("Listening client petitions...")
	while True:
		message, address = server.recvfrom(1024)
		data_string = pickle.dumps(employees)
		server.sendto(data_string, address)

def menu():
	while True:
		system("cls")
		print("Menu")
		print("1) Agregar un trabajador")
		print("2) Mostrar los trabajadores")
		print("q) Salir del programa")
		choice = input(">_ ")
		choice = choice.strip()
		if (choice == "1"):
			addEmployee()
		if (choice == "2"):
			showEmployees()
		elif (choice == "q"):
			print("Abortando el programa...")
			server.close()
			sys.exit()
		else:
			print("Opción invalida, por favor intentelo nuevamente")


serverThread = threading.Thread(target=listenClients)
menuThread = threading.Thread(target=menu)


serverThread.start()
menuThread.start()
