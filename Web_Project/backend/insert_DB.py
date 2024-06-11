import sqlite3

con = sqlite3.connect('zombie.db')
c = con.cursor()

c.execute("INSERT INTO info_list VALUES ('testip1', '1')")

con.commit()
con.close()