from time import sleep

import random

# importamos el paquete de sockets
import socket, pickle

# Creamos un servidor de sockets TCP
# AF_INET       -> socket de internet - tipo de direccion
# SOCK_STREAM   -> socket de tipo tcp, es decir, con conexión
#                  entre el servidor y el cliente

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tenemos que vincular el servidor a una IP y un puerto
# en este caso se hara la practica de forma local,
# ejecutando el cliente y servidor en la misma maquina
server.bind(("localhost", 9000))

# Ponemos el servidor en escucha de nuevas solicitudes
server.listen()



def print_teams(teams):
	for team in teams:
		print(f"Team name: {team.name} - score: {team.score}")

def fill_teams_with_random_scores(teams):
	for team in teams:
		team.score = random.randint(1, 10)
	return teams

def divide_teams(teams):
	random.shuffle(teams)
	group1 = teams[:int(len(teams) / 2)]
	group2 = teams[int(len(teams) / 2):]
	return (group1, group2)

def second_fase(teams):
	return sorted(teams, reverse=True, key=lambda x: x.score)[0:2]

def third_fase(teams):
	return sorted(teams, reverse=True, key=lambda x: x.score)[0:1]

def final(team1, team2):
	if team1.score > team2.score:
		return team1
	else:
		return team2

while True:
	teams = []

	print("Esperando que los equipos se inscriban..")
	client, address = server.accept()
	print("Cliente recibido! Esperando inscripción de equipos...")

	teams = pickle.loads(client.recv(1024))
	print("Equipos recibidos!")

	teams = fill_teams_with_random_scores(teams)

	(group1_fase1, group2_fase1) = divide_teams(teams)
	group1_fase2 = second_fase(group1_fase1)
	group2_fase2 = second_fase(group2_fase1)

	group1_fase2 = fill_teams_with_random_scores(group1_fase2)
	group2_fase2 = fill_teams_with_random_scores(group2_fase2)

	group1_fase3 = third_fase(group1_fase2)
	group2_fase3 = third_fase(group2_fase2)

	group1_fase3 = fill_teams_with_random_scores(group1_fase3)
	group2_fase3 = fill_teams_with_random_scores(group2_fase3)

	champion = final(group1_fase3[0], group2_fase3[0])

	print("Calculando ganador...")
	sleep(2)

	print(f"El equipo ganador del torneo es {champion.name}!")

	client.send(champion.name.encode("utf-8"))

	# Si queremos dejar de recibir mensajes en TCP, debemos
	# cerrar la conexión explicitamente
	client.close()
