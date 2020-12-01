from faker import Faker
import csv
from Utils.constants import *
from Generators import testcase_generator, user_generator

fake = Faker()

counter_user = 0

generate_user = user_generator.generate_user
generate_testcase = testcase_generator.generate_testcase

def generator():

    # open Users.csv
    user_file = open("./generated-data/Users.csv", "w")
    user_fieldnames = ['FirstName', 'LastName', 'Gender', 'County', 'AgeGroup_ID', '_id']
    user_writer = csv.DictWriter(user_file, fieldnames=user_fieldnames)
    user_writer.writeheader()

    # Open TestCases.csv
    tsc_file = open("./generated-data/TestCases.csv", "w")
    tsc_fieldnames = ['UserID', 'Result', 'TestCenterID', 'TestDate', '_id']
    tsc_writer = csv.DictWriter(tsc_file, fieldnames=tsc_fieldnames)
    tsc_writer.writeheader()

    # Open TestCases.csv
    mdc_file = open("./generated-data/MedicalStatus.csv", "w")
    mdc_fieldnames = ['UserID', 'MedicalCenterID', 'StatusID', '_id']
    mdc_writer = csv.DictWriter(mdc_file, fieldnames=mdc_fieldnames)
    mdc_writer.writeheader()

    # generate by date
    for i, date in enumerate(date_range):
        users_today = generate_user(i, date, user_writer, user_fieldnames)
        # print(user_today)
        generate_testcase(date, users_today, tsc_writer, tsc_fieldnames, mdc_writer, mdc_fieldnames)

    user_file.close()
    tsc_file.close()
    mdc_file.close()


if __name__ == '__main__':
    generator()
