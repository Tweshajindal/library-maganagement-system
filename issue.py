from database import cursor, conn
def issue_book():

    student_id = int(input("Enter Student ID: "))
    book_id = int(input("Enter Book ID: "))

    query = """
    INSERT INTO transactions
    (student_id, book_id, issue_date, status)
    VALUES(%s,%s,CURDATE(),'Issued')
    """

    cursor.execute(query, (student_id, book_id))

    cursor.execute(
        "UPDATE books SET quantity = quantity - 1 WHERE book_id=%s",
        (book_id,)
    )

    conn.commit()

    print("Book Issued Successfully")