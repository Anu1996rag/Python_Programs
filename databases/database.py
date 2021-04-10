"""
For adding and retrieving items from the books database
"""

# create an empty book list
books = []


# adding new book
def add_book(name, author):
    books.append({
        "name": name,
        "author": author,
        "read": False
    })
    print("Book added to the library.")


# to get all the books
def get_all_books():
    if books:
        for book in books:
            print(book)
    else:
        print("No books in the library.")


def mark_book_as_read(name):
    if name not in books:
        print("Unable to find the book.Please check the name again.\nList of available books.")
        get_all_books()

    else:
        for book in books:
            if book["name"] == name:
                book["read"] = True


def delete_book(name):
    if name not in books:
        print("Unable to find the book.Please check the name again.\nList of available books.")
        get_all_books()
    else:
        new_books_list = [book for book in books if book["name"] != name]
        print("Requested book deleted. New book list:")
        for book in new_books_list:
            print(book)

