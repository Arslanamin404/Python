# Write a Library class with no_of_books and books(list) as two instance variables. WAP to create a library from this Library class
# and show how you can print all books, add a book and get the number of books using different methods.
# Show that your program does not persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.__books = []
        self.__no_of_books = 0

    def add_book(self, book):
        self.__books.append(book)
        self.__no_of_books += 1
        print(f"'{book}' has been added to the Library.")

    def remove_book(self, book):
        if book in self.books:
            self.__books.remove(book)
            print(f"'{book}' has been removed from the Library successfully!")
        else:
            print(f"{self.book} Book is not in Library!")

    def get_count_books(self):
        return self.__no_of_books

    def list_books(self):
        if self.__no_of_books == 0:
            print("Library is Empty!")
        else:
            print("List of Books in the Library: ")
            for i, book in enumerate(self.__books, start=1):
                print(f"{i}. {book}")


my_library = Library()
while True:
    print("\nLibrary Menu:")
    print("1. Print all books")
    print("2. Add a book")
    print("3. Get the number of books")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        my_library.list_books()
    elif choice == '2':
        book = input("Enter the name of the book to add: ")
        my_library.add_book(book)
    elif choice == '3':
        num_books = my_library.get_count_books()
        print(f"The number of books in the library is: {num_books}")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
