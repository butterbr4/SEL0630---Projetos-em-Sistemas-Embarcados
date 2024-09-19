import RPi.GPIO as GPIO
import time

# Configurar o pino do LED
LED_PIN = 16

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Configurar PWM no pino do LED com uma frequência de 1000 Hz
pwm_led = GPIO.PWM(LED_PIN, 1000)
pwm_led.start(0)  # Inicializar o PWM com ciclo de trabalho 0%

def set_pwm_duty_cycle():
    """Função para definir o duty cycle via entrada do terminal."""
    while True:
        try:
            # Solicitar o ciclo de trabalho (duty cycle) do usuário
            duty_cycle = input("Defina o ciclo de trabalho do PWM (0 a 100%): ")
            duty_cycle = float(duty_cycle)
            
            # Verificar se o valor está dentro do intervalo permitido
            if 0 <= duty_cycle <= 100:
                pwm_led.ChangeDutyCycle(duty_cycle)  # Ajustar o ciclo de trabalho
                print(f"Intensidade do LED ajustada para {duty_cycle}%")
            else:
                print("O valor deve estar entre 0 e 100.")
                
        except ValueError:
            print("O valor digitado deve ser um número válido.")

try:
    set_pwm_duty_cycle()

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

finally:
    pwm_led.stop()  # Parar o PWM
    GPIO.cleanup()  # Limpar os pinos GPIO
