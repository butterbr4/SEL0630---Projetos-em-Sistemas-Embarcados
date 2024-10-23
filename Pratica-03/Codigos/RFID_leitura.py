from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

# Desabilitar os avisos
GPIO.setwarnings(False)
# Configurar a numeração dos pinos para seguir a numeração física
GPIO.setmode(GPIO.BOARD)
# Configurar os pinos dos LEDs
LED_VERDE = 16  # Pino do LED verde
LED_VERMELHO = 18  # Pino para o LED vermelho
GPIO.setup(LED_VERDE, GPIO.OUT)
GPIO.setup(LED_VERMELHO, GPIO.OUT)

# Lista de IDs cadastrados
ids_cadastrados = {"SEL097/0097"}  # IDs cadastrados

# Cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca
leitor = SimpleMFRC522()
print("Aproxime a tag do leitor para leitura.")

try:
    while True:  # Loop infinito
        # Lê o ID e o texto da tag RFID
        id, texto = leitor.read()
        print("ID: {}\nTexto: {}".format(id, texto))  # Exibe as informações coletadas

        # Verifica se o ID está cadastrado
        if id in ids_cadastrados:
            GPIO.output(LED_VERDE, GPIO.HIGH)  # Acende o LED verde
            GPIO.output(LED_VERMELHO, GPIO.LOW)  # Apaga o LED vermelho
            print("Tag cadastrada!")
        else:
            GPIO.output(LED_VERMELHO, GPIO.HIGH)  # Acende o LED vermelho
            GPIO.output(LED_VERDE, GPIO.LOW)  # Apaga o LED verde
            print("Tag não cadastrada!")

        sleep(3)  # Aguarda 3 segundos para nova leitura

finally:
    GPIO.cleanup()  # Limpa a configuração dos GPIOs ao terminar
