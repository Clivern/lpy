# 120. pass and Ellipsis
#
# pass is a no-op statement, a placeholder for a block. ... (Ellipsis) is a value, used in
# stubs, typing, and slicing. Both show up in unfinished APIs.
#
# Run: python 120_pass_ellipsis/main.py

def todo():
    pass

def stub() -> int:
    ...

print(todo(), stub(), ...)
