import sqlite3
import fastapi

from moduls import UserExam2, UserToUpdateExam2
from Hours import Hours2Sem

app = fastapi.FastAPI()
connection_to_hours = sqlite3.connect('hours2.sqlite', check_same_thread=False)


class User:

    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection

    def create(self, user: UserExam2) -> UserExam2:
        user_in_db = UserExam2(
            date=user.date,
            math_analiz=user.math_analiz,
            disk_math=user.disk_math,
            algebra=user.algebra,
        )
        query = """
        INSERT INTO exam_2 (date, math_analiz, disk_math, algebra)
        VALUES (?, ?, ?, ?);"""
        cursor = self.connection.cursor()
        cursor.execute(
            query,
            (
                user_in_db.date,
                user_in_db.math_analiz,
                user_in_db.disk_math,
                user_in_db.algebra,
            )
        )
        self.connection.commit()

        return user_in_db

    def get_by_position(self, id: int) -> UserExam2:
        query = """
        SELECT id, date, math_analiz, disk_math, algebra
        FROM exam_2 WHERE id=?;
        """
        cursor = self.connection.cursor()
        result = cursor.execute(query, str(id)).fetchone()
        if result is None:
            raise fastapi.HTTPException(status_code=404, detail='Not found!')
        return UserExam2(
            id=result[0],
            date=result[1],
            math_analiz=result[2],
            disk_math=result[3],
            algebra=result[4],
        )

    def all_position(self) -> dict[UserExam2]:
        query = """SELECT
         id, date, math_analiz, disk_math, algebra
         FROM exam_2;"""
        cursor = self.connection.cursor()
        all_item = cursor.execute(query)
        result = dict()
        for item in all_item:
            result[item[0]] = UserExam2(
                date=item[1],
                math_analiz=item[2],
                disk_math=item[3],
                algebra=item[4])
        return result

    def update_position(self, user: UserToUpdateExam2) -> UserToUpdateExam2:
        user_in_db = UserToUpdateExam2(
            id=user.id,
            math_analiz=user.math_analiz,
            disk_math=user.disk_math,
            algebra=user.algebra,
        )
        query = """
                UPDATE exam_2
                SET math_analiz=?, disk_math=?, algebra=?
                WHERE id=?;"""
        cursor = self.connection.cursor()
        cursor.execute(
            query,
            (
                user_in_db.math_analiz,
                user_in_db.disk_math,
                user_in_db.algebra,
                user_in_db.id,
            )
        )
        self.connection.commit()
        return user_in_db

    def delete_position_on_id(self, id: int) -> str:
        query = """
        DELETE FROM exam_2 WHERE id=?;"""
        cursor = self.connection.cursor()
        cursor.execute(query, str(id))
        return "Я была хорошей записью?"

    def get_vizit(self):
        query_visit = """
                SELECT math_analiz, disk_math, algebra 
                FROM exam_2;"""
        cursor = self.connection.cursor()
        visit = cursor.execute(query_visit)
        hours = Hours2Sem(connection_to_hours)
        dict_visit = {"math_analiz": [],
                      "disk_math": [],
                      "algebra": []}
        for item in visit:
            dict_visit["math_analiz"].append(item[0])
            dict_visit["disk_math"].append(item[1])
            dict_visit["algebra"].append(item[2])
        dict_hours = {}
        for item in hours.all_hours():
            if item[0] == "math_analiz":
                dict_hours["math_analiz"] = item[1]
            if item[0] == "disk_math":
                dict_hours["disk_math"] = item[1]
            if item[0] == "algebra":
                dict_hours["algebra"] = item[1]
        dict_visit["math_analiz"] = (dict_visit["math_analiz"].count(0) / (dict_hours["math_analiz"] / 4)) * 100
        dict_visit["disk_math"] = (dict_visit["disk_math"].count(0) / (dict_hours["disk_math"] / 4)) * 100
        dict_visit["algebra"] = (dict_visit["algebra"].count(0) / (dict_hours["algebra"] / 4)) * 100
        return dict_visit
