# 277. dis
#
# dis.dis prints bytecode. Useful when you wonder whether a comprehension allocates. The
# output is a teaching tool more than an API you call in apps.
#
# Run: python 277_dis_mod/main.py

import dis
def add(a, b):
    return a + b
print("BINARY" in dis.Bytecode(add).dis() or True)
print(list(dis.Bytecode(add))[0].opname)
