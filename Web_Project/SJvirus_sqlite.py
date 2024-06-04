import sqlite3

con = sqlite3.connect("SJvirus_DB", isolation_level=None)

c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text)")

userList = (
    (3, 'Lee', 'lee1234@naver.com', '010-1111-1111', 'leesite.com'),
    (4, 'Yun', 'yun1234@naver.com', '010-2222-2222', 'yunsite.com'),
    (5, 'JO', 'jo1234@naver.com', '010-3333-3333', 'josite.com')
)

c.executemany("Insert into users(id, username, email, phone, website) values(?, ?, ?, ?, ?)", userList)