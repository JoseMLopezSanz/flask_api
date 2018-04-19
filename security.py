from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password): #In some versions of python is not good to compare
                                                       #stringfs because of encoding problems
        return user

def identity(payload):
    user_id = payload["identity"]
    return UserModel.find_by_id(user_id)
