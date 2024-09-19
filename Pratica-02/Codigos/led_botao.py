import RPi.GPIO as GPIO
import time

# Configurar a biblioteca RPi.GPIO para usar o esquema de numeração BCM
GPIO.setmode(GPIO.BCM)

# Definir os pinos GPIO para o LED e o botão
LED_PIN = 16
BUTTON_PIN = 24

# Configurar o pino do LED como saída e o pino do botão como entrada com pull-down resistor
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Verificar se o botão está pressionado
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            GPIO.output(LED_PIN, GPIO.HIGH)  # Acender o LED
        else:
            GPIO.output(LED_PIN, GPIO.LOW)  # Apagar o LED
        time.sleep(0.1)  # Pequeno atraso para evitar alta carga de CPU

except KeyboardInterrupt:
    pass  # Permitir que o usuário interrompa o programa com Ctrl+C

finally:
    # Limpar os pinos GPIO ao sair
    GPIO.cleanup()
