result = dict()


def read_file(filename):

    file = open(filename)
    for line in file:
        line = line.strip('\n')
        list = line.split(',')
        result[list[0]] = float(list[3])*100


read_file('resource-data/county_data.csv')
print(result)