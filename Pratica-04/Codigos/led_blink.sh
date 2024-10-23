#!/bin/python

import RPi.GPIO as GPIO
import time

# Configurar o modo da pinagem
GPIO.setmode(GPIO.BCM)

# Definir o pino 18 como saída
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # Ligar o LED
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ligado")
        time.sleep(1)  # Aguarda 1 segundo
        
        # Desligar o LED
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED desligado")
        time.sleep(1)  # Aguarda 1 segundo

# Quando interromper o programa (Ctrl+C), limpar os recursos
except KeyboardInterrupt:
    print("Programa interrompido")

finally:
    # Resetar a configuração dos pinos GPIO
    GPIO.cleanup()

