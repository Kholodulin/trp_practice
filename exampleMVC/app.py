from flask import Flask, render_template
from models import Car

app = Flask(__name__)

@app.route('/')
def index():
    cars = [
        Car("Toyota", 2020, "Blue"),
        Car("Lada", 2010, "White"),
        Car("Ford", 2015, "Black"),
    ]
    return render_template('index.html', cars=cars)

if __name__ == '__main__':
    app.run()