import datetime

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    username="root",
    passwd="12345678",
    database="sakila",
    autocommit=True
)
# db.autocommit = True

mycursor = db.cursor()

mycursor.execute('SELECT * FROM actor;')

person = mycursor.fetchone()

while person:
    print(person[3] - datetime.timedelta(days=10))
    person = mycursor.fetchone()