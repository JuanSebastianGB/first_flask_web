#!/usr/bin/env python3
from flask import Flask, render_template
from flask.templating import render_template
app = Flask(__name__)


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


@app.route('/student/<name>')
def student(name):
    data = {
        'title': 'Student',
        'name': name
    }
    return render_template('student.html', data=data)


if __name__ == "__main__":
    """[Main function to run the application]
    """
    app.run(debug=True, port=5001)
