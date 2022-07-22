import pickle
import random
import time

# Libreria para extraer datos del teclado
# Se importan todas las librerias de sockets
from socket import *


def candidatas_apellido(candidatas):
    candidatas.sort(key=lambda candidata: candidata['Apellidos'])
    return candidatas


def candidatas_medidas_perfectas(candidatas):
    medidas_perfectas = [
        candidata for candidata in candidatas
        if candidata['Medida del busto'] == 90 and candidata['Medida de la cintura'] == 60
           and candidata['Medida de la cadera'] == 90
    ]
    if medidas_perfectas:
        return medidas_perfectas
    else:
        return 'No hay candidatas con medidas perfectas'


def candidatas_ojos_azules(candidatas):
    ojos_azules = [
        candidata for candidata in candidatas
        if candidata['Color de ojos'] == 'azul'
    ]
    if ojos_azules:
        return ojos_azules
    else:
        return 'No hay candidatas con ojos azules'


def candidatas_estatura_descendente(candidatas):
    candidatas.sort(key=lambda candidata: candidata['Estatura'], reverse=True)
    return candidatas


def send_message(socket, message, end=False):
    socket.send(pickle.dumps(
        {"message": message, "end": end}
    ) )


serverPort = 6000
# Se instancia el servidor TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
# Se define el puerto del servidor
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print("El servidor está listo para recibir peticiones: ")
while 1:
    # Se extrae la información del puerto y la dirección ip del servidor
    conSocket, addr = serverSocket.accept()
    print("Recibiendo mensajes desde el cliente", addr)
    # Obtiene la información extraida del cliente
    msg = conSocket.recv(4096)
    n = pickle.loads(msg)
    print("\nMensaje recibido: ", n)
    match n['option']:

        case 1:
            send_message(conSocket, candidatas_apellido(n['data']))
        case 2:
            send_message(conSocket, candidatas_medidas_perfectas(n['data']))
        case 3:
            send_message(conSocket, candidatas_ojos_azules(n['data']))
        case 4:
            send_message(conSocket, candidatas_estatura_descendente(n['data']))
        case 5:
            send_message(conSocket, 'Bye, bye!', True)
        case _:
            send_message(conSocket, 'Option no valida!')