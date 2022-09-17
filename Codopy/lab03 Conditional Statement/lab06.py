#Admin Account
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Ad31n15Tr@t012'
#input
us = input("Username: ")
pa = input("Password: ")
#output
if us == ADMIN_USERNAME and pa == ADMIN_PASSWORD:
    print("Welcome, admin.")
else :
    print("You are not admin.")