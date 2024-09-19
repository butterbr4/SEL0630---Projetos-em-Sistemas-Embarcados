import RPi.GPIO as GPIO
import time

# Configuração dos pinos GPIO
LED_PIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

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
    GPIO.output(LED_PIN, GPIO.HIGH)  # Acende o LED após a contagem regressiva

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
    # Solicita a entrada do usuário e realiza a contagem
    time_in_seconds = get_valid_input()
    countdown_timer(time_in_seconds)

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

finally:
    GPIO.cleanup()  # Limpa a configuração dos pinos GPIO
