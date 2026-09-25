# Original list of dictionaries :
original_list = [
    {'make': ' Google ', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Sorting the List of dictionaries :
sorted_list = sorted(original_list, key = lambda i: i['color'])
print("Sorted list:", sorted_list)