# models.py
import flask_sqlalchemy,app
import os

# app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://proj2_user:project2handin1@localhost/postgres'  
db = flask_sqlalchemy.SQLAlchemy(app.app)
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True) # key
    img = db.Column(db.String(150))
    fbID = db.Column(db.String(150))
    user = db.Column(db.String(120))
    chat = db.Column(db.Text)
    def __init__(self, i, f, u, c):
        self.img = i
        self.fbID = f
        self.user = u
        self.chat = c
    def __repr__(self): # what's __repr__?
        return '<Message chat: %s>' % self.chat

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True) # key
    img = db.Column(db.String(150))
    fbID = db.Column(db.String(150))
    user = db.Column(db.String(120))
    def __init__(self, i, f, u):
        self.img = i
        self.fbID = f
        self.user = u
    def __repr__(self): # what's __repr__?
        return '<Users name: %s>' % self.user