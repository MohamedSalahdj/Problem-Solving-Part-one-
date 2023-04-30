"""
Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 
than can be divided on x,y
"""

def divided_by(x, y):
    divided_on_x_Y = []
    for i in range(101):
        if i%x ==0 and i%y == 0:
            divided_on_x_Y.append(i)
    return divided_on_x_Y
print(divided_by(2, 5))

