from socket import socket,AF_INET, SOCK_DGRAM #Importar modulos para la comunicacion de sockets
import serial, time #Importar modulo para comunicacion con puerto serial, y manejo de tiempo

#Definicion de las variables necesarias
PUERTO = "COM7"
BAUDIOS = 9600
IP = "189.223.71.122" #IP de Antonio
#IP = "201.171.13.53" #IP de Velazco

s = socket(AF_INET, SOCK_DGRAM) #Creacion del socket
arduino = serial.Serial(PUERTO, BAUDIOS) #Creación del objeto serial para la comunicacion con el arduino receptor

while(True):
    s.sendto(b"receptor:2", (IP, 443)) #Se envia confirmacion de conexion al servidor enviando el mensaje
    x = s.recv(8192) #Se guarda en x lo recibido por el socket conectado al servidor
    time.sleep(0.5)
    if(x==b'1' or x==b'0'): 
        print(x)
        arduino.write(x) #Se manda x al arduino por el puerto serie
