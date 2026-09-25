def convert_string_to_list(words):
    return list(map(list, words))

words =  ['Day', 'Month', 'Year']
print("Convert to list of lists:", convert_string_to_list(words))