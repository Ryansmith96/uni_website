#!/usr/bin/env python3.8
from random import randint 

number = randint(1,100)
#guess = int(input("Please guess the number between 1 and 100:   "))



Correct = False
        
while Correct == False:
    guess = int(input("Please guess the number between 1 and 100:   "))
    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too High")
    elif guess == number:
        print("Dead on, congrats")
        Correct = True

