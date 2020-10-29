from microbit import *
import random


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K" ,"L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"   ]
while True:
    if button_a.is_pressed():
        display.scroll(random.choice(letters))
    
    elif button_b.is_pressed():
        display.scroll(str(random.randint(1, 99)))