#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <names>
Student Number: <studnum>
Prac: <Prac Num>
Date: <dd/mm/yyyy>
"""

# import Relevant Librares
import RPi.GPIO as GPIO

global counter
counter = 0

global values
values[] = ["000","001","010","011","100", "101","111"]

def increment(channel):
    global counter
    if counter==7:
        counter=0
    else:
        counter = counter-1

    GPIO.output(led1, values[counter][0])
    GPIO.output(led2, values[counter][1])
    GPIO.output(led3, values[counter][2])

def decrement(channel):
    global counter
    if counter==0:
        counter=7
    else:
        counter-=1

GPIO.add_event_detect(button_up, GPIO.FALLING, callback=increment(), bouncetime=300)


# Logic that you write
def main():
    print("write your logic here")


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
