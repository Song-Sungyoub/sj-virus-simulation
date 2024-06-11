import sqlite3

con = sqlite3.connect('zombie.db')
c = con.cursor()

for row in c.execute('SELECT * FROM info_list'):
    print(row)

con.close()