from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username, password):
    user = User.find_by_name(username)
    if user and safe_str_cmp(user['password'], password):
        userC = User()
        userC.id = user['id']
        userC.username = user['username']
        userC.password = user['password']
        return userC

def identity(payload):
    user_id = payload['identity']
    print(user_id)
    return User.find_by_id(user_id)


