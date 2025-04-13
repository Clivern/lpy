# 401. pytest fixtures
#
# @pytest.fixture injects setup. yield is teardown. scope= can be function, class, module,
# session. Fixtures compose by requesting others.
#
# Run: python 401_pytest_fixture/main.py

import pytest

@pytest.fixture
def sample():
    return {"n": 1}

def test_sample(sample):
    assert sample["n"] == 1

if __name__ == "__main__":
    raise SystemExit(pytest.main(["-q", __file__, "--noconftest", "-p", "no:cacheprovider"]))
