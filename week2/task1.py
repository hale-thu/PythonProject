def get_last_element(lst):
    return lst[-1]

def sort_list(lst):
    return sorted(lst, key=get_last_element)

sample_tuple = [(2,5), (1,2), (4,4), (2,3), (2,1)]
print(sort_list(sample_tuple))
