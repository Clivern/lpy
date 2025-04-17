# 410. tenacity wait
#
# wait_exponential backs off. retry_if_result retries on a bad return. before_sleep logs.
# Use this around HTTP, not around CPU work.
#
# Run: python 410_tenacity_wait/main.py

from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_result
@retry(stop=stop_after_attempt(3), wait=wait_fixed(0), retry=retry_if_result(lambda r: r is None))
def probe():
    probe.i = getattr(probe, "i", 0) + 1
    return "ok" if probe.i >= 2 else None
print(probe())
