import time
import board
import analogio
import digitalio

fsr = analogio.AnalogIn(board.A0)

def get_voltage(pin):
    # Convert the 16-bit ADC reading to a voltage (using 3.3V as the reference)
    return (pin.value * 3.3) / 65535

while True:
     voltage = get_voltage(fsr)
     force = 8.8152 * voltage**2 + 4.7946 * voltage
     print("Analog value:", fsr.value, "Voltage: {:.2f} V".format(voltage), "Force: {:.2f} N".format(force))

     if voltage < 0.5:
         print("Sensor not pressed or very lightly pressed.")
     elif voltage < 1.5:
         print("Sensor moderately pressed.")
     else:
         print("Sensor heavily pressed.")

     time.sleep(0.1)

