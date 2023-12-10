# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.
from flask import Flask, render_template
from pydantic import BaseModel



app = Flask(__name__)

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

users = []

@app.route("/users/")
def show_users():
    context = {'title': 'Users',
               'users': users}
    return render_template('users.html', **context)

if __name__ == '__main__':
    app.run(debug=True)