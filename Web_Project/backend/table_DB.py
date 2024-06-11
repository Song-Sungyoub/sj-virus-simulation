import sqlite3

con = sqlite3.connect('zombie.db')
c = con.cursor()

c.execute("CREATE TABLE info_list (ip_address varchar(50), zombie_num varcahar(50))")

con.commit()
con.close()