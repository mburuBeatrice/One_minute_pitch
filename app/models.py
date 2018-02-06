from . import db

class Pitch:
    '''
    Pitch class to define Pitch Objects
    '''

    def __init__(self,id,title,pitch):
        self.id =id
        self.title = title
        self.pitch = pitch

class Comment:

    all_comments = []

    def __init__(self,id,title,comment):
        self.id = id
        self.title = title
        self.comment = comment
    @classmethod
    def get_comments(cls,id):

        response = []

        for comment in cls.all_comments:
            if comment.pitch_id == id:
                response.append(comment)

    def save_comments(self):
        Comment.all_comments.append(self)


    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear() 

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))


    def __repr__(self):
        return f'User {self.username}'


