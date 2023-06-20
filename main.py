import uvicorn
import fastapi
import sqlite3

from Hours import Hours2Sem
from db import User
from moduls import UserExam2, UserToUpdateExam2
from Tables import setup_db

app = fastapi.FastAPI()
connection_to_objects = sqlite3.connect('semester2.sqlite', check_same_thread=False)
connection_to_hours = sqlite3.connect('hours2.sqlite', check_same_thread=False)
user = User(connection_to_objects)
hours = Hours2Sem(connection_to_hours)


@app.post('/create_position', status_code=201)
def create_position(item: UserExam2):
    return user.create(item)


@app.get('/get_by_date/{id}', status_code=200)
def get_by_date(id: int):
    return user.get_by_position(id)


@app.get('/all_position', status_code=200)
def get_all():
    return user.all_position()


@app.put('/update_position', status_code=204)
def update_position(item: UserToUpdateExam2):
    return user.update_position(item)


@app.delete('/delete_position/{date}', status_code=203)
def delete_position(id: int):
    return user.delete_position_on_id(id)


@app.get('/get_visit')
def get_visit():
    return user.get_vizit()


@app.get('/count_hours_sem2', status_code=200)
def all_hour():
    return hours.count_hours_sem2()


if __name__ == "__main__":
    setup_db(connection_to_objects)
    setup_db(connection_to_hours)
    uvicorn.run(app, host='localhost', port=5000)
