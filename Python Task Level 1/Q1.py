"""
Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
the x,y range
"""

def even_and_odd_numbers(x, y):
    l_even = []
    l_odd = []
    for i in range(x, y+1):
        if i%2 == 0:
            l_even.append(i)
        else:
            l_odd.append(i)
    return f"even numbers : {l_even}\n\nodd numbers: {l_odd}"

print(even_and_odd_numbers(5,50))
