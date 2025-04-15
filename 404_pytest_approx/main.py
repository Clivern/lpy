# 404. pytest approx recap
#
# approx(rel=..., abs=...) sets tolerance. It compares sequences too. Use it instead of
# round() in numeric tests.
#
# Run: python 404_pytest_approx/main.py

import pytest
assert [0.1 + 0.2] == pytest.approx([0.3])
print("ok")
