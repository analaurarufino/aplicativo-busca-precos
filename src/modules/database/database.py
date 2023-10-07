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
            password=password
        )
        return mydb


class DataPersistence:
    
    def __init__(self):
        self.database_connection = Connect()
        self.mydb = self.database_connection.connectDB()
          
    def create_table(self):
    def insert(self, mydb):
    def update(self,mydb):
    def delete(self,):
    def list_all(self):
    def research(self,):
    def disconnectDB(self):