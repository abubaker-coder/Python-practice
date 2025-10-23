class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"📗 '{book_name}' added to the library!")

    def show_books(self):
        if len(self.books) == 0:
            print("❌ No books available right now.")
        else:
            print(f"\n📚 Books available in {self.name}:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"📖 You borrowed '{book_name}'. Please return it soon!")
        else:
            print("❌ Sorry, that book is not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"✅ Thanks for returning '{book_name}'!")


# ------------ Main program ------------
def main():
    print("🏛️ Welcome to the Python Library System 🏛️")
    library = Library("City Library")

    while True:
        print("\n1. Add Book")
        print("2. Show Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            book_name = input("Enter the name of the book to add: ")
            library.add_book(book_name)

        elif choice == '2':
            library.show_books()

        elif choice == '3':
            book_name = input("Enter the name of the book to borrow: ")
            library.borrow_book(book_name)

        elif choice == '4':
            book_name = input("Enter the name of the book to return: ")
            library.return_book(book_name)

        elif choice == '5':
            print("👋 Thanks for visiting the library!")
            break

        else:
            print("❌ Invalid option, try again.")


if __name__ == "__main__":
    main()