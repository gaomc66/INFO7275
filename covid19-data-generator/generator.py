# from faker import Faker
# import json
# import random
#
# fake = Faker()
#
# print(fake.name())
# print(fake.country())
# print(fake.email())
#
# data_set = {"key1": [1, 2, 3], "key2": [4, 5, 6]}
# json_dump = json.dumps(data_set)
# print(json_dump)

# generate test
import csv
import random
from faker import Faker
from datetime import datetime

l = Faker('en_GB')
# f = open("./generated-data/test.csv", "r")
# k = csv.reader(f)

g = open("./generated-data/test.csv", "a")
w = csv.writer(g)
w.writerow(('id', 'name', 'address', 'college', 'company', 'dob', 'age'))
for i in range(10):
    w.writerow((i + 1, l.name(), l.address(), random.choice(['psg', 'sona', 'amirta', 'anna university']),
                random.choice(['CTS', 'INFY', 'HTC']),
                (random.randrange(1950, 1995, 1), random.randrange(1, 13, 1), random.randrange(1, 32, 1)),
                random.choice(range(0, 100))))
# f.close()
