# 431. Faker locales
#
# Faker("de_DE") generates German data. unique.email() avoids repeats. providers add
# domain methods. Keep seeds in tests.
#
# Run: python 431_faker_locale/main.py

from faker import Faker
fake = Faker("de_DE")
fake.seed_instance(1)
print(fake.country())
print(fake.unique.email() != fake.unique.email())
