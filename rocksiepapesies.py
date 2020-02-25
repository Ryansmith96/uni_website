#!/usr/bin/env python3.8
import random


# values and scores 
#userguess = str(input("rock, paper, scissors:  "))
#computerand = randint(0,2)
computerguess = ""
userscore = 0
computerscore = 0
computerlist = ["rock", "paper", "scissors"]

#computerand = randint(0,2)
#if computerand == 0:
#    computerguess = "rock"
#if computerand == 1:
#    computerguess = "paper"
#if computerand == 2:
#    computerguess = "scissors" 


computerguess = random.choice(computerlist)


  

# the game
while computerscore < 3 and userscore < 3:
    userguess = str(input("rock, paper, scissors:  "))
    if userguess == "rock" and computerguess == "rock":
        print("Computer also played rock: Tie") 
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        computerguess = random.choice(computerlist)
    elif userguess == "rock" and computerguess == "paper":
        print("Computer played paper: You Lose")
        computerscore = computerscore + 1
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        computerguess = random.choice(computerlist)
    elif userguess == "rock" and computerguess == "scissors":
        print("Computer played scissors: You Win!")
        userscore = userscore + 1
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        computerguess = random.choice(computerlist)
    elif userguess == "paper" and computerguess == "rock":
        print("Computer played rock: You Win!")
        userscore = userscore + 1
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        computerguess = random.choice(computerlist)
    elif userguess == "paper" and computerguess == "paper":
        print("Computer also played paper: Tie")
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        computerguess = random.choice(computerlist)
    elif userguess == "paper" and computerguess == "scissors":
        print("Computer played scissors: You Lose")
        computerscore = computerscore + 1
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        computerguess = random.choice(computerlist)
    elif userguess == "scissors" and computerguess == "rock":
        print("Computer played rock: You Lose")
        computerscore = computerscore + 1
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        computerguess = random.choice(computerlist)
    elif userguess == "scissors" and computerguess == "paper":
        print("Computer played paper: You Win!")
        userscore = userscore + 1
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        computerguess = random.choice(computerlist)
    elif userguess == "scissors" and computerguess == "scissors":
        print("Computer played scissors: Tie")
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        computerguess = random.choice(computerlist)
    elif userguess != "rock" or "paper" or "scissors":
        print("Please enter rock, paper, or scissors (no caps no spaces)")




if userscore == 3:
    print("Congrats you won!")
elif computerscore == 3:
    print("You lost to a machine :(")
