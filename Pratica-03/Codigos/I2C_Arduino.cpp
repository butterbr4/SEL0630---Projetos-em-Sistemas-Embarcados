#include <Wire.h>

#define I2C_ADDRESS 0x08  // Endereço I2C do Arduino (pode ser ajustado conforme necessário)
#define POT_PIN A0        // Pino analógico conectado ao potenciômetro

void setup() {  
  Wire.begin(I2C_ADDRESS);        // Inicializa o Arduino como escravo I2C
  Wire.onRequest(requestEvent);   // Registra a função de callback para requisições
  Serial.begin(9600);             // Inicializa a comunicação serial para depuração
}

void loop() {
  // O loop pode permanecer vazio, pois a ação é tratada na função de requisição
}

void requestEvent() {
  int potValue = analogRead(POT_PIN); // Lê o valor do potenciômetro (0-1023)
  
  byte highByteValue = highByte(potValue); // Obtém o byte superior
  byte lowByteValue = lowByte(potValue);   // Obtém o byte inferior
  
  Wire.write(highByteValue); // Envia o byte superior
  Wire.write(lowByteValue);  // Envia o byte inferior
  
  // Exibe o valor no terminal serial para verificação
  Serial.print("Valor enviado: ");
  Serial.println(potValue);
}
