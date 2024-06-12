import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Sairam@123",
        database="cosmetics",
        charset="utf8"
    )
