from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Test
from app.schemas import TestOut, TestCreate

app = FastAPI()


@app.get("/tests", response_model=list[TestOut])
async def read_test_details(db: Session = Depends(get_db)) -> list[TestOut]:
    db_tests = db.query(Test).all()
    return [TestOut.from_orm(test) for test in db_tests]


@app.post("/test", response_model=TestOut)
async def put_test_details(test: TestCreate, db: Session = Depends(get_db)) -> TestOut:
    new_test = Test(field_1=test.field_1)
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    return new_test
