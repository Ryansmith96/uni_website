#!/usr/bin/env python3.8
from math import *

def addition (num1, num2):
    result = num1 + num2
    return result 
def minus (num1, num2):
    result = num1 - num2
    return result 
def multiply (num1, num2):
    result = num1 * num2
    return result
def divide (num1, num2):
    result = num1 / num2
    return result

operator = input("Please enter the function you need:   ")
num1 = int(input("Please enter the first number:   ")) 
num2 = int(input("Please enter the second number:   "))


if operator == "+":
     answer = addition(num1, num2)
elif operator == "-":
     answer = minus(num1, num2)
elif operator == "*":
     answer = multiply(num1, num2)
elif operator =="/":
     answer = divide(num1, num2)

print("Answer:  " + str(answer))        


