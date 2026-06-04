from database import conn, cursor
def view_books():

    cursor.execute(
        "SELECT * FROM books"
    )

    books = cursor.fetchall()

    for book in books:
        print(book)