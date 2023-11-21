import mysql.connector

def create_login_table(db_cursor):
    # テーブルが存在しない場合は作成
    db_cursor.execute("""
    DROP TABLE IF EXISTS role;
    """)
    db_cursor.execute("""
    DROP TABLE IF EXISTS login_user;
    """)
    
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS role (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(32)
    );
    """)

    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS login_user (
        id integer primary key,
        name varchar(128) not null,
        email varchar(256) not null,
        password varchar(128) not null,
        role integer not null
    );
    """)
    
    db_cursor.execute("""
    insert into role(id, name) values
    (1, 'ROLE_GENERAL'),
    (2, 'ROLE_ADMIN');
    """)

    db_cursor.execute("""
    insert into login_user(id, name, email, password, role) values
    (2, 'eightbit', 'eightbit@eightbit.co.jp', '$2a$10$QIV2huHMTSGFC7WDYWYLPuCQ/oD92aBqRA6ql2TTBapHKnUiklF32', 1);
    """)

    print('login関連テーブル作成完了')