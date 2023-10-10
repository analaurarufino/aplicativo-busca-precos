import mysql.connector
from abc import ABC, abstractmethod

class Database(ABC):
    
    @abstractmethod
    def connectDB(self):
        pass

class Connect:
    def __init__(self):
        self.mydb = None

    def connectDB(self):
        keys = open('database.txt')
        host = keys.readline().split('=')[1].strip()
        username = keys.readline().split('=')[1].strip()
        password = keys.readline().split('=')[1].strip()
        self.mydb = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
        )
        return self.mydb


    def close(self):
        if self.mydb:
            self.mydb.close()
        


class DataPersistence:
    def __init__(self, table_name, db):
        self.mydb = db
        self.cursor = self.mydb.cursor()
        self.table_name = table_name
          
    def create_table(self):
        create_table_query = f"CREATE TABLE IF NOT EXISTS {self.table_name} (name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))"
        self.cursor.execute(create_table_query)
        self.mydb.commit()
        
    def insert(self, column_values):
        columns = ', '.join(column_values.keys())
        values = ', '.join(['%s'] * len(column_values))

        insert_query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({values})"
        data = tuple(column_values.values())

        print(data)

        self.cursor.execute(insert_query, data)
        self.mydb.commit()
        
    def get(self, conditions):
        # Constrói a parte da query para a cláusula WHERE
        where_clause = " AND ".join([f"{key} = %s" for key in conditions.keys()])
        values = tuple(conditions.values())

        select_query = f"SELECT * FROM {self.table_name} WHERE {where_clause}"

        self.cursor.execute(select_query, values)
        return self.cursor.fetchone()

    def update(self, conditions, column_values):
        # Constrói a parte da query para a cláusula WHERE
        where_clause = " AND ".join([f"{key} = %s" for key in conditions.keys()])
        values = tuple(list(conditions.values()) + list(column_values.values()))

        set_clause = ", ".join([f"{key} = %s" for key in column_values.keys()])
        update_query = f"UPDATE {self.table_name} SET {set_clause} WHERE {where_clause}"

        self.cursor.execute(update_query, values)
        self.mydb.commit()

    def delete(self, conditions):
        # Constrói a parte da query para a cláusula WHERE
        where_clause = " AND ".join([f"{key} = %s" for key in conditions.keys()])
        values = tuple(conditions.values())

        delete_query = f"DELETE FROM {self.table_name} WHERE {where_clause}"

        self.cursor.execute(delete_query, values)
        self.mydb.commit()
        
    def disconnectDB(self):
        self.database_connection.close()
