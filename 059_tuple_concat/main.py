# 059. Tuple concatenation
#
# + and * build new tuples. A trailing comma makes a one-tuple. t += (x,) rebinds t when t
# is a local name; it does not mutate the old tuple.
#
# Run: python 059_tuple_concat/main.py

t = (1, 2)
print(t + (3,), t * 2)
u = t
t += (3,)
print(t, u)
print((1,) == (1))
