from flask_restful import Resource, reqparse
from model.user import UserModel
from flask_jwt import jwt_required

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('account',
            type = str,
            required = True,
            help = 'This field cannot be blank'
            )
    parser.add_argument('password',
            type = str,
            required = True,
            help = 'This field cannot be blank'
            )
    parser.add_argument('username',
            type = str, 
            required = True,
            help = 'This field cannot be blank'
            )


    def post(self):        
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_account(data['account']) :
            return {"message" : "A user {username}  with account : {account} already exists".format(username = data['username'],
                                                                                                account  = data['account'])}, 400
        
        user = UserModel(data['account'], data['password'], data['username'])
        user.save_to_db()

        return {"message" : "A user {username}  with account : {account} create successful".format(username = data['username'],
                                                                                               account  = data['account'])}, 201

   
class UserChangeProfile(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('account',
            type = str,
            required = True,
            help = 'This field cannot be blank'
            )
    parser.add_argument('password',
            type = str,
            required = True,
            help = 'This field cannot be blank'
            )

    @jwt_required()
    def put(self):
        data = UserChangeProfile.parser.parse_args()
        user_post = UserModel(data['account'], data['password'])
        user_profile = UserModel.find_by_account(user_post.account)

        if user_profile:
            if user_profile.password == user_post.password:
                return {"message" : "Password is same as orignial"}
            else:
                user_profile.password = user_post.password
                user_profile.save_to_db()
                return {"message" : "password has beeb updated"}
        return {"message" : "That account do not exits"}





