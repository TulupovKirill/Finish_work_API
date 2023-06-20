from pydantic import BaseModel


class UserExam2(BaseModel):
    date: str
    math_analiz: int | None = None
    disk_math: int | None = None
    algebra: int | None = None


class UserToUpdateExam2(BaseModel):
    id: int
    math_analiz: int | None = None
    disk_math: int | None = None
    algebra: int | None = None


class HoursExam2(BaseModel):
    math_analiz: int | None = None
    disk_math: int | None = None
    algebra: int | None = None
