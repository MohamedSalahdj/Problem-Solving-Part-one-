"""
2. Get the names that contains ‘a’ in a list using [normal list - list comprehension - functional
programming]
"""
from module import Names, S


# 1- normal list
new_list = []
for name in Names:
    if 'a' in name:
       new_list.append(name)
print(new_list)
print(S)

# 2- list comprehension
list_contain_names_include_a = [name for name in Names if 'a' in name]
print(list_contain_names_include_a)
print(S)


# 3-functional programming
def name_with_a(name):
    if 'a' in name:
        return name
new_list = filter(name_with_a, Names)
print(list(new_list))