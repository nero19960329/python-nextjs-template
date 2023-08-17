from loguru import logger
from sqlalchemy.orm import Session

from app.db import SessionLocal, engine
from app.models import Base, Test

Base.metadata.create_all(engine)


def create_initial_data(db: Session) -> None:
    test_foo = db.query(Test).filter(Test.field_1 == "foo").first()
    if not test_foo:
        db.add(Test(field_1="foo"))
        db.commit()
        logger.debug("Created `foo` test data")

    test_bar = db.query(Test).filter(Test.field_1 == "bar").first()
    if not test_bar:
        db.add(Test(field_1="bar"))
        db.commit()
        logger.debug("Created `bar` test data")


if __name__ == "__main__":
    session = SessionLocal()
    create_initial_data(session)
    session.close()
