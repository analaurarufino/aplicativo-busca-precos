import mysql.connector
from abc import ABC, abstractmethod

class Database(ABC):
    
    @abstractmethod
    def connectDB(self):
        pass

class Connect(Database):
    
    def connectDB(self):
        keys = open('database.txt')
        host = keys.readline().split('=')[1].strip()
        username = keys.readline().split('=')[1].strip()
        password = keys.readline().split('=')[1].strip()
        mydb = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
        )
        return mydb


class DataPersistence:
    
    def __init__(self):
        self.database_connection = Connect()
        self.mydb = self.database_connection.connectDB()
        self.cursor = self.mydb.cursor()
          
    def create_table(self):
        new_table = "CREATE TABLE IF NOT EXISTS tabela (name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))"
        self.cursor.execute(new_table)
        self.mydb.commit()
        
    def insert(self, name, email, password):
        insert_query = "INSERT INTO tabela (name, email, password) VALUES (%s, %s, %s)"
        data = (name, email, password)
        self.cursor.execute(insert_query, data)
        self.mydb.commit()
        
    def update(self, name, new_email, new_password):
        update_query = "UPDATE tabela SET email = %s, password = %s WHERE name = %s"
        data = (new_email, new_password, name)
        self.cursor.execute(update_query, data)
        self.mydb.commit()

    def delete_name(self, name):
        first_delete_query = "DELETE FROM tabela WHERE name = %s"
        data = (name,)
        self.cursor.execute(first_delete_query, data)
        self.mydb.commit()
    
    def delete_email(self, email):
        second_delete_query = "DELETE FROM tabela WHERE email = %s"
        data = (email,)
        self.cursor.execute(second_delete_query, data)
        self.mydb.commit()
    
    def delete_password(self, password):
        third_delete_query = "DELETE FROM tabela WHERE password = %s"
        data = (password,)
        self.cursor.execute(third_delete_query, data)
        self.mydb.commit()
        
    def list_all(self):
        list = "SELECT * FROM tabela"
        self.cursor.execute(list)
        return self.cursor.fetchall()
    
    def research(self, search_query):
        research_query = "SELECT * FROM tabela WHERE name LIKE %s OR email LIKE %s OR password LIKE %s"
        data = (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%")
        self.cursor.execute(research_query, data)
        return self.cursor.fetchall()
        
    def disconnectDB(self):
        self.database_connection.close()