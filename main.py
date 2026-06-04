from book import add_book, delete_book,update_book
from view import view_books
from issue import issue_book
from return_file import return_book
from view import view_books

while True:
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Update Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. View Books")
    print("7. Exit")

    choice = int(input())

    if choice == 1:
        add_book()

    elif choice == 2:
        delete_book()

    elif choice == 3:
        update_book()

    elif choice == 4:
        issue_book()
    elif choice == 5:
        return_book()
    elif choice == 6:
        view_books()        


    elif choice == 7:
        break