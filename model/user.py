from db import db 

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    account = db.Column(db.String(80))
    password = db.Column(db.String(80))
    username = db.Column(db.String(80))

    def __init__(self, account, password, username = None):
        self.account = account 
        self.password = password 
        self.username = username

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_account(cls, account):
        return cls.query.filter_by(account = account).first()

    @classmethod 
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()
    

