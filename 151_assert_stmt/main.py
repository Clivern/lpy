# 151. assert
#
# assert cond, msg raises AssertionError when cond is false. python -O strips asserts. Do
# not use them for input checks that must always run.
#
# Run: python 151_assert_stmt/main.py

def area(w, h):
    assert w > 0 and h > 0, "sizes must be positive"
    return w * h

print(area(3, 4))
try:
    area(0, 2)
except AssertionError as e:
    print(e)
