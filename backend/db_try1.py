import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('CREATE TABLE articles (id int, title varchar(1024), body text, created datetime)')

# Insert実行
c.execute("INSERT INTO articles VALUES (1,'今朝のおかず','魚を食べました','2020-02-01 00:00:00')")
c.execute("INSERT INTO articles VALUES (2,'今日のお昼ごはん','カレーを食べました','2020-02-02 00:00:00')")
c.execute("INSERT INTO articles VALUES (3,'今夜の夕食','夕食はハンバーグでした','2020-02-03 00:00:00')")

conn.commit()

conn.close()