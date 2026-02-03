# Library Management System 📚

A Python CLI tool designed to manage library assets and member transactions using Object-Oriented Programming.

## 📝 Description

This script simulates a real-world library system. It manages the lifecycle of books and member interactions just like real-world libraries (e.g., borrowing limits, stock availability, and ownership verification).

## 🚀 Features

* **Add Books:** Register new books into the system with Title, Author, and ISBN.
* **Register Members:** Create new member profile with unique IDs.
* **Borrowing System:** Lend books to members with automatic checks for availability and a **3-book limit**.
* **Secure Returns:** Return system that verifies if the member actually possesses the book before accepting it.
* **Live Status:** Real-time updates of book status ("Available" vs "Not_Available").
* **Search Book:** Search if a book is in the library's catalog by its Title or by ISBN, and if yes, get informed about its availability.
* **Show Books:** See all the books the library currently has, with the option of seeing only the available ones.


## 🛠️ Technologies Used

* Python 3.x
* Standard Libraries: `time`
* Concepts: OOP (Classes & Objects), Lists, Input Validation, CLI Menu

## 📅 Version History

* **v1.0** - Initial Release: Advanced system with Book/Member management, secure Borrow/Return logic.
* **v1.2** - 1.2 Release: Added a **Search** option where users can check if a book exists (and if yes, check for its availability) in the library. Also, fixed some logical errors.
* **v1.4** - 1.4 Release: Added a **Show Books** option where users can view the entire library catalog. They can also choose to see only the books that are available for lending. Made some small improvements to prevent issues with book titles.
* **v1.6** - 1.6 Release: Added a **main** function, so the code only gets executed when the file runs directly and not imported as a module. Also, fixed a small issue in **ret** method of the Library class.

---
*Created by [FRONX]*