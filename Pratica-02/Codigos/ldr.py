from gpiozero import LightSensor
import time

# Configuração do sensor de luz
ldr = LightSensor(4)  # Sensor de luz no pino GPIO 4

def monitor_light():
    try:
        while True:
            light_value = ldr.value  # Obter o valor do sensor de luz (0 a 1)
            print(f"Nível de Luz: {light_value:.2f}")  # Imprimir com 2 casas decimais
            
            time.sleep(1)  # Pausa de 1 segundo entre leituras
    except KeyboardInterrupt:
        print("\nPrograma interrompido.")
    finally:
        print("Encerrando o monitoramento.")

# Executar a função de monitoramento
monitor_light()
