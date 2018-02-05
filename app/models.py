from . import db

class User(db.model):
    __tablename__ = 'users'
    id = db.column(db.integer,primary_key = True)
    username = db.column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'


