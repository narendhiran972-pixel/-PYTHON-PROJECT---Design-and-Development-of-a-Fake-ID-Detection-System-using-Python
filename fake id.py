import re

def is_valid_name(name):
    return name.isalpha()

def is_valid_age(age):
    return age.isdigit() and 18 <= int(age) <= 60

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def is_valid_id(id_no):
    return id_no.isdigit() and len(id_no) == 6

def check_id():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    email = input("Enter Email: ")
    id_no = input("Enter ID Number (6 digits): ")

    if (is_valid_name(name) and 
        is_valid_age(age) and 
        is_valid_email(email) and 
        is_valid_id(id_no)):
        print("Result: Valid ID")
    else:
        print("Result: Fake ID")

while True:
    print("\n1. Check ID\n2. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        check_id()
    elif choice == "2":
        print("Exiting system...")
        break
    else:
        print("Invalid choice")
