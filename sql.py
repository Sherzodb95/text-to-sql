import sqlite3

# Connect to sqlite3
connection = sqlite3.connect('students.db')

# Create a cursor object
cursor = connection.cursor()

# Drop the table if it already exists
cursor.execute("DROP TABLE IF EXISTS STUDENTS")

# Create the table
table_info = """
CREATE TABLE STUDENTS(
    NAME VARCHAR(25), 
    CLASS VARCHAR(25), 
    SECTION VARCHAR(25), 
    MARKS INT
);
"""
cursor.execute(table_info)

# Insert records
cursor.execute("INSERT INTO STUDENTS VALUES('Sherzod', 'ML Engineering', 'A', 90)")
cursor.execute("INSERT INTO STUDENTS VALUES('David', 'Data Analytics', 'B', 88)")
cursor.execute("INSERT INTO STUDENTS VALUES('Allen', 'Data Science', 'A', 95)")
cursor.execute("INSERT INTO STUDENTS VALUES('John', 'Data Analytics', 'A', 90)")
cursor.execute("INSERT INTO STUDENTS VALUES('Antony', 'Text Analytics', 'A', 45)")

# Display the records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENTS")
for row in data:
    print(row)

# Commit and close the connection
connection.commit()
connection.close()