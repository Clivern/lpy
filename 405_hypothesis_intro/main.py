# 405. Hypothesis
#
# @given(st.integers()) generates examples. find() searches for a counterexample. Database
# shrinks failing cases. Property tests sit next to examples.
#
# Run: python 405_hypothesis_intro/main.py

from hypothesis import given, strategies as st, settings
@settings(max_examples=20)
@given(st.integers(), st.integers())
def test_add_commutes(a, b):
    assert a + b == b + a
test_add_commutes()
print("ok")
