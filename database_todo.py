from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///To_Do_List4.spqlite3'
app.config['SECRET_KEY'] = 'random string'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column('User_id',db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(20))

    def __init__( self,username,password):
        self.username = username
        self.password = password


class Task(db.Model):
    id = db.Column('Task_id',db.Integer, primary_key=True)
    Task_event = db.Column(db.String(100))
    date = db.Column(db.String(20))

    def __init__(self,Task_event,date):
        self.Task_event = Task_event
        self.date = date



class Completed_task(db.Model):
    id = db.Column('Task_id',db.Integer, primary_key=True)
    Task_event = db.Column(db.String(100))
    date = db.Column(db.String(20))

    def __init__(self,Task_event,date):
        self.Task_event = Task_event
        self.date = date
