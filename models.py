import os
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy 

database_name = "century"
database_path ="postgresql://{}:{}@{}/{}".format('postgres', 'ghostman','localhost:5432', database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
    db.app = app
    db.init_app(app)
    db.create_all()


class Question(db.Model):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    answer = Column(String)
    category = Column(String)
    question = Column(String)
    difficulty = Column(Integer)

    def __init__(self, answer, category, difficulty, question):
        self.answer = answer
        self.question = question
        self.category = category
        self.difficulty = difficulty

    def insert(self):
        db.session_add(self)
        db.session_commit()

    def update(self):
        db.session_commit()

    def delete(self):
        db.session_delete(self)
        db.session_commit()

    def format(self):
        return {
            "id": self.id,
            "answer": self.answer,
            "question": self.question,
            "category": self.category,
            "difficulty": self.difficulty
        }
