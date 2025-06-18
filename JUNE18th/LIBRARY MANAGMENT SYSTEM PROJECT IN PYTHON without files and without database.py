class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.issued = 0

    def available_copies(self):
        return self.quantity - self.issued


class Library:
    def __init__(self):
        self.books = {}  # key: book_id, value: Book object

    def add_book(self, book_id, title, author, quantity):
        if book_id in self.books:
            print("Book ID already exists, updating quantity.")
            self.books[book_id].quantity += quantity
        else:
            self.books[book_id] = Book(book_id, title, author, quantity)
        print(f"Book '{title}' added/updated successfully.")

    def view_books(self):
        if not self.books:
            print("No books available in library.")
            return
        print(f"{'ID':<6}{'Title':<30}{'Author':<20}{'Available':<10}")
        for book in self.books.values():
            print(f"{book.book_id:<6}{book.title:<30}{book.author:<20}{book.available_copies():<10}")

    def search_book(self, title):
        found = False
        for book in self.books.values():
            if title.lower() in book.title.lower():
                print(f"Found - ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Available: {book.available_copies()}")
                found = True
        if not found:
            print("No book found with that title.")

    def issue_book(self, book_id):
        if book_id not in self.books:
            print("Book ID not found.")
            return
        book = self.books[book_id]
        if book.issued < book.quantity:
            book.issued += 1
            print(f"Book '{book.title}' issued successfully.")
        else:
            print("Sorry, all copies of this book are issued.")

    def return_book(self, book_id):
        if book_id not in self.books:
            print("Book ID not found.")
            return
        book = self.books[book_id]
        if book.issued > 0:
            book.issued -= 1
            print(f"Book '{book.title}' returned successfully.")
        else:
            print("No issued copies to return.")


def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book(Borrowed)")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            quantity = int(input("Enter Quantity: "))
            library.add_book(book_id, title, author, quantity)

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            title = input("Enter title to search: ")
            library.search_book(title)

        elif choice == '4':
            book_id = input("Enter Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == '5':
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
