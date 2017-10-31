"""
    This is a program to be used to clean the valve.

    Press F5 or "Run" the program to operate this.
    
"""

import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Channel for GPIO
# 4, 17, 22, 27
#High is on
#Low is off

question = "Would you want to run all of them?"
question += "\n y(yes)/n(no)/a(air)/q(quit) \n"

while True:

    ans = input(question)
    os.system("clear")

#If you want to run one color only
    if ans == 'n':
        question2 = "\nWhat color do you want?"
        question2 += "\n w(white)/y(yellow)/b(black)/r(red)/q(quit) \n"
        color = input(question2)
        r = [4]
        w = [17]
        y = [22]
        b = [27]
        GPIO.setup(w,GPIO.OUT)
        GPIO.setup(y,GPIO.OUT)
        GPIO.setup(b,GPIO.OUT)
        GPIO.setup(r,GPIO.OUT)


        while True:
            if color == 'w':
                GPIO.output(w,GPIO.HIGH)
                print("White valve is on.")
                time.sleep(0.5)
                GPIO.output(w,GPIO.LOW)
                print("White valve is off.")
                break
            elif color == 'y':
                GPIO.output(y,GPIO.HIGH)
                print("Yellow valve is on.")
                time.sleep(0.5)
                GPIO.output(y,GPIO.LOW)
                print("Yellow valve is off.")
                break
            elif color == 'b':
                GPIO.output(b,GPIO.HIGH)
                print("Black valve is on.")
                time.sleep(0.5)
                GPIO.output(b,GPIO.LOW)
                print("Black valve is off")
                break
            elif color == 'r':
                GPIO.output(r,GPIO.HIGH)
                print("Red valve is on.")
                time.sleep(0.5)
                GPIO.output(r,GPIO.LOW)
                print("Red valve is off.")
                break
            elif color == 'q':
                break
            elif color not in ("w","y","b","r","q"):
                print("Please enter the right key!")
                color = input(question2)
            else:
                break
#if you want to just run all of them together            
    elif ans == 'y':

        question3 = "How many times do you want to burst? \n"
        try:
            number = int(input(question3))
        except ValueError:
            print("Please enter a number only!")
        else:
            x = [4,17,22,27]
            GPIO.setup(x,GPIO.OUT)
            while number > 0:
                GPIO.output(x,GPIO.HIGH)
                print("Valves are all on.")
                time.sleep(0.5)
                GPIO.output(x,GPIO.LOW)
                print("Valves are all off.")
                time.sleep(1)
                number = number - 1
#if you want to run all air

    elif ans == 'a':
        y = [4,17,22,27]
        GPIO.setup(y,GPIO.OUT)
        #turns on all valve
        
        GPIO.output(y,GPIO.HIGH)
        turn_off = "Do you want to close the air now?"
        print (turn_off)
        turn_ans = input("\n y(yes) \n")
        while True:
            if turn_ans == 'y':
                #turns off all valve
                GPIO.output(y,GPIO.LOW)
                break
            elif turn_ans != 'y':
                print(turn_off)
                turn_ans = input("\n y(yes) \n")
            else:
                continue
#if you want to quit the program            
    elif ans == 'q':
        break
#if you hit other keys in the first question
    elif ans not in ('y','n','a','q'):
        print("PLease type the right key!")
#if you type something other than what is listed
    else:
        break
