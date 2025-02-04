# 127. send on generators
#
# g.send(value) resumes the generator and makes yield evaluate to that value. The first
# resume must be send(None) or next(g).
#
# Run: python 127_send/main.py

def accumulator():
    total = 0
    while True:
        n = yield total
        if n is None:
            continue
        total += n

g = accumulator()
print(next(g))
print(g.send(5), g.send(7))
