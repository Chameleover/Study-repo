house = input("Which house are you in? ").lower()
color = ''
if house == 'gryffindor':
    color = 'Scarlet and yellow, of'
elif house == 'hufflepuff':
    color = 'Yellow and black'
elif house == 'ravenclaw':
    color = 'Blue and bronze'
elif house == 'slytherin':
    color = 'Green and silver(ssss)'
else:
    color = 'Not known'

print("Your house colours are...\n")
print(color)