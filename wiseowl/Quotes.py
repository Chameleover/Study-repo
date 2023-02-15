
# some quotations
great_quotes = (
    "And we danced, on the brink of an unknown future, to an echo from a vanished past. (John Wyndham) \n" + \
    "Life is what happens to you while you're busy making other plans. (wrongly attributed to John Lennon)\n" + \
    "You cannot overestimate the unimportance of practically everything. (John Maxwell)"
)

print(great_quotes)


def split_quotations(text:str):
    text = text.splitlines()
    return text


def get_words(quote_text):
    quote_list = quote_text.split(" ")
    return quote_list


def count_words(list_of_words):
    return len(list_of_words)


def longest_word(list_of_words):
    return max(list_of_words, key=len).upper()


first, second, last = split_quotations(great_quotes)
print("First Quotation stats:")
first = get_words(first)
print(count_words(first))
print(longest_word(first))

print("Second Quotation stats:")
second = get_words(second)
print(count_words(second))
print(longest_word(second))

print("Third Quotation stats:")
last = get_words(last)
print(count_words(last))
print(longest_word(last))