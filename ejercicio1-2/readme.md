# Punto 1 - 2

## intrucciones para ejecutar el ejercicio
- Instalar las dependencias con el siguiente comando:
```
	python -m pip install -U prettytable
```
- Ejecutar el servidor con el siguiente comando:
```
	python server.py
```
- Una vez el servidor este iniciado y este escuchando solicitudes, debe agregar empleados con el menu del servidor
- Cuando cuente con la cantidad de empleados deseada, ponga en escucha el programa Wireshark en modo "adaptar for loopback traffic" e inmediatamente ejecute el cliente con el siguiente comando:
```
	python client.py
```
- Una vez mostrada la tabla de los empleados, puede detener la captura de Wireshark para analizar las tramas.
