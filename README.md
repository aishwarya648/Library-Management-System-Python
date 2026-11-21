# 📚 Library Management System

## About the Project
The Library Management System is a simple console-based application developed using Python. It helps manage books in a library by allowing users to add new books, view available books, search for books, issue books, and return books.

The project uses JSON file storage to save book details, so the data remains available even after the program is closed.

## Features

- **Add Book:** Add new books using Book ID, title, and author name.
- **View Books:** Display all books along with their availability status.
- **Search Book:** Search books by title or author name.
- **Issue Book:** Issue available books to users.
- **Return Book:** Return issued books and update their status.
- **Reports:** Display total books, issued books, and available books.
- **Data Persistence:** Store book information in a JSON file.

## Technologies Used

- Python
- JSON
- File Handling
- Object-Oriented Programming (OOP)

## Project Structure

```text
Library-Management-System/
│
├── library.py
├── library.json
└── README.md
```

- `library.py` – Main Python program containing the library management functions.
- `library.json` – Stores book information.
- `README.md` – Project documentation.

## How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Library-Management-System-Python.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Library-Management-System-Python
```

### Step 3: Run the Program

```bash
python library.py
```

## Menu Options

```text
--- LIBRARY MANAGEMENT ---

1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Reports
7. Exit
```

## Sample Output

```text
--- LIBRARY MANAGEMENT ---

1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Reports
7. Exit

Enter choice: 1

Enter Book ID: 101
Enter Book Title: Python Programming
Enter Author Name: John

Book added successfully!
```

## Learning Outcomes

- Understanding Python classes and objects.
- Learning Object-Oriented Programming concepts.
- Working with JSON data.
- Using file handling to store and retrieve information.
- Implementing CRUD-like operations.
- Developing menu-driven applications.

## Future Enhancements

- Add user/student details.
- Add due dates for books.
- Implement book fine calculation.
- Develop a graphical user interface.
- Connect the application to a database such as SQLite.

## Author

Developed as part of a Python programming task.
