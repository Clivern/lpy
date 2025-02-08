# 148. finally
#
# finally runs on the way out of try, whether it returned, raised, or broke. Use it for
# cleanup that must happen. with is often clearer.
#
# Run: python 148_finally/main.py

def work(ok):
    try:
        if not ok:
            raise RuntimeError("no")
        return "ok"
    finally:
        print("cleanup")

print(work(True))
try:
    work(False)
except RuntimeError:
    print("caught")
