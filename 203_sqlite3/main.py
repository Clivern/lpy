# 203. sqlite3
#
# sqlite3 is an in-process SQL database in the stdlib. connect(":memory:") is great for
# lessons. Use placeholders, never f-strings, for values.
#
# Run: python 203_sqlite3/main.py

import sqlite3
con = sqlite3.connect(":memory:")
con.execute("create table users (id integer, name text)")
con.execute("insert into users values (?, ?)", (1, "Ada"))
row = con.execute("select name from users where id = ?", (1,)).fetchone()
print(row[0])
con.close()
