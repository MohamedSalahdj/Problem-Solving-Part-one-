"""
4. Get the names that contains 2 or more ‘a’ letter using [normal list - list comprehension - functional
programming]
"""
from module import Names, S

# 1- normal list
def get_names_contain_more_than_two_a(names):
    l =[]
    for name in names:
        if name.count('a') >= 2:
            l.append(name)
    return l    

print(get_names_contain_more_than_two_a(Names))
print(S)

#2- list comprehension
new_l = [name for name in Names if name.count('a') >= 2]
print(new_l)
print(S)

#3- functional programming
def get_names_contain_more_than_two(name):
    if name.count('a') >= 2:
        return name

new_l = filter(get_names_contain_more_than_two, Names)
print(list(new_l))
