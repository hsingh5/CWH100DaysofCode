"""
Faulty Calculator:It does all right computation except
45*3=555
56+9=77
56/6=4
"""
print("Welcome to Calculator!!")

var1 = int(input("Enter the first variable:"))
var2 = int(input("Enter the second variable:"))

print("Which operation do you want:")
print("Press 1 for Multiplication")
print("Press 2 for Addition")
print("Press 3 for Division")
print("Press 4 for Subtraction")
choice_by_user = int(input("Enter your choice:"))
if choice_by_user in [1, 2, 3, 4]:
    if choice_by_user == 1:
        if var1 == 45 and var2 == 3:
            print("The result is: 555")
        elif var1 == 3 and var2 == 45:
            print("The result is: 555")
        else:
            print("The result is:", var1 * var2)
    elif choice_by_user == 2:
        if var1 == 56 and var2 == 9:
            print("The result is: 77")
        elif var1 == 9 and var2 == 56:
            print("The result is: 77")
        else:
            print("The result is:", var1 + var2)
    elif choice_by_user == 3:
        if var1 == 56 and var2 == 4:
            print("The result is: 4 ")
        else:
            print("The result is :", var1 / var2)
    elif choice_by_user == 4:
        print("The result is :", var1 - var2)

else:
    print("Wrong selection")
