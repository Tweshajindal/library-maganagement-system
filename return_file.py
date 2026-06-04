from database import cursor, conn
def return_book():

    trans_id = int(input("enter transaction id : "))
    book_id = int(input("Enter book ID: "))
    query="""
    update transactions
    set return_date = curdate(),
        status = 'Returned'
    where trans_id=%s
    """
    cursor.execute(query,(trans_id,))
    cursor.execute(
        "update books set quantity = quantity + 1 where book_id=%s",
        (book_id,)
    )
    conn.commit()
    print("book returned succesfully")