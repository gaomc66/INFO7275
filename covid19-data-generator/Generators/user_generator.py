from faker import Faker
import random
from Utils.constants import *

fake = Faker()

counter_user = 0

# _id(f"{usrid:08n}"), FirstName, LastName, Gender, County, AgeGroup_ID
def generate_user(i, today, writer, fieldnames):
    pos_num_today = int(positive_num.get(today) / 10)
    total_num_today = pos_num_today / (positive_rate.get(today)/100)
    county_names = list(county_weight.keys())
    county_weights = tuple(county_weight.values())
    age_group_names = list(age_group_id_list)
    age_group_weights = tuple(age_weight.get(int(8 / 7)).values())

    today_usr = []

    for i in range(int(total_num_today)):
        global counter_user
        counter_user += 1

        # _id
        _id = f"usrid{counter_user:08n}"

        # FirstName, LastName
        FirstName = fake.name().split(' ')[0]
        LastName = fake.name().split(' ')[1]

        # Gender
        Gender = random.choices(gender_list, weights=None, k=1)[0]

        # County
        County = random.choices(county_names, weights=county_weights, k=1)[0]

        # AgeGroup
        AgeGroup_ID = random.choices(age_group_names, weights=age_group_weights, k=1)[0]

        curt_usr = {}
        for variables in fieldnames:
            curt_usr[variables] = eval(variables)

        today_usr.append(curt_usr)
        writer.writerow(curt_usr)

    return today_usr
