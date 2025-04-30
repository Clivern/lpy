# 080. Test helpers
#
# Faker, freeze_time, and responses.
#
# Run: python 080_test_libs/main.py

# --- faker data ---
from faker import Faker
fake = Faker()
fake.seed_instance(0)
print(fake.name(), "@" in fake.email())
print(len(fake.paragraph()) > 10)

# --- faker locale ---
from faker import Faker
fake = Faker("de_DE")
fake.seed_instance(1)
print(fake.country())
print(fake.unique.email() != fake.unique.email())

# --- freezegun time ---
from datetime import datetime, timezone
from freezegun import freeze_time
with freeze_time("2025-01-15 12:00:00", tz_offset=0):
    print(datetime.now(timezone.utc).date())

# --- responses mock ---
import requests
import responses
@responses.activate
def run():
    responses.add(responses.GET, "https://api.example/x", json={"ok": True}, status=200)
    r = requests.get("https://api.example/x", timeout=1)
    print(r.json(), len(responses.calls))
run()
