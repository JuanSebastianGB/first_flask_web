#!/usr/bin/env python3
from flask import Flask, url_for
from flask.globals import request
from flask.templating import render_template
from werkzeug.utils import redirect
app = Flask(__name__)


@app.before_request
def before_request():
    """[Testing code to use before a request]
    """
    print("before of the request")


@app.after_request
def after_request(response):
    """[Testing code to use after the request]
    """

    print("After the request")
    return response


@app.route('/')
def index():
    """[View of the intex of the created page]

    Returns:
        [str]: [This return a msj]
    """
    # return "<h1>Hellow world!!!!</h1>"
    students = ['Juan', 'Amaya', 'Andres', 'Lisa']
    #students = []
    data = {
        'title': 'First Flask app',
        'msj': 'Be welcome to this new app',
        'students': students,
        'nro_students': len(students)
    }
    return render_template("index.html", data=data)


@app.route('/student/<name>/<int:age>')
def student(name, age):
    """[Student class, just for testing]

    Args:
        name ([str]): [Name of the student]
        name ([int]): [Age of the student]

    Returns:
        [Template]: [Rendered student's template to show]
    """
    data = {
        'title': 'Student',
        'name': name,
        'age': age
    }
    return render_template('student.html', data=data)


def query_string():
    """[Implementing query string, to handle dinamic inputs]
    """
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "ok"


def page_not_found(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))


if __name__ == "__main__":
    """[Main function to run the application]
    """
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, port=5001)
