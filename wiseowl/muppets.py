with open('Muppets.csv', 'r') as file:
    lines = file.read()
    lines = lines.splitlines()
    list_of_muppets = []
    for line in lines:
        current = line.split(',')
        list_of_muppets.append(current)

for muppet in list_of_muppets:
    muppet, animal, colour = muppet
    print(f'{muppet} ({colour} {animal})')
