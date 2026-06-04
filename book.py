from database import conn, cursor

def add_book():

    title = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))

    query = """
    INSERT INTO books(title, author, quantity)
    VALUES(%s,%s,%s)
    """

    values = (title, author, quantity)

    cursor.execute(query, values)
    conn.commit()

    print("Book Added Successfully")


from database import cursor

def delete_book():
    book_id = int(input("enter book id to delete: "))
    query = "DELETE FROM books WHERE book_id = %s"
    cursor.execute(query,(book_id,))
    conn.commit()
    print("book deleted")

from database import cursor

def update_book():
    book_id=int(input("Enter book ID: "))  
    title = input("enter new title: ")
    author = input("enter new author: ")
    quantity = int(input("enter new quantity: "))
    query = """
    UPDATE books
    SET title=%s, author=%s,quantity=%s 
    WHERE book_id=%s
    """
    values = (title,author,quantity,book_id)
    cursor.execute(query,values)
    conn.commit()
    print("Updated successfully") 

