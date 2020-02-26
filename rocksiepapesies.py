#!/usr/bin/env python3.8
import random


# values and scores 
computerguess = ""
userscore = 0
computerscore = 0
computerlist = ["rock", "paper", "scissors"]
game = True 

# machine learning append
rock_counter = 0
paper_counter = 0
scissors_counter = 0


def better_decision ():
    max_counter = max(rock_counter, paper_counter, scissors_counter)
    if rock_counter == max_counter:
        return "paper"
    elif paper_counter == max_counter:
        return "scissors"
    elif scissors_counter == max_counter:
        return "rock"
    else:
        random.choice(computerlist)

#computerguess = better_decision()
  

# the game
while game == True:
    userguess = str(input("rock, paper, scissors (press q to quit):  "))
    computerguess = better_decision()
    if userguess == "rock" and computerguess == "rock":
        print("Computer also played rock: Tie") 
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        #computerguess = random.choice(computerlist)
        rock_counter +=1
    elif userguess == "rock" and computerguess == "paper":
        print("Computer played paper: You Lose")
        computerscore = computerscore + 1
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        #computerguess = random.choice(computerlist)
        rock_counter +=1
    elif userguess == "rock" and computerguess == "scissors":
        print("Computer played scissors: You Win!")
        userscore = userscore + 1
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        #computerguess = random.choice(computerlist)
        rock_counter +=1
    elif userguess == "paper" and computerguess == "rock":
        print("Computer played rock: You Win!")
        userscore = userscore + 1
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        #computerguess = random.choice(computerlist)
        paper_counter +=1
    elif userguess == "paper" and computerguess == "paper":
        print("Computer also played paper: Tie")
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        #computerguess = random.choice(computerlist)
        paper_counter +=1
    elif userguess == "paper" and computerguess == "scissors":
        print("Computer played scissors: You Lose")
        computerscore = computerscore + 1
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        #computerguess = random.choice(computerlist)
        paper_counter +=1
    elif userguess == "scissors" and computerguess == "rock":
        print("Computer played rock: You Lose")
        computerscore = computerscore + 1
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        #computerguess = random.choice(computerlist)
        scissors_counter +=1
    elif userguess == "scissors" and computerguess == "paper":
        print("Computer played paper: You Win!")
        userscore = userscore + 1
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
        #computerguess = random.choice(computerlist)
        scissors_counter +=1
    elif userguess == "scissors" and computerguess == "scissors":
        print("Computer played scissors: Tie")
        print("Your score is: " + str(userscore)) 
        print("Computer score is: " + str(computerscore))
       # computerguess = random.choice(computerlist)
        scissors_counter +=1
    elif userguess == "q":
        game = False
    elif userguess != "rock" or "paper" or "scissors" or "q":
        print("Please enter rock, paper, or scissors (no caps no spaces)") 
    if userscore == 3:
        game = False 
        print("Congrats you won!")
    elif computerscore == 3:
        game = False
        print("You lost to a machine :(")


