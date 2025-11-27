from os import name, system
from random import choice
from time import sleep 

def c_t(): # A function that clears the user's terminal
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
c_t()

def valid(check): # The function for input validation
    while True: 
        inp = input("'Rock', 'Paper' or 'Scissors' (press 'q' to quit)? ").strip().lower()
        if inp in check:
            return inp
        else:
            print("Please enter a valid choice (or 'q' to quit)!")
            sleep(1) 

def comp(check):
    return choice(check)

def outcome(user, comp):  # The function that defines who wins
    if user == comp:
        return "No one (it was a tie)"
    elif user == "rock":
        if comp == "scissors":
            return "You"
        else:
            return "The Computer"
    elif user == "paper":
        if comp == "rock":
            return "You"
        else:
            return "The Computer"
    elif user == "scissors":
        if comp == "paper":
            return "You"
        else:
            return "The Computer"


print("Play 'Rock Paper Scissors' with your computer!")

while True:
    uschoice = valid({"rock", "paper", "scissors", "q"}) # Input Validation
    if uschoice == "q":
        break
    cochoice = comp(("rock", "paper", "scissors")) # Computer's Choice
    print(f"The computer chose {cochoice}.")
    winner = outcome(uschoice, cochoice) # Contains the winner
    print(f"The winner is: {winner}!")
    sleep(1.5)
    c_t() # Clears the user's terminal