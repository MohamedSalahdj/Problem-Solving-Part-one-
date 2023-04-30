"""
Build an email slicer : create a function that takes an email as input and retrieve the
username and domain of the email
"""

def get_username_and_domain():
    try:
        email = input("Enter Your email: ")
        # if '@' and '.' not in email:
        #     print("Enter the correct email")
        #     get_username_and_domain()
    except ValueError:
        print("Your email not correct")
        get_username_and_domain()
    else:
        for i in range(len(email)):
            if email[i] == '@':
                username = email[:i]
                domain = email[i+1:]
        return f'username: {username}\ndomain: {domain}'

print(get_username_and_domain())