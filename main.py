from flask import Flask, render_template
from datetime import datetime
from pm25 import get_pm25
import json
app = Flask(__name__)
books = {
    1: 'Python',
    2: 'Java',
    3: 'C++'
}


@app.route('/pm25-charts')
def pm25_charts():
    return render_template('pm25_chart.html')


@app.route('/pm25-data', methods=['GET'])
def pm25_data():
    columns, values = get_pm25()
    site = [value[0] for value in values]
    pm25 = [value[2] for value in values]
    datetime = values[0][-2]
    # get highest & lowest data
    sorted_data = sorted(values, key=lambda x: x[2])

    lowest_data = {'site': sorted_data[0][0], 'pm25': sorted_data[0][2]}
    highest_data = {'site': sorted_data[-1][0], 'pm25': sorted_data[-1][2]}
    result = json.dumps({
        'site': site,
        'pm25': pm25,
        'datetime': datetime,
        'lowest': lowest_data,
        'hightest': highest_data
    }, ensure_ascii=False)
    return result


@app.route("/sum/x=<a>&y=<b>")
def get_sum(a, b):
    try:
        return f'總和為:{eval(a)+eval(b)}'
    except Exception as e:
        print(e)
        return 'Incorrect numbers'


@app.route('/')
def index():
    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    return render_template('index.html', time=now, name='Eric')


@app.route('/books')
def book():

    books = {
        1: {
            "name": "Python book",
            "price": 299,
            "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348"
        },

        2: {

            "name": "Java book",
            "price": 399,
            "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348"
        },

        3: {
            "name": "C# book",
            "price": 499,
            "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348"
        }}
    for id in books:
        print(books[id]['name'], books[id]['price'])

    return render_template('books.html', books=books)


@app.route('/books/<int:id>')
def get_books(id):
    try:

        return books[id]
    except Exception as e:
        print(e)
        return 'Wrong Number'


@app.route('/pm25')
def pm25_table():
    columns, values = get_pm25()
    return render_template('pm25.html', columns=columns, values=values)


app.run(debug=True)
