from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


class Run(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    distance = db.Column(db.Float, nullable=False)
    pace = db.Column(db.Float, nullable=False)
    badge = db.Column(db.Boolean, default=False)


class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    distance = db.Column(db.Float, nullable=False)
    average_speed = db.Column(db.Float, nullable=False)
    climb = db.Column(db.Float, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    badge = db.Column(db.Boolean, default=False)


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    calories = db.Column(db.Integer, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/runs', methods=['POST'])
def add_run():
    data = request.get_json()
    new_run = Run(
        user_id=data['user_id'],
        distance=data['distance'],
        pace=data['pace'],
        badge=False  # Update badge logic as needed
    )
    db.session.add(new_run)
    db.session.commit()
    return jsonify({'message': 'Run added successfully'}), 201


@app.route('/api/rides', methods=['POST'])
def add_ride():
    data = request.get_json()
    new_ride = Ride(
        user_id=data['user_id'],
        distance=data['distance'],
        average_speed=data['average_speed'],
        climb=data['climb'],
        calories=data['calories'],
        badge=False  # Update badge logic as needed
    )
    db.session.add(new_ride)
    db.session.commit()
    return jsonify({'message': 'Ride added successfully'}), 201


@app.route('/api/foods', methods=['POST'])
def add_food():
    data = request.get_json()
    new_food = Food(
        user_id=data['user_id'],
        calories=data['calories']
    )
    db.session.add(new_food)
    db.session.commit()
    return jsonify({'message': 'Food added successfully'}), 201


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)