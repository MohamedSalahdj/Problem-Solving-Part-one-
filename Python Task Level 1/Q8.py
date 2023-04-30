"""
Create a function that takes x,y 
and prints all the number that can be divide by y from x to 100
"""

def divide_by_y(x, y):
    l = []
    for i in range(x, 101):
        if i % y ==0:
            l.append(i)
    return l


print(divide_by_y(5, 10))