# 400. pytest basics
#
# test_ functions are collected. assert is rewritten with introspection. This lesson runs
# a tiny test file via pytest.main. Match the filename test_*.py in real trees.
#
# Run: python 400_pytest_basic/main.py

import pytest

def inc(n):
    return n + 1

def test_inc():
    assert inc(1) == 2

if __name__ == "__main__":
    raise SystemExit(pytest.main(["-q", __file__, "--noconftest", "-p", "no:cacheprovider"]))
