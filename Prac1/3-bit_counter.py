#!/usr/bin/python3
# import Relevant Librares
import RPi.GPIO as GPIO




"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Jack Teversham
Student Number: TVRJAC001
Prac: Pac 01
Date: 23/07/2019
"""
global counter
counter = 0

global values
values = ["000","001","010","011","100","101","111"]

led_1 = 17 #physical pin 11
led_2 = 23 #physical pin 16
led_3 = 24 #physical pin 18

button_up = 27 #physical pin 13
button_down = 22 #physical pin 15

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)
GPIO.setup(button_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.output(led_1, 0)
GPIO.output(led_2, 0)
GPIO.output(led_3, 0)



def increment(channel):
    global counter
    print("incrementing")
    GPIO.output(led_1, int(values[counter][0]))
    GPIO.output(led_2, int(values[counter][1]))
    GPIO.output(led_3, int(values[counter][2]))
    if counter==6:
        counter=0
    else:
        counter +=1
    

def decrement(channel):
    global counter
    print("Decrementing")
    GPIO.output(led_1, int(values[counter][0]))
    GPIO.output(led_2, int(values[counter][1]))
    GPIO.output(led_3, int(values[counter][2]))
    if counter==0:
        counter=6
    else:
        counter -= 1



GPIO.add_event_detect(button_up, GPIO.FALLING, callback= increment,
                  bouncetime=200)
GPIO.add_event_detect(button_down, GPIO.FALLING, callback= decrement,
                  bouncetime=200)

# Logic that you write
def main():
    #setup()
    money = "money"



# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
