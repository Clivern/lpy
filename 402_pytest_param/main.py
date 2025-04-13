# 402. pytest parametrize
#
# @pytest.mark.parametrize runs a test many times. ids= names cases. A failing case does
# not skip the rest. Combine with fixtures.
#
# Run: python 402_pytest_param/main.py

import pytest

@pytest.mark.parametrize("a,b,want", [(1, 1, 2), (2, 3, 5)])
def test_add(a, b, want):
    assert a + b == want

if __name__ == "__main__":
    raise SystemExit(pytest.main(["-q", __file__, "--noconftest", "-p", "no:cacheprovider"]))
