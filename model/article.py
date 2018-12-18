from db import db
from sqlalchemy.orm import load_only

class ArticleModel(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    item = db.Column(db.String(80))
    source = db.Column(db.String(80))
    content = db.Column(db.String)
    date = db.Column(db.String(80))

    def __init__(self, title, item, source, date, content):
        self.title = title
        self.item = item 
        self.source = source
        self.date = date
        self.content = content

    def save_to_data(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all_item(cls):
        all_item = cls.query.options(load_only("item"))
        return list(set([ x.item for x in all_item ]))

    
