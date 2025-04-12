# 399. SQLAlchemy filters
#
# in_, is_, and or_ live in sqlalchemy. where() can take several AND clauses. returning()
# (on supporting backends) yields inserted rows.
#
# Run: python 399_sqlalchemy_filter/main.py

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
