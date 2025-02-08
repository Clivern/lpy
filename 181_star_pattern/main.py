# 181. Star patterns
#
# case [first, *rest]: captures a sequence prefix. case {"k": v, **rest}: captures
# leftover mapping keys. Patterns can nest.
#
# Run: python 181_star_pattern/main.py

def head_tail(xs):
    match xs:
        case [head, *tail]:
            return head, tail
        case []:
            return None, []
        case _:
            return None, None

print(head_tail([1, 2, 3]), head_tail([]))
