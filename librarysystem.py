class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # Book is available initially

    def __str__(self):
        return f"'{self.title}' by {self.author} - {'Available' if self.is_available else 'Not Available'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def lend_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.is_available = False
                print(f"Book '{book.title}' has been lent out.")
                return
        print(f"Sorry, the book '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                book.is_available = True
                print(f"Book '{book.title}' has been returned.")
                return
        print(f"Sorry, the book '{title}' was not lent out or doesn't exist.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in the library:")
        for book in self.books:
            print(book)


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Lend a book")
        print("3. Return a book")
        print("4. Display available books")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            book = Book(title, author)
            library.add_book(book)

        elif choice == "2":
            title = input("Enter the title of the book you want to lend: ")
            library.lend_book(title)

        elif choice == "3":
            title = input("Enter the title of the book you want to return: ")
            library.return_book(title)

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            print("Exiting the Library System. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
