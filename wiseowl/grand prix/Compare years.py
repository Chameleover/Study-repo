
# path where files are stored (you'll need to change this)
file_path = ''

# read first file into a list
with open(file_path + "Grand Prix 2016.csv", 'r') as gp_2016:

    # read all lines into list
    grand_prix_2016 = [line.split(",")[1] for line in gp_2016.read().splitlines()]

# read second file into a list
with open(file_path + "Grand Prix 2017.csv", 'r') as gp_2017:

    # read all lines into list
    grand_prix_2017 = [line.split(",")[1] for line in gp_2017.read().splitlines()]

# show results so far
print(grand_prix_2016)
print(grand_prix_2017)

