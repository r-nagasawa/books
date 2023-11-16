@echo off
start /WAIT python .\DB\createDB.py
echo bookdbデータベース作成
start /WAIT python .\status\insertStatus.py
echo statusテーブル作成
start /WAIT python .\genre\insertGenre.py
echo genreテーブル作成
start /WAIT python .\user\createUserData.py
start /WAIT python .\user\insertUser.py
echo userテーブル作成
start /WAIT python .\books\createBooksData.py
start /WAIT python .\books\insertBooks.py
echo booksテーブル作成
start /WAIT python .\history\createHistoryData.py
start /WAIT python .\history\insertHistory.py
echo historyテーブル作成


pause


