
from flask import Flask, render_template

app = Flask(__name__)

name = 'FJ'
movies = [
    {'title': 'list1', 'year': '2021-04-13'},
    {'title': 'list2', 'year': '1989'},
    {'title': 'list3', 'year': '1993'},
    {'title': 'list4', 'year': '1994'},
    {'title': 'list5', 'year': '1996'},

]


@app.route('/')
def index():		
    return render_template('index.html', name=name, movies=movies)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
