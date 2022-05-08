# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# ----------------------| Gymnasiearbete W&E's Fräsiga Robot |-----------------------
# ----------------------| Written by: William Pettersson     |-----------------------
# ----------------------| Version 1.0                        |-----------------------
# ----------------------| https://WoERobotics.xyz/           |-----------------------
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# Import libraries
from gpiozero import OutputDevice # https://gpiozero.readthedocs.io/en/stable/
import time

# Define pins
relay = OutputDevice(5)
motor1a1 = OutputDevice(22)
motor1a2 = OutputDevice(27)
motor1b1 = OutputDevice(17)
motor1b2 = OutputDevice(12)
motor2a1 = OutputDevice(26) 
motor2a2 = OutputDevice(25)
motor2b1 = OutputDevice(13)
motor2b2 = OutputDevice(6)

# Functions
# Movement(AWD):
def Forward():
    motor1a1.on()
    motor1b2.on()
    motor2a1.on()
    motor2b2.on()

def Backward():
    motor1a2.on()
    motor1b1.on()
    motor2a2.on()
    motor2b1.on()

def Right():
    motor1a1.on()
    motor1b1.on()
    motor2a1.on()
    motor2b1.on()

def Left():
    motor1a2.on()
    motor1b2.on()
    motor2a2.on()
    motor2b2.on()

def Stop(): # Stops all motors
    motor1a1.off()
    motor1a2.off()
    motor1b1.off()
    motor1b2.off()
    motor2a1.off()
    motor2a2.off()
    motor2b1.off()
    motor2b2.off()

# Relay
def Lights(mode): # Can be used to either specify on/off or just toggle
    if mode == 1:
        relay.on()
    elif mode == 2:
        relay.off()
    elif mode == 0:
        relay.toggle()
     
# Startup message
print('Welcome to W&E´s Robot v1.0!')
print('To run a test simply enter "test" on the action promt')
print('You can also enter "quit" to exit the program')

# Loop that checks for inputs and performs specified action
while True:
    Stop() # Stop the robot after action is complete
    print('')
    action = input('Enter W,A,S,D or E and press Enter: ').lower() # WASD = movement keys, E toggles the lights on and off
    if action == 'w':
        Forward()
        input('Press Enter to stop')
    elif action == 's':
        Backward()
        input('Press Enter to stop')
    elif action == 'a':
        Left()
        input('Press Enter to stop')
    elif action == 'd':
        Right()
        input('Press Enter to stop')
    elif action == 'e':
        Lights(0)
    elif action == 'test': # Test that runs though all the functions
        if input('Run test? Y/N: ').lower() == 'y':
            print('Forward')
            Forward()
            time.sleep(2)
            Stop()
            print('Backward')
            Backward()
            time.sleep(2)
            Stop()
            print('Left')
            Left()
            time.sleep(2)
            Stop()
            print('Right')
            Right()
            time.sleep(2)
            Stop()
            print('Lights')
            Lights(1)
            time.sleep(2)
            Lights(2)
            print('Test done!')
    elif action == 'quit': # Breaks the loop and stops the robot if it's moving(should not be able to happen)
        print('Quitting program!')
        Stop()
        break
    else:
        print('invalid command')
