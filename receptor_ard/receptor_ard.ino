const int pinLED1 = 13;//Declaracion de puerto
const int pinLED0 = 2;//Declaracion de puerto
void setup() 
{
   Serial.begin(9600);
   pinMode(pinLED1, OUTPUT);//Puerto en modo salida
   pinMode(pinLED0, OUTPUT);//Puerto en modo salida
}

void loop()
{
   if (Serial.available()>0) // envía datos solo cuando los recibe:
   {
      char option = Serial.read();//Lee los datos
      //Condicional para enviar los datos a la salida
      if (option == '1'){
        digitalWrite(pinLED1, HIGH);//Enciende el puerto 13 (led verde) cuando se cumple la condicion
        digitalWrite(pinLED0, LOW);}//Apaga el puerto 2 (led rojo) cuando se cumple la condicion
      else{
        digitalWrite(pinLED1, LOW);//Apaga el puerto 13 (led verde) cuando no se cumple la condicion
        digitalWrite(pinLED0, HIGH);}//Enciende el puerto 2 (led rojo) cuando no se cumple la condicion
   }
}
