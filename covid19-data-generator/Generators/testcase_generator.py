from faker import Faker
import random
from Utils.constants import *

counter = 0
# generate one test case for each user
# _id f"tscid{counter_tsc:08n}", UserID, Result, TestCenterID, TestDate
def generate_testcase(today, users, writer, fieldnames):
    global counter
    positive_rate_today = positive_rate.get(today)
    positive_weights = (positive_rate_today, 100 - positive_rate_today)

    for curtUser in users:
        counter += 1

        # _id
        _id = f"tsc{counter:08n}"

        # UserID
        UserID = curtUser.get('_id')

        # Result
        Result = random.choices(medical_status_list, weights=positive_weights, k=1)[0]

        # TestCenterID
        TestCenterID = random.choice(medical_center_id_list)

        # TestDate
        TestDate = "2020/"+today

        curt_tsc = {}
        for variables in fieldnames:
            curt_tsc[variables] = eval(variables)

        writer.writerow(curt_tsc)

