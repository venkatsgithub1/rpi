from picozero import LED
from time import sleep

# GPIO pin 0
indicator8 = LED(0)
# GPIO pin 1
indicator4 = LED(1)
# GPIO pin 2
indicator2 = LED(2)
# GPIO pin 3
indicator1 = LED(3)

def switchoffleds(*leds):
    for led in leds:
        led.off()

def lightupnumber(binary_string):
    if binary_string[0] == '1':
        indicator8.on()
    if binary_string[1] == '1':
        indicator4.on()
    if binary_string[2] == '1':
        indicator2.on()
    if binary_string[3] == '1':
        indicator1.on()
        
def get_binary_string(number):
    return '{0:04b}'.format(number)

# method to light 4 bit numbers from 1 to 15
def light_4bit_numbers():
    for number in range(1, 16):
        binary_string = get_binary_string(number)
        lightupnumber(binary_string)
        sleep(0.5)
        switchoffleds(indicator8, indicator4, indicator2, indicator1)
        
# method to switch on leds based on input
def switchonleds():
    number = int(input("Enter a number less than 16\n"))
    if number < 16:
        switchoffleds(indicator8, indicator4, indicator2, indicator1)
        binary_string = get_binary_string(number)
        print('bin str', binary_string)
        if len(binary_string) == 4:
            lightupnumber(binary_string)
    else:
        print('invalid input, try again')
        switchoffleds(indicator8, indicator4, indicator2, indicator1)

try:
    while True:
        # uncomment switchonleds to input a number and observe leds in binary format.
        #switchonleds()
        # the method plays 1 to 15, with leds switching on and off in loop.
        light_4bit_numbers()
except KeyboardInterrupt:
    switchoffleds(indicator8, indicator4, indicator2, indicator1)
