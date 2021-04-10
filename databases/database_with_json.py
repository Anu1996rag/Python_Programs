"""
For adding and retrieving items from the books database in the form of csv

read,author,read\n
"""

import json

# create an empty book list
books_file = "books.json"


# adding new book
def add_book(name, author):
    books = get_all_books()
    books.append({
        "name": name,
        "author": author,
        "read": False
    })
    _save_all_books(books)
    print("Book added to the library.")


# saving all the books : to be called only in this file
def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


# to get all the books
def get_all_books():
    try:
        with open(books_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Unable to find the database.")
        exit(0)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book["name"] == name:
            book["read"] = True
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    new_books_list = [book for book in books if book["name"] != name]
    print("Requested book deleted. New book list:")
    # saving the new book list
    _save_all_books(new_books_list)
    for book in new_books_list:
        print(book)
