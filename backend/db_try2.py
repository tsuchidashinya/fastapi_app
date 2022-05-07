import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('SELECT * from articles')
# for row in c:
#     print(row)

print(c.fetchone())
