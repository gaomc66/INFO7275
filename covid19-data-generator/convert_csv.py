result = dict()

file = open('positive_data.csv')

for line in file:
    line = line.strip('\n')
    (key, val) = line.split(',')
    result[key] = int(val)

print(result)