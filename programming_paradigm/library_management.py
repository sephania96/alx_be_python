class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            print("Book is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            print("Book is already available.")


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print("Book not found.")

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")