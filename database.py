import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Twesha@123",
    database="Library_Management_system"
)

cursor = conn.cursor()

print("Database Connected")

cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)