"""
    Create a python function that takes 2 numbers x, y 
    and prints the multiplication table from x to y
"""

def  multiplication_table_of_two_number(from_table_x, to_table_y):
    for table in range(from_table_x, to_table_y+1):
        for i in range(1,10):
            print(f"{i} * {table} = {i*table}")
        print("-"*25)

multiplication_table_of_two_number(2, 10)