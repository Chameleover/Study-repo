
# Julius Caesar Act 4, Scene 3, 218–224
brutus_speech = "There is a tide in the affairs of men \nWhich, taken at the flood, leads on to fortune; \nOmitted, all the voyage of their life \nIs bound in shallows and in miseries. \nOn such a full sea are we now afloat, \nAnd we must take the current when it serves, \nOr lose our ventures."

# print out the text of this speech
print(brutus_speech)

list_of_words = brutus_speech.split(" ")
list_of_formatted_words = []

for word in list_of_words:
    word = word.replace(",", "")
    word = word.replace(".", "")
    word = word.replace(";", "")
    word = word.replace("\n", "")
    word = word.lower()
    list_of_formatted_words.append(word)

print(f'Number of words = {len(list_of_formatted_words)}\n')

for num in range(29):

    number_words = len([x for x in list_of_formatted_words if len(x) == num])
    if number_words:
        print(f'{num}-letter words = {number_words}')