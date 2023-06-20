import sqlite3
import fastapi

from moduls import HoursExam2
app = fastapi.FastAPI()


class Hours2Sem:

    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    def count_hours_sem2(self) -> HoursExam2:
        query = """SELECT
        math_analiz, disk_math, algebra
        FROM hours_exam_2;"""
        cursor = self.connection.cursor()
        result = cursor.execute(query)
        for item in result:
            return HoursExam2(
                math_analiz=item[0],
                disk_math=item[1],
                algebra=item[2]
            )
