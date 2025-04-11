# 396. SQLAlchemy engine
#
# create_engine("sqlite+pysqlite:///:memory:") is a connection factory. text() wraps SQL.
# connect() is a connection. Use bound parameters.
#
# Run: python 396_sqlalchemy_engine/main.py

from sqlalchemy import create_engine, text
engine = create_engine("sqlite+pysqlite:///:memory:")
with engine.connect() as con:
    con.execute(text("create table t (n integer)"))
    con.execute(text("insert into t (n) values (:n)"), {"n": 3})
    con.commit()
    print(con.execute(text("select n from t")).scalar_one())
