# 150. Custom exceptions
#
# Subclass Exception (not BaseException). Put domain errors in a small hierarchy so
# callers can catch a parent. Keep the constructor compatible with str(e).
#
# Run: python 150_custom_exc/main.py

class NotFound(Exception):
    pass

class UserNotFound(NotFound):
    def __init__(self, user_id):
        super().__init__(f"user {user_id} missing")
        self.user_id = user_id

try:
    raise UserNotFound(9)
except NotFound as e:
    print(e, e.user_id)
