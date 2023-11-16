import mysql.connector

def create_genre(db_cursor):
    # テーブルが存在しない場合は作成
    db_cursor.execute("""
    DROP TABLE IF EXISTS genre;
    """)
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS genre (
        id INT AUTO_INCREMENT PRIMARY KEY,
        genre VARCHAR(255)
    );
    """)
    db_cursor.execute("""
    insert into genre (genre) values 
    ('小説'),
    ('ビジネス'),
    ('科学'),
    ('ミステリー'),
    ('ファンタジー'),
    ('歴史'),
    ('自己啓発'),
    ('料理')
    ;
    """)

    print('genreテーブル作成完了')