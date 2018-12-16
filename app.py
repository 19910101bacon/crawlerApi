from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from user import User, UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
app.config['JWT_AUTH_URL_RULE'] = '/login'
api = Api(app)

jwt = JWT(app, authenticate, identity)

#api.add_resource(Crawler, '/crawler/<string:name>')
api.add_resource(User, '/user/<string:name>')
#api.add_resource(Article, '/item/<string:name>/article')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port = 5000, debug = True)

