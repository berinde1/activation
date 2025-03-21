# import time
# import board
# import analogio
# import digitalio
# from adafruit_motor import stepper

# DELAY = 0.01
# STEPS = 200

##set up motor command pins as outputs
# coils = (digitalio.DigitalInOut(board.GP22),  #AIN1
#     digitalio.DigitalInOut(board.GP26),       #AIN2
#     digitalio.DigitalInOut(board.GP28),       #BIN1
#     digitalio.DigitalInOut(board.GP27))       #BIN2

# for coil in coils:
#     coil.direction = digitalio.Direction.OUTPUT

##use the stepper motor library to set up motor output
# motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

##run the motor forward
# for step in range(STEPS):
#     motor.onestep()
#     time.sleep(DELAY)

##run the motor backward
# for step in range(STEPS):
#     motor.onestep(direction=stepper.BACKWARD)
#     time.sleep(DELAY)

##run the motor forward with higher torque
# for step in range(STEPS):
#     motor.onestep(style=stepper.DOUBLE)
#     time.sleep(DELAY)

##run the motor backward with higher torque
# for step in range(STEPS):
#     motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#     time.sleep(DELAY)

##run the motor forward and alternate torque levels
# for step in range(STEPS):
#     motor.onestep(style=stepper.INTERLEAVE)
#     time.sleep(DELAY)

##run the motor backward and alternate torque levels
# for step in range(STEPS):
#     motor.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
#     time.sleep(DELAY)

##clear coils so no power is sent to motor & shaft can spin freely
# motor.release()

# --------------------

fsr = analogio.AnalogIn(board.A0)

relay = digitalio.DigitalInOut(board.GP0)
relay.direction = digitalio.Direction.OUTPUT

cleaning_queued = 0
cleaning_complete = 0

def commence_cleaning():
    relay.value = True
    #MOTOR.VALUE = TRUE
    time.sleep(0.1)
    #WHILE LOOP HERE, CHOOSE PARAMTETERS
    #if MOTOR.POSITION = END:
        #MOTOR.VALE = FALSE
        #cleaning_complete == 1
        #time.sleep(1)
        #MOTOR.VALUE = TRUE(OPPOSITE DIRECTION)
        #REMAINING LOGIC: while loop to be checking for when the motors go back to the intial position, when they are, move on. CHANGE EXISTING LOGIC TO RELAYS OFF BEFORE MOTORS MOVING BACK
    if cleaning_complete == 1:
        relay.value = False
        cleaning_complete = 0 #cleaning_complete is also a part of queueing, queues cleaning_complete to be 1 when the motors are at final position

    #relay.value = True
    #print("Test successful!")
    #exit()

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

