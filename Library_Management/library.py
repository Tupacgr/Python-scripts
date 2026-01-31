from time import sleep

class Book:
    def __init__(self, title, author, isbn, status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

class Member:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.times = 0
        self.lended = list()

class Library:
    def __init__(self):
        self.books = list()
        self.members = list()
    def add(self, title, author, isbn):
        self.books.append(Book(title, author, isbn, "Available"))
    def register(self, name, id):
        self.members.append(Member(name, id))
    def lend(self,id, isbn):
        msg = ""
        for i in self.members:
            if id == i.id:
                if i.times<3:
                    msg = "Times_Correct"
                    c = i
                else:
                    msg = "Times_Incorrect"
                    print("The member can only borrow up to 3 books!")
                break
        if msg == "": 
            msg = "No_User"
            print("There is no such member!")
        if msg == "Times_Correct":
            for i in self.books:
                msg1 = ""
                if isbn == i.isbn:
                    if i.status == "Available":
                        i.status = "Not_Available"
                        msg1 = "Available_True"
                        c.times += 1
                        c.lended.append(i.isbn)
                        print(f"The book {i.title} has been lended to {c.name}.")
                    else:
                        msg1 = "Available_False"
                        print(f"The book {i.title} is not available.")
                    break
                if msg1 == "":
                    msg1 = "No_Book"
                    print("There is no such book.")

    def ret(self, id, isbn):
        msg = ""
        for i in self.members:
            if id == i.id:
                msg = "User_Correct"
                c = i
                break
        if msg == "": print("There is no such member!")
        if msg == "User_Correct":
            msg1 = ""
            for i in self.books:
                if isbn == i.isbn:
                    msg1 = "ISBN_Correct"
                    if i. status == "Available":
                        msg1 = "Already_Available"
                        break
            if msg1 == "": print("There is no such book.")
            elif msg1 == "Already_Available": print("The book is already available.")
            elif msg1 == "ISBN_Correct" and i.isbn in c.lended: 
                c.times -= 1
                c.lended.remove(i.isbn)
                i.status = "Available"
                print(f"{i.title} returned by {c.name}")
            elif msg1 == "ISBN_Correct": print("The book was not lended to you.")
    def grep(self):
        pass

def add_book(library):
    title = input("Enter the Title: ").strip().capitalize()
    author = input("Enter the Author: ").strip().capitalize()
    isbn = str(input("Enter the ISBN: ")).strip()
    library.add(title, author, isbn)
    print(f"Book {title.capitalize()} added successfully.")
    sleep(2)

def register_member(library):
    name = input("Enter the name: ").strip().capitalize()
    id = str(input("Enter the member ID: ")).strip()
    library.register(name, id)
    print(f"Member {name} registered.")
    sleep(2)

def borrow_book(library):
    id = str(input("Enter the Member's ID: ")).strip()
    isbn = str(input("Enter the book's ISBN: ")).strip()
    library.lend(id, isbn)
    sleep(2)

def return_book(library):
    id = str(input("Enter Member ID: ")).strip()
    isbn = str(input("Enter ISBN: ")).strip()
    library.ret(id, isbn)
    sleep(2)

l1 = Library()
while True:
    menu = """--- Library Management System --- \n1. Add Book \n2. Register Member \n3. Borrow Book \n4. Return Book \n5. Exit"""
    print(menu)
    while True:
        flag = True
        c = int(input("Enter a choice: "))
        if c in (1,2,3,4,5): 
            if c != 5:
                print("Loading...")
                break
            else:
                flag = False
                print("System going to exit in:")
                for i in range(3):
                    print(i+1)
                    sleep(1)
                break
        else: 
            print("Please enter a valid choice")
            sleep(1)
    if not(flag): break
    if c == 1: add_book(l1)
    elif c == 2: register_member(l1)
    elif c == 3: borrow_book(l1)
    elif c == 4: return_book(l1)