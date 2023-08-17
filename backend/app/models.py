from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Test(Base):  # type: ignore
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, index=True)
    field_1 = Column(String)
