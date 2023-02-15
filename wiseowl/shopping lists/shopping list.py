import glob
import pandas as pd
import sys

path = '*.csv'


list_of_months = []
months_names = []

for file_name in glob.glob(path):
    # get name
    months_names.append(file_name[:-4])

    with open(file_name, 'r') as file:
        lines = file.read()
        lines = lines.splitlines()
    list_of_months.append(lines)


# Put months names and shopping lists together
for i in range(len(list_of_months)):
    list_of_months[i][0] = months_names[i]

print(list_of_months)
for i, month in enumerate(list_of_months):
    # month name:
    name = month[0]
    print(name)
    print('-' * len(name))
    # Iterate in each month
    for j in range(1, len(month)):
        date, store, spent = month[j].split(",")
        print(f"On {date} spent {spent} in {store}")
    print()


# WENT WITH THIS SOLUTION ---------
# current_month = []
# with open(file_name, 'r') as file:
#     lines = file.read()
#     lines = lines.splitlines()
#     current_month.append(lines)
# list_of_months.append(current_month)


# with open(file_name) as file:
#     data_frame = pd.read_csv(file)
#     current = data_frame.to_string(header=None, index=None)
#     list_of_months.append(current)