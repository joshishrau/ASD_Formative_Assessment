class LibraryError(Exception):
    """Raised for invalid library operations."""


class Library:
    def __init__(self):
        self._books = {}
        self._next_id = 1

    def add_book(self, title, author):
        if not title.strip() or not author.strip():
            raise LibraryError("Title and author are required")
        book = {
            "id": self._next_id,
            "title": title.strip(),
            "author": author.strip(),
            "available": True,
        }
        self._books[book["id"]] = book
        self._next_id += 1
        return book

    def search(self, query=""):
        query = query.lower().strip()
        return [
            b for b in self._books.values()
            if query in b["title"].lower() or query in b["author"].lower()
        ]

    def _get(self, book_id):
        if book_id not in self._books:
            raise LibraryError("Book not found")
        return self._books[book_id]

    def issue_book(self, book_id):
        book = self._get(book_id)
        if not book["available"]:
            raise LibraryError("Book is already issued")
        book["available"] = False
        return book

    def return_book(self, book_id):
        book = self._get(book_id)
        if book["available"]:
            raise LibraryError("Book was not issued")
        book["available"] = True
        return book
