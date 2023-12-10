# Задание №3
# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.


from typing import Optional, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

users = []


@app.get("/users/", response_model=List[User])
async def show_users():
    return users


@app.post("/users/")
async def add_user(user: User):
    users.append(user)
    return {"user": user, "status": "add"}


@app.put("/users/{user_id}", response_model=User)
async def update_item(user_id: int, user: User):
    for i, user_ in enumerate(users):
        if user_.id == user_id:
            users[i] = user
            return user
    return HTTPException(status_code=404, detail='User not found')


@app.delete("/users/{user_id}")
async def delete_item(user_id: int):
    for i, user_ in enumerate(users):
        if user_.id == user_id:
            users[i].status = 'False'
            return {"status": "delete"}
    return HTTPException(status_code=404, detail='User not found')
