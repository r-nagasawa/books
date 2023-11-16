#import mysql.connector

def create_book_DB(cursor):
    cursor.execute("DROP DATABASE IF EXISTS bookdb;")
    cursor.execute("CREATE DATABASE bookdb;")
    cursor.execute("use bookdb;")
    # cursor.close()

    print('bookdbデータベース作成完了')
