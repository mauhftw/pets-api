from werkzeug.security import safe_str_cmp
from models.user import User
import database


users = User.all()
username_table = {user.email: user for user in users}
userid_table = {user.id: user for user in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


