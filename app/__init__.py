from flask import Flask, jsonify, request

from app.library import Library, LibraryError


def create_app():
    app = Flask(__name__)
    library = Library()

    @app.get("/")
    def home():
        return jsonify(message="Library Management System is running")

    @app.post("/books")
    def add_book():
        data = request.get_json(silent=True) or {}
        try:
            book = library.add_book(data.get("title", ""), data.get("author", ""))
        except LibraryError as err:
            return jsonify(error=str(err)), 400
        return jsonify(book), 201

    @app.get("/books")
    def list_books():
        query = request.args.get("q", "")
        return jsonify(library.search(query))

    @app.post("/books/<int:book_id>/issue")
    def issue_book(book_id):
        try:
            return jsonify(library.issue_book(book_id))
        except LibraryError as err:
            return jsonify(error=str(err)), 400

    @app.post("/books/<int:book_id>/return")
    def return_book(book_id):
        try:
            return jsonify(library.return_book(book_id))
        except LibraryError as err:
            return jsonify(error=str(err)), 400

    return app
