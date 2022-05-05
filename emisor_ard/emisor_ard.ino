int PULSADOR = 2; // Pin de entrada del pulsador
int estado = LOW; 

void setup(){
  Serial.begin(9600); //Apertura de la comunicacion serial
  pinMode(PULSADOR,INPUT);//Declaracion variable como entrada 
}

void loop(){
  while(digitalRead(PULSADOR)==LOW); // Mientras no se presione: apagado. Esperamos a que cambie su estado para salir del while.
  delay(20); //Delay para evitar rebote
  estado = !estado;// Envia el estado del LED pero contrario, encendido = LOW, apagado=HIGH.
  Serial.println(!estado); 
  while(digitalRead(PULSADOR)==HIGH);// Mientras  el pulsador esta presionado esperamos a que cambie su estado para salir del while.
  delay(20); //Delay para evitar rebote
}
