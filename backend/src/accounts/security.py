import bcrypt


def hash_password(password: str) -> bytes:
    pw = bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt).decode()


def check_password(password: str, password_in_db: str) -> bool:
    return bcrypt.checkpw(password.encode(), password_in_db.encode())
