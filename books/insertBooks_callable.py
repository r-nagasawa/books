import random
import faker
import csv
from datetime import datetime, timedelta
#import mysql.connector

def insert_books(db_cursor):
    fake = faker.Faker(['en_US', 'ja_JP'])  # ダミーデータを生成するためのライブラリ

    # genres = ['小説', 'ビジネス', '科学', 'ミステリー', 'ファンタジー', '歴史', '自己啓発', '料理']
    sample_data = []
    now_date = datetime.now()
    
    for _ in range(1000):

        stock = random.randint(0, 2)
        lending_status = 2 if stock == 0 else 1
        
        # tmp_date = datetime.now() - timedelta(days=random.randint(7, 365))
        # last_lending_date = tmp_date.strftime('%Y-%m-%d')
        # due_date = (tmp_date + timedelta(days=31)).strftime('%Y-%m-%d')
        
        book = {
            'title': fake.catch_phrase(),
            'author': fake.name(),
    #        'genre': random.choice(genres),
            'genre': random.randint(1, 8),
            'publication_year': random.randint(1980, 2023),
            'isbn': fake.isbn13(),
            'stock': stock,
            'lending_status': lending_status,
            #'due_date': due_date
            'registration_date': (now_date + timedelta(days=random.randint(-200, -5))).strftime('%Y-%m-%d')
        }
        sample_data.append(book)
        #print(book)

    # 生成されたサンプルデータを表示
    #for book in sample_data:
    #   print(book)
    #


    csv_filename = './csv/sample_books_v2.csv'

    # CSVファイルにデータを書き込む
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['title', 'author', 'genre', 'publication_year', 'isbn', 'stock', 'lending_status', 'registration_date']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()  # ヘッダーを書き込む

        for book in sample_data:
            """
            lending_status = random.choice(['Available', 'Not Available'])
            last_lending_date = None if lending_status == 'Available' else (datetime.now() - timedelta(days=random.randint(7, 365))).strftime('%Y-%m-%d')
            
            book['lending_status'] = lending_status
            book['last_lending_date'] = last_lending_date
            """
            writer.writerow(book)  # 各書籍のデータを行として書き込む

    print(f'{len(sample_data)}件のデータが{csv_filename}にエクスポートされました。')

    db_cursor.execute("""
    DROP TABLE IF EXISTS books;
    """)
    # テーブルが存在しない場合は作成
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        genre INT,
        publication_year INT,
        isbn VARCHAR(50),
        stock INT,
        lending_status INT, 
        registration_date DATE
    );
    """)

    csv_filename = './csv/sample_books_v2.csv'

    # CSVファイルからデータを読み込み、データベースに挿入
    with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
        
            #last_lending_date = None if row['last_lending_date'] == '' else datetime.strptime(row['last_lending_date'], '%Y-%m-%d').date()
            # データベースに挿入
            db_cursor.execute("""
            INSERT INTO books (title, author, genre, publication_year, isbn, stock, lending_status, registration_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                row['title'], row['author'], row['genre'], int(row['publication_year']),
                row['isbn'], row['stock'], row['lending_status'], row['registration_date']
            ))

    print('booksテーブル作成完了')
    