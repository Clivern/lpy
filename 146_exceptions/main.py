# 146. try and except
#
# try runs a suite. except Type catches matching errors. except Exception as e binds the
# instance. Bare except: catches BaseException and is too wide.
#
# Run: python 146_exceptions/main.py

def parse(s):
    try:
        return int(s)
    except ValueError as e:
        print(type(e).__name__, e)
        return None

print(parse("3"), parse("no"))
