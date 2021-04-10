"""
For adding and retrieving items from the books database in the form of csv

read,author,read\n
"""

# create an empty book list
books_file = "books.txt"


# adding new book
def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f"{name},{author},0\n")  # 0 for read = False
    print("Book added to the library.")


# saving all the books : to be called only in this file
def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


# to get all the books
def get_all_books():
    try :
        with open(books_file, 'r') as file:
            lines = [line.strip().split(',') for line in file.readlines()]

        return [
            {'name': line[0], 'author': line[1], 'read': line[2]}
            for line in lines
        ]
    except FileNotFoundError:
        print("Unable to find the database.")
        exit(0)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book["name"] == name:
            book["read"] = '1'
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    new_books_list = [book for book in books if book["name"] != name]
    print("Requested book deleted. New book list:")
    # saving the new book list
    _save_all_books(new_books_list)
    for book in new_books_list:
        print(book)
