import mysql.connector
from DB import createDB_callable
from books import insertBooks_callable
from user import insertUser_callable
from history import insertHistory_callable
from genre import insertGenre_callable
from status import insertStatus_callable

if __name__ == '__main__':
    print('処理開始')
    cnx = None
    cnx = mysql.connector.connect(
        user='root',  # ユーザー名
        password='root', 
        host='localhost'  # ホスト名(IPアドレス）
    )

    border = '-----------------------------------------------------------------'
    cursor = cnx.cursor()
    createDB_callable.create_book_DB(cursor)
    print(border)
    insertBooks_callable.insert_books(cursor)
    print(border)
    insertUser_callable.create_user(cursor)
    print(border)
    insertHistory_callable.create_history(cursor)
    print(border)
    insertGenre_callable.create_genre(cursor)
    print(border)
    insertStatus_callable.create_status(cursor)
    print(border)
    
    
    cnx.commit()
    cursor.close()
    cnx.close()
    print('bookDB作成完了')