import bcrypt


def hash_password(passw):
    hashed_password = bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt())
    return hashed_password


def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

# hashed = hash_password('hello456699')
