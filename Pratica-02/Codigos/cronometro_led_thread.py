import RPi.GPIO as GPIO
import time
import threading

# Configuração dos pinos GPIO
LED_PIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def blink_led():
    """Função para fazer o LED piscar continuamente."""
    while not stop_event.is_set():
        GPIO.output(LED_PIN, GPIO.HIGH)  # Acende o LED
        time.sleep(0.5)  # LED fica aceso por 0.5 segundos
        GPIO.output(LED_PIN, GPIO.LOW)   # Apaga o LED
        time.sleep(0.5)  # LED fica apagado por 0.5 segundos

def countdown_timer(seconds):
    """Função para realizar a contagem regressiva."""
    while seconds:
        # Usando divmod para converter segundos em minutos e segundos
        minutes, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(minutes, secs)
        print(time_format, end='\r')  # Imprime o tempo formatado na mesma linha
        time.sleep(1)  # Espera por 1 segundo
        seconds -= 1
    
    print("\nContagem finalizada!")
    stop_event.set()  # Sinaliza para parar o piscar do LED
    GPIO.output(LED_PIN, GPIO.HIGH)  # Mantém o LED aceso ao final da contagem

def get_valid_input():
    """Função para solicitar e validar a entrada do usuário."""
    while True:
        try:
            # Solicita um valor ao usuário
            time_input = input("Digite o tempo em segundos para a contagem regressiva: ")
            time_input = int(time_input)  # Converte a entrada para inteiro
            
            # Verifica se o valor é positivo
            if time_input <= 0:
                print("O número deve ser positivo. Tente novamente.")
            else:
                return time_input  # Retorna o valor válido
        except ValueError:
            print("O valor digitado deve ser um número inteiro. Tente novamente.")

try:
    # Inicializa o evento para sinalizar quando parar o LED
    stop_event = threading.Event()

    # Solicita a entrada do usuário e realiza a contagem
    time_in_seconds = get_valid_input()

    # Cria e inicia a thread para piscar o LED
    led_thread = threading.Thread(target=blink_led)
    led_thread.start()

    # Realiza a contagem regressiva na thread principal
    countdown_timer(time_in_seconds)

    # Espera a thread do LED terminar após a contagem regressiva
    led_thread.join()

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
    stop_event.set()  # Para o piscar do LED caso Ctrl+C seja pressionado

finally:
    GPIO.cleanup()  # Limpa a configuração dos pinos GPIO