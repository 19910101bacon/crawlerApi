from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resource.user import UserRegister, UserChangeProfile
from resource.crawler import Crawler
from resource.item import Item
#from resource.article import Article
from security import authenciate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URL'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_AUTH_USERNAME_KEY'] = 'account'
app.secret_key = 'secretkey'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenciate, identity)

api.add_resource(UserRegister, '/register')
api.add_resource(UserChangeProfile, '/profile')
api.add_resource(Crawler, '/crawler')
api.add_resource(Item, '/item')
#api.add_resource(Article, '/item/<string:item_name>/<int:id>')



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug = True)
