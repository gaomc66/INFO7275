import pandas as pd
from pandas.io.pytables import DataCol

result = dict()
def read_file(filename):

    file = open(filename)
    for line in file:
        line = line.strip('\n')
        list = line.split(',')
        result[list[0]] = float(list[3])*100


# read_file('resource-data/county_data.csv')
# print(result)

def csv_to_json(filename, distinationfile):
    print(f"filename {filename}")
    print(f"distinationfile {distinationfile}")
    csv_data = pd.read_csv(filename)
    # ,lines=True
    csv_data.to_json(path_or_buf = distinationfile, orient='records')        
    return csv_data


