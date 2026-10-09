import pytest

from app import create_app
from app.library import Library, LibraryError


@pytest.fixture
def client():
    return create_app().test_client()


# ---------- Unit tests (business logic) ----------
def test_add_book():
    lib = Library()
    book = lib.add_book("Clean Code", "Robert Martin")
    assert book["id"] == 1 and book["available"] is True


def test_add_book_requires_fields():
    with pytest.raises(LibraryError):
        Library().add_book("", "Someone")


def test_search_by_title_and_author():
    lib = Library()
    lib.add_book("Clean Code", "Robert Martin")
    lib.add_book("Refactoring", "Martin Fowler")
    assert len(lib.search("clean")) == 1
    assert len(lib.search("martin")) == 2


def test_issue_and_return_flow():
    lib = Library()
    lib.add_book("Clean Code", "Robert Martin")
    assert lib.issue_book(1)["available"] is False
    with pytest.raises(LibraryError):
        lib.issue_book(1)
    assert lib.return_book(1)["available"] is True
    with pytest.raises(LibraryError):
        lib.return_book(1)


def test_unknown_book():
    with pytest.raises(LibraryError):
        Library().issue_book(99)


# ---------- API tests ----------
def test_home(client):
    assert client.get("/").status_code == 200


def test_api_add_and_search(client):
    res = client.post("/books", json={"title": "Scrum Guide", "author": "Sutherland"})
    assert res.status_code == 201
    found = client.get("/books?q=scrum").get_json()
    assert found[0]["title"] == "Scrum Guide"


def test_api_add_invalid(client):
    assert client.post("/books", json={"title": ""}).status_code == 400


def test_api_issue_return(client):
    client.post("/books", json={"title": "Scrum Guide", "author": "Sutherland"})
    assert client.post("/books/1/issue").status_code == 200
    assert client.post("/books/1/issue").status_code == 400
    assert client.post("/books/1/return").status_code == 200
    assert client.post("/books/1/return").status_code == 400
