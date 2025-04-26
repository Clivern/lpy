# 430. Faker
#
# Faker() generates fake names, emails, and text. seed_instance makes it repeatable.
# locale= switches language. Tests and demos use this instead of production dumps.
#
# Run: python 430_faker_data/main.py

from faker import Faker
fake = Faker()
fake.seed_instance(0)
print(fake.name(), "@" in fake.email())
print(len(fake.paragraph()) > 10)
