class LibraryItem:
    def __init__(self, name):
        self.name = name
        self.available = True

class Book(LibraryItem):
    def __init__(self, name, author):
        super().__init__(name)
        self.author = author

class Computer(LibraryItem):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

class Library:
    def __init__(self):
        self.books = [Book("Introduction to Algorithms", "Thomas H. Cormen"), Book("Python Crash Course", "Eric Matthes")]
        self.computers = [Computer("MacBook Pro", "Apple"), Computer("ThinkPad X1 Carbon", "Lenovo")]

    def borrow_book(self, student, book_name):
        for book in self.books:
            if book.name == book_name and book.available:
                book.available = False
                print(f"{student.get_name()} borrowed the book '{book.name}'")
                return
        print("Sorry, the requested book is not available.")

    def borrow_computer(self, student, computer_name):
        for computer in self.computers:
            if computer.name == computer_name and computer.available:
                computer.available = False
                print(f"{student.get_name()} borrowed the computer '{computer.name}'")
                return
        print("Sorry, the requested computer is not available.")

    def borrow_computer(self, user, computer_name):
        print(f"{user.get_name()} borrowed the computer {computer_name}.")