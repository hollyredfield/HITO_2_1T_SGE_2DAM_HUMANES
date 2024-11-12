# database/connection.py
import mysql.connector
from mysql.connector import Error

# He implementado esta clase usando el patrón Singleton para asegurar una única conexión
class DBConnection:
    # Uso una variable de clase para mantener la única instancia
    _instance = None

    def __new__(cls):
        # Me aseguro de que solo exista una instancia de la conexión
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def connect(self):
        try:
            if not self.connection or not self.connection.is_connected():
                self.connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='encuesta'
                )
            return self.connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    def get_connection(self):
        if not self.connection or not self.connection.is_connected():
            self.connect()
        return self.connection

    def close(self):
        if self.connection and self.connection.is_connected():
            try:
                self.connection.close()
                print("Connection closed successfully")
            except Error as e:
                print(f"Error closing the connection: {e}")

