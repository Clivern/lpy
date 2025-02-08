# 149. else on try
#
# try/else runs the else suite when no exception was raised. It keeps the success path out
# of try so you do not catch errors from it.
#
# Run: python 149_else_try/main.py

def load(s):
    try:
        n = int(s)
    except ValueError:
        print("bad")
    else:
        print("got", n)

load("4")
load("x")
