# 403. pytest.raises
#
# pytest.raises(Exc) is a context manager. match= is a regex on the message. pytest.approx
# compares floats. xfail marks an expected fail.
#
# Run: python 403_pytest_raises/main.py

import pytest

def test_div():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_approx():
    assert 0.1 + 0.2 == pytest.approx(0.3)

if __name__ == "__main__":
    raise SystemExit(pytest.main(["-q", __file__, "--noconftest", "-p", "no:cacheprovider"]))
