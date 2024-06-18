import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS database 
            (num_index INTEGER PRIMARY KEY AUTOINCREMENT, 
            mac_address TEXT, 
            ip_address TEXT, 
            command_line TEXT, 
            time_table TEXT, 
            check_box TEXT)""")

cur.execute("""INSERT INTO database VALUES
            (NULL,
            'de:ad:be:ef',
            '192.180.0.0',
            'ping',
            '2024.06.19 12:05',
            'O'
            )""")

cur.execute("""SELECT * FROM database""")

cur.execute("""UPDATE database SET time_table = '2024.06.19 12:13' WHERE num_index = 1""")

con.commit()
con.close()