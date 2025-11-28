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

def outcome(user, comp):  # The function that defines who wins
    wins = {"rock": "scissors",
            "paper": "rock",
            "scissors": "paper"}
    if user in wins and wins[user] == comp:
        score[0] += 1
        return "You"
    elif comp in wins and wins[comp] == user:
        score[1] += 1
        return "The Computer"
    else:
        return "No one (it was a tie)"


print("Play 'Rock Paper Scissors' with your computer!")
score = [0, 0]

while True:
    uschoice = valid({"rock", "paper", "scissors", "q"}) # Input Validation
    if uschoice == "q":
        break
    cochoice = choice(("rock", "paper", "scissors")) # Computer's Choice
    print(f"The computer chose {cochoice}.")
    winner = outcome(uschoice, cochoice) # Contains the winner
    print(f"The winner is: {winner}!")
    print(f"The score is (You - Computer): {score[0]} - {score[1]}")
    sleep(1.5)
    c_t() # Clears the user's terminal