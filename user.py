import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class User(Resource):
    TABLE_NAME = 'users'

    def __init__(self, _id = None, username = None, password = None):
        self.id = _id 
        self.username = username
        self.password = password


    parser = reqparse.RequestParser()
    parser.add_argument('password', 
            type = str,
            required = True,
            help = 'This field cannot be blank'
            )
    
    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item.__dict__
        return {'message' : 'No user'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username = ?".format(table = cls.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        
        if row:
            user = User(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = User(row[0], row[1], row[2])
        else:
            user = None
        
        connection.close()
        return user
    def put(self, name):
        if not self.find_by_name(name):
            return {'message' : "this user didn't register"}
        data = User.parser.parse_args()
        update_password = {'password' : data['password']}

        try:
            User.update(update_password, name)
        except:
            raise
            return {'message' : 'An error occured changing password'} 
        return update_password

    @classmethod
    def update(cls, update_item, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET password = ? WHERE username = ?".format(table = cls.TABLE_NAME)
        cursor.execute(query, (update_item['password'], name ))

        connection.commit()
        connection.close()

        

class UserRegister(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type = str,
            required = True,
            help = 'This field cannot be blank')

    parser.add_argument('password',
            type = str,
            required = True,
            help = 'This field cannot be blank')
    
    def post(self):
        data = UserRegister.parser.parse_args() 
        register_username = data['username']
        register_password = data['password']

        if User.find_by_name(register_username):
            return {'message' : 'user with that namealready exists'}, 404

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table = self.TABLE_NAME)
        cursor.execute(query, (register_username, register_password))

        connection.commit()
        connection.close()
        
        return {'message' : 'User {}create successful'.format(register_username)}


class UserList(Resource):
    TABLE_NAME = 'users'

    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM {table}".format(table = self.TABLE_NAME)
        result = cursor.execute(query)
        keys = [col[0] for col in result.description]
        users = []

        for row in result:
            d = dict(zip(keys, row))
            users.append(d)
        connection.close()

        return {'users' : users} 


























