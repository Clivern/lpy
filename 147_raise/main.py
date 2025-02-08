# 147. raise
#
# raise Exception("msg") throws. raise without an argument re-raises the current
# exception. raise New from old sets __cause__.
#
# Run: python 147_raise/main.py

def must_positive(n):
    if n <= 0:
        raise ValueError("n must be > 0")
    return n

try:
    must_positive(-1)
except ValueError as e:
    print(e)
