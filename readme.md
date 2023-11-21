# 仕様

### 発火スクリプト：createBookDB.py
各フォルダ内のpythonモジュールを呼び出してDBを作成する  
各モジュール単体でも実行可能なファイルをoldファイルに格納している  
同名のbatファイルはpython内のログが表示されないので使用しない  
books, user, historyテーブル作成時に生成されるデータはcsvフォルダに格納される  

### 発火方法：cmdから発火スクリプトのパスに移動し、
    python createBookDB.py
※DBのユーザ、パスワードは以下に合わせる必要がある  
| user  | password |
| ----- |--------- |
| root  | root     |

又は`createBookDB.py`内の以下の行を環境に合わせて編集して下さい

```python
user='root',
password='root', 
```

※必要なモジュールはpipでインストールする必要がある



### 必要モジュール：
コマンドプロンプトから以下のコマンドを実行し、  
それぞれのモジュールをインストールして下さい  

faker  
```cmd
pip install faker
```
mysql.connector  
```cmd
pip install mysql-connector-python
```
