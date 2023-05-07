from flask import Flask, render_template, request
import random
from dataclasses import dataclass


app = Flask(__name__)


@dataclass
class User:
    name: str
    language: str
    course: str = ''
    grade: int = 0


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        language = request.form['language']
        user = User(name, language)
        return render_template('course.html', user=user)
    return render_template('index.html')


@app.route('/course', methods=['POST'])
def course():
    user = User(request.form['name'], request.form['language'])
    course = request.form['course']
    if course not in ('base', 'pro'):
        return 'Invalid course selected'
    user.course = course
    return render_template('grade.html', user=user)


@app.route('/grade', methods=['POST'])
def grade():
    user = User(request.form['name'], request.form['language'], request.form['course'])
    user.grade = random.randint(0, 100)
    return render_template('result.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)