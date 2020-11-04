import re
# * Write a Python method to check whether a string is a valid password:
# * Password rules:
# * Should have atleast one number
# * Should have at least one uppercase and one lowercase character.
# * Should have at least one special symbol
# * Should be between 6 to 20 characters long.


def password_checker(password):
    regex = "[a-z]?[A-Z]?[0-9]?[\W]?"

    validPassword = re.match(regex, password)

    # print(validPassword)

    if validPassword and len(password) > 6:
        print('Password is valid')

    else:
        print('Enter the valid Password')
        print('\n Should have atleast one number\n \
Should have at least one uppercase and one lowercase character.\n \
Should have at least one special symbol\n \
Should be between 6 to 20 characters long.')


password = input('Enter the Password: ')

if password == "":
    print('Password can\'t be blank')

else:
    password_checker(password)


# * Solution 2
# def password_check(passwd):

#     SpecialSym = ['$', '@', '#', '%']
#     val = True

#     if len(passwd) < 6:
#         print('Length be at least 6')
#         val = False

#     if len(passwd) > 20:
#         print('length should not be greater than 8')
#         val = False

#     if not any(char.isdigit() for char in passwd):
#         print('Password should have at least one numeral')
#         val = False

#     if not any(char.isupper() for char in passwd):
#         print('Password should have at least one uppercase letter')
#         val = False

#     if not any(char.islower() for char in passwd):
#         print('Password should have at least on lowercase letter')
#         val = False

#     if not any(char in SpecialSym for char in passwd):
#         print('Password should have at least one of the symbol $@#')
#         val = False

#     if val:
#         return val


# password = input('Enter Password: ')

# if(password_check(password)):
#     print('Password is valid')

# else:
#     print('Invalid Password')
