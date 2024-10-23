import smbus
import time

# Inicializa o barramento I2C
bus = smbus.SMBus(1)  # 1 indica /dev/i2c-1

# Endereço I2C do Arduino (deve corresponder ao definido no Arduino)
DEVICE_ADDRESS = 0x08

def read_potentiometer():
    try:
        # Solicita 2 bytes do Arduino
        data = bus.read_i2c_block_data(DEVICE_ADDRESS, 0, 2)
        
        # Reconstrói o valor original usando bit shift
        pot_value = data[0] * 256 + data[1]
        
        return pot_value
    except Exception as e:
        print(f"Erro na leitura I2C: {e}")
        return None

if __name__ == "__main__":
    while True:
        value = read_potentiometer()
        if value is not None:
            print(f"Valor recebido: {value}")
        time.sleep(1)  # Aguarda 1 segundo antes da próxima leitura
