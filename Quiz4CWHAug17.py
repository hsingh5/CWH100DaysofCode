"""
Quiz: to take input from user till 100.But when user input is 100 or more than 100 it will break
"""
while (1):
    input_from_user = int(input("Enter any number:"))
    if input_from_user > 100:
        print("Congo you entered value more than 100")
        break
    else:
        print("Try again")
        continue
