import json
import os

FILE = "library.json"


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False

    def to_dict(self):
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "issued": self.issued
        }


class Library:

    def __init__(self):
        self.books = self.load_data()

    def load_data(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                return json.load(f)
        return {}

    def save_data(self):
        with open(FILE, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self):
        bid = input("Enter Book ID: ")

        if bid in self.books:
            print("Book ID already exists!")
            return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(bid, title, author)
        self.books[bid] = book.to_dict()

        self.save_data()
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books.values():
            status = "Issued" if book["issued"] else "Available"
            print("Book ID:",book["id"])
            print("Title:",book["title"])
            print("Author:",book["author"])
            

    def search_book(self):
        keyword = input("Enter title or author: ").lower()

        found = False

        for book in self.books.values():
            if (keyword in book["title"].lower()
                or keyword in book["author"].lower()):
                print(book)
                found = True

        if not found:
            print("Book not found!")

    def issue_book(self):
        bid = input("Enter Book ID: ")

        if bid not in self.books:
            print("Book not found!")
        elif self.books[bid]["issued"]:
            print("Book already issued!")
        else:
            self.books[bid]["issued"] = True
            self.save_data()
            print("Book issued successfully!")

    def return_book(self):
        bid = input("Enter Book ID: ")

        if bid not in self.books:
            print("Book not found!")
        elif not self.books[bid]["issued"]:
            print("Book is not issued!")
        else:
            self.books[bid]["issued"] = False
            self.save_data()
            print("Book returned successfully!")

    def report(self):
        total = len(self.books)
        issued = sum(
            1 for b in self.books.values() if b["issued"]
        )

        print("Total Books:", total)
        print("Issued Books:", issued)
        print("Available Books:", total - issued)


library = Library()

while True:
    print("\n--- LIBRARY MANAGEMENT ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Reports")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        library.search_book()
    elif choice == "4":
        library.issue_book()
    elif choice == "5":
        library.return_book()
    elif choice == "6":
        library.report()
    elif choice == "7":
        break
    else:
        print("Invalid choice!")