from faker import Faker
import json
import random

fake = Faker()

print(fake.name())
print(fake.country())
print(fake.email())

data_set = {"key1": [1, 2, 3], "key2": [4, 5, 6]}
json_dump = json.dumps(data_set)
print(json_dump)
