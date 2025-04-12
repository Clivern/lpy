# 398. SQLAlchemy select
#
# select(User).where(User.name == "Ada") is the 2.0 query style. join, order_by, and limit
# chain. Core and ORM share the same SQL compiler.
#
# Run: python 398_sqlalchemy_select/main.py

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
