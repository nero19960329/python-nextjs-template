from pydantic import BaseModel


class TestBase(BaseModel):
    field_1: str


class TestCreate(TestBase):
    pass


class TestOut(TestBase):
    id: int

    class Config:
        from_attributes = True
