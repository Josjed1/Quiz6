# library_interface.py
from abc import ABC, abstractmethod

class CatalogInterface(ABC):
    @abstractmethod
    def search_by_title(self, title):
        pass

    @abstractmethod
    def search_by_author(self, author):
        pass

    @abstractmethod
    def search_by_genre(self, genre):
        pass


class BorrowingInterface(ABC):
    @abstractmethod
    def borrow_book(self, user_id, book_id):
        pass

    @abstractmethod
    def return_book(self, user_id, book_id):
        pass

    @abstractmethod
    def generate_borrowing_report(self):
        pass


class LibraryUserInterface(CatalogInterface, BorrowingInterface):
    pass


class LibrarianInterface(CatalogInterface, BorrowingInterface):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def remove_book(self, book_id):
        pass

    @abstractmethod
    def generate_overdue_report(self):
        pass

    @abstractmethod
    def generate_popularity_report(self):
        pass


# book.py
class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre


# library.py
class Library:
    def __init__(self):
        self.catalog = []
        self.borrowed_books = []
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def add_book_to_catalog(self, book):
        self.catalog.append(book)

    def remove_book_from_catalog(self, book_id):
        self.catalog = [b for b in self.catalog if b.book_id != book_id]

    def search_by_title(self, title):
        return [book for book in self.catalog if title.lower() in book.title.lower()]

    def search_by_author(self, author):
        return [book for book in self.catalog if author.lower() in book.author.lower()]

    def search_by_genre(self, genre):
        return [book for book in self.catalog if genre.lower() in book.genre.lower()]

    def borrow_book(self, user_id, book_id):
        # Logic to handle book borrowing
        print(f"User {user_id} borrowed book {book_id}.")

    def return_book(self, user_id, book_id):
        # Logic to handle book return
        print(f"User {user_id} returned book {book_id}.")

    def generate_borrowing_report(self):
        # Logic to generate borrowing report
        print("Generated borrowing report.")

    def generate_overdue_report(self):
        # Logic to generate overdue report
        print("Generated overdue report.")

    def generate_popularity_report(self):
        # Logic to generate popularity report
        print("Generated popularity report.")


# i.py
if __name__ == "__main__":
    library = Library()

    # Create a librarian with broader management features
    librarian = LibrarianInterface()
    library.add_user(librarian)

    # Create a guest user with limited functionalities
    guest_user = CatalogInterface()
    library.add_user(guest_user)

    # Add books to the catalog
    book1 = Book(1, "Book A", "Author X", "Genre 1")
    book2 = Book(2, "Book B", "Author Y", "Genre 2")
    library.add_book_to_catalog(book1)
    library.add_book_to_catalog(book2)

    # Librarian performs various actions
    librarian.add_book(book1)
    librarian.generate_popularity_report()

    # Guest user searches for books
    search_results = guest_user.search_by_author("Author X")
    print("Search results:", search_results)
