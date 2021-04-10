import database


def prompt_add_book():
    name = input("Enter the name of the book:")
    author = input("Enter the name of the author:")
    database.add_book(name,author)


def list_books():
    database.get_all_books()


def prompt_read_book():
    name = input("Enter the book name you finished reading:")
    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the book name you want to delete:")
    database.delete_book(name)


USER_CHOICE = """
Enter :
- 'a' to add new book
- 'l' to list all books
- 'r' to mark book as read
- 'd' to delete a book
- 'q' to quit

Your choice : """

MENU = {
    'a': prompt_add_book,
    'l': list_books,
    'r': prompt_read_book,
    'd': prompt_delete_book,
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in MENU:
            choice = MENU[user_input]
            choice()
        else:
            print("Unable to find the menu, please try again.")

        user_input = input(USER_CHOICE)

menu()