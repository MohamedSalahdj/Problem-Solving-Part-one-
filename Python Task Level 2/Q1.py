"""
Transform all names to uppercase using 
[normal list - list comprehension - functional programming]

"""
from module import Names, S

# 1- by using normal list
new_list = []
for name in Names:
    new_list.append(name.upper())
print(new_list)
print(S)

# 2- list comprehension
list_with_uppercase_name = [name.upper() for name in Names]
print(list_with_uppercase_name)
print(S)

#3-functional programming
list_with_uppercase = map(str.upper,new_list)
print(list(list_with_uppercase))