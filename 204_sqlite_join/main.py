# 204. sqlite joins and row_factory
#
# Row factory lets you access columns by name. A join combines tables. commit() persists;
# :memory: dies with the connection.
#
# Run: python 204_sqlite_join/main.py

import sqlite3
con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row
con.executescript("""
create table t (id integer, name text);
create table u (user_id integer, city text);
insert into t values (1, 'Ada');
insert into u values (1, 'London');
""")
row = con.execute(
    "select t.name, u.city from t join u on t.id = u.user_id"
).fetchone()
print(row["name"], row["city"])
