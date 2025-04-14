
from database import insert_users, get_user
from werkzeug.security import generate_password_hash, check_password_hash

def signup_user(email,passwordToHash):
    hashedPassword = generate_password_hash(passwordToHash)
    insert_users(email,hashedPassword)
    
def verify_login(email, password):
    passwordHash = get_user(email)
    
    if check_password_hash(passwordHash,password):
        return True
    else:
        return False
    