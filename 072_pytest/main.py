# 072. pytest and Hypothesis
#
# assert, fixtures, parametrize, raises, approx, and property tests.
#
# Run: python 072_pytest/main.py

# --- pytest basic ---
import pytest

def inc(n):
    return n + 1

def test_inc():
    assert inc(1) == 2

# --- pytest fixture ---
import pytest

@pytest.fixture
def sample():
    return {"n": 1}

def test_sample(sample):
    assert sample["n"] == 1

# --- pytest param ---
import pytest

@pytest.mark.parametrize("a,b,want", [(1, 1, 2), (2, 3, 5)])
def test_add(a, b, want):
    assert a + b == want

# --- pytest raises ---
import pytest

def test_div():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_approx():
    assert 0.1 + 0.2 == pytest.approx(0.3)

# --- pytest approx ---
import pytest
assert [0.1 + 0.2] == pytest.approx([0.3])
print("ok")

# --- hypothesis intro ---
from hypothesis import given, strategies as st, settings
@settings(max_examples=20)
@given(st.integers(), st.integers())
def test_add_commutes(a, b):
    assert a + b == b + a
test_add_commutes()
print("ok")

if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main(["-q", __file__, "--noconftest", "-p", "no:cacheprovider"]))
