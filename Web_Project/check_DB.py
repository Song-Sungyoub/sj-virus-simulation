import sqlite3

con = sqlite3.connect("SJvirus_DB", isolation_level=None)

c = con.cursor()

sl = c.execute("select * from users")

print(sl.fetchall())