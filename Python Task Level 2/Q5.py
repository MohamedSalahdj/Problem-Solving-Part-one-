"""
Print a list contains the len of each word in the list using [normal list - list comprehension -
functional programming]
"""
from module import Names, S

#1- normal list
def get_length_of_each_word(names):
    new_list = []
    for name in names:
        new_list.append(len(name))
    return new_list

print(get_length_of_each_word(Names))
print(S)

# 2-list comprehension
length_of_each_name = [len(name) for name in Names]
print(length_of_each_name)
print(S)

# 3- functional programming
def get_length_of_each_name(name):
    return len(name)


new_l = list(map(get_length_of_each_name,Names))
print(new_l)