"""
Get the names that starts with ‘t’ in a list using [normal list - list comprehension - functional
programming
"""
from module import Names, S


# 1- normal list
#first solution 
def name_start_with_t(names):
    new_l = []
    for i in range(len(names)):
        if names[i][0] == 't': 
            new_l.append(names[i])
    return new_l

print(name_start_with_t(Names))
print(S)

#Second solution 
def name_start_with_t_2(names):
    new_l = []
    for name in names:
        if name.startswith('t'):
            new_l.append(name)
    return new_l

print(name_start_with_t_2(Names))
print(S)


# 3-list comprehension
new_list_includes_names_start_With_t = [name for name in Names if name.startswith('t')]
print(new_list_includes_names_start_With_t)
print(S)

#3-functional programming
def name_start_with_t(name):
    if name[0] == 't': 
        return name

new_list_includes_names_start_With_t = list(filter(name_start_with_t, Names))
print(new_list_includes_names_start_With_t)