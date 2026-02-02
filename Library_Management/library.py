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
            msg1 = ""
            for i in self.books:
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
                    if i.status == "Available":
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

    def by_title(self):
        title = input("Enter the book's Titile in lowercase: ").strip().lower().capitalize()
        flag = False
        for i in self.books:
            if title == i.title:
                flag = True
                print(f"The book belongs to the library's collection.")
                if i.status == "Available": print(f"The {title} is available for lending.")
                else: print(f"Howerver, the {title} is not available for lending right now.")
                break
        if not(flag): print("There is no such book in the library.")

    def by_isbn(self):
        isbn = str(input("Enter the book's ISBN: ")).strip()
        flag = False
        for i in self.books:
            if isbn == i.isbn:
                flag = True
                print(f"The ISBN you provided corresponds to the {i.title} and it belongs to the library's collection.")
                if i.status == "Available": print(f"The {i.title} is available for lending.")
                else: print(f"However, the {i.title} is not available for lending right now.")
                break
        if not(flag): print("The ISBN you provided does not match with any of the library's books.")
    
    def show(self, choice):
        if choice == "F":
            print("The library has the following books:")
            for i in self.books: print(f"{i.title} by {i.author} (ISBN: {i.isbn})")
        else:
            flag = False
            c = 0
            for i in self.books:
                if i.status == "Available":
                    if c == 0:
                        c = 1
                        flag = True
                        print("The available books are:")
                    print(f"{i.title} by {i.author} (ISBN: {i.isbn})")
            if not(flag): print("No books are available right now.")


def add_book(library):
    title = input("Enter the Title: ").strip().lower().capitalize()
    author = input("Enter the Author: ").strip().lower().capitalize()
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

def ex():
    while True:
        choice = input("Are you sure you want to exit(Y/N)? ").strip().upper()
        if choice in ("Y","N","YES","NO"): break
    if choice in ("Y","YES"):
        print("Going to exit in:")
        for i in range(1,4):
            print(i)
            sleep(1)
        exit()

def search(library):
    while True:
        pre = input("Do you want to search a book by its Title or by its ISBN(T/I)? ").strip().upper()
        if pre in ("I","ISBN", "TITLE", "T"): break
        else: 
            print("Please enter a valid choice (T for Title or I for ISBN).")
            sleep(1)
    if pre in ("T","TITLE"): library.by_title()
    else: library.by_isbn()
    sleep(2)

def show_books(library):
    while True:
        choice = input("You want a full list books or only the available ones (F,A)? ").strip().upper()
        if choice in ("F","FULL","A","AVAILABLE"): break
        else: 
            print("Please enter a valid choice (F for a full list or A for only the available books.)")
            sleep(1)
    choice = "F" if choice == "FULL" else ("A" if choice == "AVAILABLE" else choice)
    library.show(choice)
    sleep(2)

def main():
    l1 = Library()
    while True:
        menu = """--- Library Management System --- \n1. Add Book \n2. Register Member \n3. Borrow Book \n4. Return Book \n5. Search a book\n6. Show Books\n7. Exit"""
        print(menu)
        while True:
            c = int(input("Enter a choice: "))
            if c in (1,2,3,4,5,6,7): 
                if c != 7:
                    print("Loading...")
                    break
                else: ex()
            else: 
                print("Please enter a valid choice")
                sleep(1)

        if c == 1: add_book(l1)
        elif c == 2: register_member(l1)
        elif c == 3: borrow_book(l1)
        elif c == 4: return_book(l1)
        elif c == 5: search(l1)
        elif c == 6: show_books(l1)

if __name__ == "__main__":
    main()