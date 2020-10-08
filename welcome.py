'''
login Format:
username : name
password : name
'''

import employees


def login():
    valid = 1
    print("Please enter your login details below ")
    username = input("username : ").lower()
    password = input("password : ").lower()
    if username not in employees.allEmployees:
        print("invalid username")
        valid = 0
    elif username != password:
        print("invalid password")
        valid = 0
    else:
        print("Login Successful! Welcome!")
    return valid, username


def welcome():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WELCOME TO SEP EVENT MANAGEMENT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    successlogin, username = login()
    retrycount = 1
    # If login is not successful
    while successlogin != 1:
        if retrycount > 3:
            print("Number of allowed retries over. Please try later")
            break
        print("Retry " + str(retrycount) + " of 3")
        successlogin, username = login()
        retrycount += 1
    return successlogin, username


#successfulLogin, username = welcome()
#print(successfulLogin)
#print(username)
