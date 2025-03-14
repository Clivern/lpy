# 287. doctest
#
# doctest runs examples in docstrings. A line starting with >>> is a call; the next line
# is the expected repr. Good for small functions; pytest for apps.
#
# Run: python 287_doctest/main.py

def add(a, b):
    """
    >>> add(2, 3)
    5
    """
    return a + b
import doctest
print(doctest.testmod(verbose=False).failed)
