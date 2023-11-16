import random
import faker
import csv
from datetime import datetime, timedelta
import mysql.connector


def create_user(db_cursor):
    fake = faker.Faker(['en_US', 'ja_JP'])  # ダミーデータを生成するためのライブラリ

    sample_data = []
    now_date = datetime.now()

    for _ in range(250):

        stock = random.randint(0, 2)
        lending_status = 'Not Available' if stock == 0 else 'Available'
        tmp_date = datetime.now() - timedelta(days=random.randint(7, 365))
        last_lending_date = tmp_date.strftime('%Y-%m-%d')
        due_date = (tmp_date + timedelta(days=31)).strftime('%Y-%m-%d')
        
        user = {
            'last_name': fake.last_name(),
            'first_name': fake.first_name(),
            'birth': fake.date_of_birth(minimum_age=16, maximum_age=100).strftime('%Y-%m-%d'),
            'sex': random.choice(['M', 'F']),
            'tel': fake.phone_number(),
            'mail': fake.email(),
            'address': fake.address().replace("\n", " "),
            #'due_date': due_date
            'user_registered': (now_date + timedelta(days=random.randint(-400, -100))).strftime('%Y-%m-%d')
        }
        sample_data.append(user)
    #    print(user)

    # 生成されたサンプルデータを表示
    #for book in sample_data:
    #   print(book)
    #


    csv_filename = './csv/sample_user.csv'

    # CSVファイルにデータを書き込む
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['last_name', 'first_name', 'birth', 'sex', 'tel', 'mail', 'address', 'user_registered']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()  # ヘッダーを書き込む

        for book in sample_data:

            writer.writerow(book)  # 各書籍のデータを行として書き込む

    print(f'{len(sample_data)}件のデータが{csv_filename}にエクスポートされました。')

    # テーブルが存在しない場合は作成
    db_cursor.execute("""
    DROP TABLE IF EXISTS user;
    """)
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        last_name VARCHAR(255),
        first_name VARCHAR(255),
        birth DATE,
        sex VARCHAR(10),
        tel VARCHAR(50),
        mail VARCHAR(255),
        address VARCHAR(1000),
        user_registered DATE
    );
    """)

    csv_filename = './csv/sample_user.csv'

    # CSVファイルからデータを読み込み、データベースに挿入
    with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
        
            #last_lending_date = None if row['last_lending_date'] == '' else datetime.strptime(row['last_lending_date'], '%Y-%m-%d').date()
            # データベースに挿入
            db_cursor.execute("""
            INSERT INTO user (last_name, first_name, birth, sex, tel, mail, address, user_registered)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                row['last_name'], row['first_name'], row['birth'], (row['sex']),
                row['tel'], row['mail'], row['address'], row['user_registered']
            ))

    print('userテーブル作成完了')