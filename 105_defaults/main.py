# 105. Default arguments
#
# A default is evaluated once, at def time. Never use a mutable default: the same list is
# reused. Use None and create inside instead.
#
# Run: python 105_defaults/main.py

def append_one(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(append_one(1))
print(append_one(2))
print(append_one(3, [0]))
