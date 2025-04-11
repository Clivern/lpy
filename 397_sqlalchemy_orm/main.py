# 397. SQLAlchemy ORM
#
# Mapped columns on a DeclarativeBase subclass are the table. Session talks to the engine.
# add and commit persist. scalars().all() fetches.
#
# Run: python 397_sqlalchemy_orm/main.py

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
