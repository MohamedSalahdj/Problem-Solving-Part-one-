"""
Make a temperature/measurement converter. Write a script that can convert
Fahrenheit to Celcius and back, or inches to centimeters and back, etc in 3 different
ways
"""

def convert_Fahrenheit_to_celcius():
    try:
        num = int(input("""Enter the temperature you like to convert
        1-convert from Fahrenheit to celcius and 
        2-celcius to Fahrenheit convert """))
        if num == 1:
            try:
                temp = float(input("You will convert from Fahrenheit to celcius \nEnter the temperature: "))
            except ValueError:
                print("accept only number! ")
                convert_Fahrenheit_to_celcius()
            else:
                celcius = (temp - 32 ) * 5 / 9
                print(f'{celcius}°C')
        elif num == 2:
            try:
                temp = float(input("You will convert from celcius to Fahrenheit\nEnter the temperature: "))
            except ValueError:
                print("accept only number! ")
                convert_Fahrenheit_to_celcius()
            else:
                Fahrenheit = (temp * 1.8) + 32
                print(f'{Fahrenheit}°F')
        else:
            print("please Enter 1 Or 2 ")
            convert_Fahrenheit_to_celcius()
    except ValueError:
        print("accept only number! ")
        convert_Fahrenheit_to_celcius()

convert_Fahrenheit_to_celcius()