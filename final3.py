class Book:
    def __init__(self, book_id, title, author, level):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.level = level
        self.available = True

    def display_info(self):
        availability = "Available" if self.available else "Not Available"
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Level: {self.level}")
        print(f"Availability: {availability}")


class Member:
    def __init__(self, member_id, name, email, level):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []

    def display_info(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Level: {self.level}")
        print("Borrowed Books:")
        if not self.borrowed_books:
            print("None")
        else:
            for book in self.borrowed_books:
                print(f"- {book.title}")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display_info()
                print("")

    def display_members(self):
        if not self.members:
            print("No members in the library.")
        else:
            for member in self.members:
                member.display_info()
                print("")

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def edit_member(self, member_id):
        member = self.find_member_by_id(member_id)
        if member is None:
            print("Member not found.")
        else:
            print("Current Member Details:")
            member.display_info()
            print("")
            name = input("Enter the updated member name: ")
            email = input("Enter the updated member email: ")
            level = input("Enter the updated level (A/B/C): ")
            member.name = name
            member.email = email
            member.level = level
            print("Member details updated successfully.")

    def delete_member(self, member_id):
        member = self.find_member_by_id(member_id)
        if member is None:
            print("Member not found.")
        else:
            self.members.remove(member)
            print(f"{member.name} has been deleted from the library.")

    def borrow_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)
        if member is None:
            print("Member not found.")
        elif book is None:
            print("Book not found.")
        elif book.level > member.level:
            print("This book is not suitable for the member's level.")
        elif not book.available:
            print("This book is not available.")
        else:
            book.available = False
            member.borrowed_books.append(book)
            print(f"{member.name} has borrowed {book.title}.")

    def return_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)
        if member is None:
            print("Member not found.")
        elif book is None:
            print("Book not found.")
        elif book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f"{member.name} has returned {book.title}.")
        else:
            print(f"{member.name} did not borrow {book.title}.")


def display_menu():
    print("--------------------- Welcome to the Library System ---------------------")
    print("1. Add Member")
    print("2. Edit Member")
    print("3. show Members")
    print("4. Delete Member")
    print("5. Add Book")
    print("6. show Books")
    print("7. Borrow Book")
    print("8. Return Book")
    print("9. Exit")

library = Library()

while True:
    display_menu()
    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        member_id = input("Enter the member ID: ")
        name = input("Enter the member name: ")
        email = input("Enter the member email: ")
        level = input("Enter the level (A/B/C): ")
        member = Member(member_id, name, email, level)
        library.add_member(member)
        print("Member added successfully.")
    elif choice == "2":
        member_id = input("Enter the member ID to edit: ")
        library.edit_member(member_id)

    elif choice == "3":
        library.display_members()
    elif choice == "4":
        member_id = input("Enter the member ID: ")
        library.delete_member(member_id)

    elif choice == "5":
        book_id = input("Enter the book ID: ")
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        level = input("Enter the level (A/B/C): ")
        book = Book(book_id, title, author, level)
        library.add_book(book)
        print("Book added successfully.")

    elif choice == "6":
        library.display_books()

    elif choice == "7":
        member_id = input("Enter the member ID: ")
        book_id = input("Enter the book ID: ")
        library.borrow_book(member_id, book_id)
    elif choice == "8":
        member_id = input("Enter the member ID: ")
        book_id = input("Enter the book ID: ")
        library.return_book(member_id, book_id)
    elif choice == "9":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
