# 433. responses
#
# @responses.activate mocks requests. add(GET, url, json=, status=) stubs a call.
# assert_call_count checks usage. httpx needs respx or pytest-httpx.
#
# Run: python 433_responses_mock/main.py

import requests
import responses
@responses.activate
def run():
    responses.add(responses.GET, "https://api.example/x", json={"ok": True}, status=200)
    r = requests.get("https://api.example/x", timeout=1)
    print(r.json(), len(responses.calls))
run()
