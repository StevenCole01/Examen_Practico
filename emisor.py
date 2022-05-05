from socket import socket,AF_INET, SOCK_DGRAM #Importar modulos para la comunicacion
import time #Importar modulo para el manejo de tiempo
import serial #Importar modulo para comunicacion con puerto serial

#Definicion de las variables necesarias
PUERTO = "COM7"
BAUDIOS = 9600
IP = "189.223.71.122" #IP de Antonio
#IP = "201.171.13.53" #IP de Velazco


s = socket(AF_INET,SOCK_DGRAM) #Creacion del socket
serialArduino = serial.Serial(PUERTO, BAUDIOS) #Creación del objeto serial para la comunicacion con el puerto
time.sleep(1) #Tiempo de retardo
cad = ""
while True:
    cad = int(serialArduino.readline().decode("ascii"))#Lectrura y conversion de lo recivido por el puerto serieo
    print(cad) #Imprime lo recibido por el puerto serie, "1" o "0"
    if cad == 1:
        s.sendto(b"emisor:1", (IP, 443)) #Se envia un uno al servidor
    if cad == 0:
        s.sendto(b"emisor:0", (IP, 443)) #Se envia un cero al servidor