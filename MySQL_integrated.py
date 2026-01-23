import mysql.connector

#connecting to MYSQL server
conn=mysql.connector.connect(
    host='localhost',
    user='Username',
    password='Password'
)
objCursor=conn.cursor()

#creating a database
objCursor.execute("CREATE DATABASE IF NOT EXISTS DB_name")
print("Database 'DB_name' created (or already exists).")

#saving the changes
conn.commit()

#closing the cursor and connection
objCursor.close()
conn.close()

#connect to MySQL server with the database created
conn=mysql.connector.connect(
    host='localhost',
    user='Username',
    password='Password',
    database='DB_name'
)

objCursor = conn.cursor()

#Creating a Table
table1=("""
 CREATE TABLE IF NOT EXISTS table1 (
    Time VARCHAR(50),
    Name VARCHAR(100),
    Duration VARCHAR(150),
    Purpose VARCHAR(250)
)
""")
objCursor.execute(table1)
objCursor.execute("SHOW TABLES")
print(objCursor.fetchall())  #print tables

#saving changes
conn.commit()

#Inserting values in the table created
parent="INSERT INTO table1 (Time,Name,Duration,Purpose) VALUES (%s, %s, %s, %s)"
Vals=[
    ("08:00 AM", "Morning Routine", "60", "Wake up, freshen up, breakfast"),
    ("09:00 AM", "Work/Study", "60", "Focus on tasks or study"),
    ("10:00 AM", "Work/Study", "60", "Continue work/study"),
    ("11:00 AM", "Break", "30", "Short break, stretch"),
    ("11:30 AM", "Work/Study", "90", "Finish morning tasks"),
    ("01:00 PM", "Lunch", "60", "Have lunch, relax"),
    ("02:00 PM", "Exercise", "60", "Walk, gym, or yoga"),
    ("03:00 PM", "Work/Study", "120", "Afternoon tasks"),
    ("05:00 PM", "Snack/Break", "30", "Tea/snack break"),
    ("05:30 PM", "Work/Study", "90", "Finish remaining tasks"),
    ("07:00 PM", "Dinner", "60", "Eat dinner, relax"),
    ("08:00 PM", "Leisure", "60", "Hobbies, reading, TV"),
    ("09:00 PM", "Planning", "30", "Plan next day"),
    ("09:30 PM", "Relax", "30", "Wind down, meditate"),
    ("10:00 PM", "Sleep Prep", "30", "Prepare for sleep"),
]
objCursor.executemany(parent,Vals)

#saving changes
conn.commit() 

#closing the cursor and connection
objCursor.close()
conn.close()