import random
import csv
from Utils.constants import *
import datetime

counter = 0


# _id, UserID, MedicalCenterID, StatusID, Date
def generate_medical_report(today, positive_user, writer, fieldnames):
    global counter
    counter += 1
    medical_center_weights = tuple(medical_center_weight.values())
    death_weight = int(death_list.get(today) / positive_num.get(today) * 100)
    unknown_weight = 50 - death_weight

    # _id
    _id = f"mcrid{counter:08n}"

    # UserID
    UserID = positive_user.get('_id')

    # MedicalCenterID
    MedicalCenterID = random.choices(medical_center_id_list, weights=medical_center_weights, k=1)[0]

    # StatusID
    if positive_user.get('AgeGroup_ID') in ('agid02', 'agid03', 'agid04'):
        StatusID = random.choices(medical_status_list, weights=(78, 21.8, 0.2), k=1)[0]
    else:
        StatusID = random.choices(medical_status_list, weights=(50, unknown_weight, death_weight), k=1)[0]

    today_str = "2020/" + today
    Date = datetime.datetime.strptime(today_str, "%Y/%m/%d")

    curt_medical_status = {}
    for variables in fieldnames:
        curt_medical_status[variables] = eval(variables)
    print(fieldnames)
    print(curt_medical_status)
    writer.writerow(curt_medical_status)
