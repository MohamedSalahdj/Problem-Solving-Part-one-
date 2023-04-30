#     Unpack the list in

from module import Names, S

# Q7. a,b , a= the first index , b = rest of the list
a = Names[0] 
b = Names[1:]
print(a)
print(b)
print(S)
a, *b =Names 
print(a)
print(b)
print(S)

#8. a = the first index , b = the last index
a = Names[0]
b= Names[-1]
print(a,'\t\t',b)
print(S)
a,*_,b  =Names
print(a,'\t\t',b)
print(S)


#9. a = the first index , b = the second index
a = Names[0]
b = Names[1]
print(a,'\t\t',b)
print(S)
a,b,*_ = Names
print(a,'\t\t',b)
print(S)
