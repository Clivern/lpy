# 071. SQLAlchemy
#
# Engine, ORM, select, and filters.
#
# Run: python 071_sqlalchemy/main.py

# --- sqlalchemy engine ---
from sqlalchemy import create_engine, text
engine = create_engine("sqlite+pysqlite:///:memory:")
with engine.connect() as con:
    con.execute(text("create table t (n integer)"))
    con.execute(text("insert into t (n) values (:n)"), {"n": 3})
    con.commit()
    print(con.execute(text("select n from t")).scalar_one())
print(engine.dialect.name)

# --- sqlalchemy orm ---
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
engine = create_engine("sqlite+pysqlite:///:memory:")
Base.metadata.create_all(engine)
with Session(engine) as s:
    s.add(User(id=1, name="Ada"))
    s.commit()
    print(s.scalars(select(User)).first().name)

# --- sqlalchemy select ---
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = "u"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
engine = create_engine("sqlite+pysqlite:///:memory:")
Base.metadata.create_all(engine)
with Session(engine) as s:
    s.add_all([User(id=1, name="Ada"), User(id=2, name="Alan")])
    s.commit()
    q = select(User).where(User.name.startswith("A")).order_by(User.id)
    print([u.name for u in s.scalars(q)])

# --- sqlalchemy filter ---
from sqlalchemy import create_engine, or_, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = "u2"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
engine = create_engine("sqlite+pysqlite:///:memory:")
Base.metadata.create_all(engine)
with Session(engine) as s:
    s.add_all([User(id=1, name="Ada"), User(id=2, name="Bob")])
    s.commit()
    q = select(User).where(or_(User.name == "Ada", User.id == 2))
    print(sorted(u.name for u in s.scalars(q)))
