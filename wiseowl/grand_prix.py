path = './grand prix/'

# Open Grand Prix 2016
with open(path + 'Grand Prix 2016.csv') as file:
    grand_2016 = file.read()
    grand_2016 = grand_2016.splitlines()
    grand_2016_no_index = []
    for line in grand_2016:
        line = line.split(',')
        grand_2016_no_index.append(line[1])

    grand_2016_set = set(grand_2016_no_index)


with open(path + 'Grand Prix 2017.csv', 'r') as file:
    grand_2017 = file.read()
    grand_2017 = grand_2017.splitlines()
    grand_2017_no_index = []
    for line in grand_2017:
        line = line.split(',')
        grand_2017_no_index.append(line[1])
    grand_2017_set = set(grand_2017_no_index)

# compare
compare = grand_2016_set.difference(grand_2017_set)
for prix in compare:
    print(f'{prix} is in 2016 only')

compare = grand_2017_set.difference(grand_2016_set)
for prix in compare:
    print(f'{prix} is in 2017 only')