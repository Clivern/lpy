# 409. tenacity retry
#
# @retry retries a function on exception. stop_after_attempt caps tries. wait_fixed sleeps
# between. reraise=True keeps the last error.
#
# Run: python 409_tenacity_retry/main.py

from tenacity import retry, stop_after_attempt, retry_if_exception_type
box = {"n": 0}
@retry(stop=stop_after_attempt(3), retry=retry_if_exception_type(ValueError), reraise=True)
def flaky():
    box["n"] += 1
    if box["n"] < 3:
        raise ValueError("again")
    return "ok"
print(flaky(), box["n"])
