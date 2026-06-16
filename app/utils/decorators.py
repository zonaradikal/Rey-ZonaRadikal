from functools import wraps
from flask import session, abort

def admin_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not session.get("user_id"):
            abort(401)

        if session.get("role") != "admin":
            abort(403)

        return func(*args, **kwargs)

    return wrapper