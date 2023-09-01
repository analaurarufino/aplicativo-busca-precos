import mysql.connector

def connectDB():
    keys = open('database.txt')
    host = keys.readline().split('=')[1]
    username = keys.readline().split('=')[1]
    password = keys.readline().split('=')[1]
    mydb = mysql.connector.connect(
    host=host,
    user=username,
    password=password
    )
    return mydb