from os import name, system
from time import sleep

def c_t(): # A function that clears the user's terminal
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def show(set1): # A function to display the desired set
    k = 0
    for i in set1:
        k += 1
        print(f"{k}. {i.capitalize()}")


menu = [
    "--- HR Skill Matcher Options ---",
    "1. Add new skill(s) for Candidate A",                   
    "2. Add new skill(s) for Candidate B",                   
    "3. See their Common skills",       
    "4. See TOTAL combined skills",     
    "5. See skills Candidate A has but B doesn't",
    "6. See skills Candidate B has but A doesn't",
    "7. See their UNIQUE skills",
    "8. Remove a skill from a candidate",                    
    "9. Quit"                                                
]

a_skills = set()
b_skills = set()

while True:
    c_t()
    for i in menu:
        print(i)
    choice = input("Enter your choice (only the number): ") # Reads the user's choice
    if choice == "1":
        sk = input("Enter the skill(s) you want to add for candidate A seperated by commas (e.g. Python, Sql, Html): ")
        print(f"{sk} successfully inserted.")
        sk = sk.lower().strip().split(",")
        for i in range(len(sk)):
            sk[i] = sk[i].strip()
            a_skills.add(sk[i])
        sleep(1) # Waits for 1 second before clearing the terminal
    elif choice == "2":
        sk = input("Enter the skill(s) you want to add for candidate B seperated by commas (e.g. Python, Sql, Html): ")
        print(f"{sk} successfully inserted.") 
        sk = sk.lower().strip().split(",")
        for i in range(len(sk)):
            sk[i] = sk[i].strip()
            b_skills.add(sk[i])
        sleep(1) # Waits for 1 second before clearing the terminal
    elif choice == "3":
        new = a_skills.intersection(b_skills)
        print("Their Common skills are: ")
        show(new)
        sleep(4) # Waits for 4 seconds before clearing the terminal
    elif choice == "4":
        new = a_skills.union(b_skills)
        print("The skills you will gain if you hire both candidates are:")
        show(new)
        sleep(4) # Waits for 4 seconds before clearing the terminal
    elif choice == "5":
        new = a_skills.difference(b_skills)
        print("The skills that Candidate A has but B doesn't are:")
        show(new)
        sleep(4) # Waits for 4 seconds before clearing the terminal
    elif choice == "6":
        new = b_skills.difference(a_skills)
        print("The skills that Candidate B has but A doesn't are:")
        show(new) 
        sleep(4) # Waits for 4 seconds before clearing the terminal
    elif choice == "7":
        new = a_skills.symmetric_difference(b_skills)
        print("Their Unique skills are: ")
        show(new)
        sleep(4) # Waits for 4 seconds before clearing the terminal
    elif choice == "8":
        while True:
            c = input("Enter 'A' for candidate A skill removal or 'B' for candidate B skill removal: ")
            c = c.strip().upper()
            if c == "A" or c == "B":
                break
            else:
                print("Please enter a valid input")
        if c == "A":
            sk = input("Enter the skill name you want to remove from candidate A: ")
            sk = sk.strip().lower()
            if sk in a_skills:
                a_skills.remove(sk)
                print(f"{sk.capitalize()} successfully removed")
            else:
                print(f"{sk.capitalize()} not found")
            sleep(1) # Waits for 1 second before clearing the terminal
        elif c == "B":
            sk = input("Enter the skill name you want to remove from candidate B: ")
            sk = sk.strip().lower()
            if sk in b_skills:
                b_skills.remove(sk)
                print(f"{sk.capitalize()} successfully removed")
            else:
                print(f"{sk.capitalize()} not found")
            sleep(1) # Waits for 1 second before clearing the terminal
    elif choice == "9":
        while True:
            final = input("Are you sure you want to quit(YES/NO)? ")
            final = final.strip().upper()
            if final == "YES" or final == "NO":
                break
            else:
                print("Please enter a valid input")
        if final == "YES":
            print("Going to quit in: ")
            for i in range(3, 0, -1):
                print(i)
                sleep(1) # Waits for 1 second before clearing the terminal
            break
        else:
            print("Process aborted")
            sleep(1) # Waits for 1 second before clearing the terminal
    else:
        print("Please enter a valid input")
        sleep(2) # Waits for 2 seconds before clearing the terminal