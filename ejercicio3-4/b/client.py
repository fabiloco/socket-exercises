from team import Team

# importamos el paquete de sockets
import socket, pickle

# Creamos un cliente de sockets TCP de la misma manera
# que con el servidor
# AF_INET       -> socket de internet
# SOCK_STREAM   -> socket de tipo tcp, es decir, con conexión
#                  entre el servidor y el cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos el cliente a la misma dirección a la que
# enlazamos el servidor
client.connect(("localhost", 9000))

teams = []

def startChampionship():
	print("Ingrese cuantos equipos desea inscribir")
	N_TEAMS = int(input(">_ "))
	if(N_TEAMS < 10 or N_TEAMS > 20):
		print("El número de equipos debe estar por debajo de 20 y por arriba de 10")
		return


	i = 0
	while i < N_TEAMS:
		print(f"Ingrese el nombre del equipo número: {i + 1}")
		team_name = input(">_ ")
		new_team = Team(team_name, 0)
		teams.append(new_team)
		i+=1

def sendTeamToServer():
	data_string = pickle.dumps(teams)
	client.send(data_string)

startChampionship()
sendTeamToServer()

# client.send("Hello server".encode("utf-8"))
# print(client.recv(1024).decode("utf-8"))

# client.send("Bye".encode("utf-8"))
# print(client.recv(1024).decode("utf-8"))
