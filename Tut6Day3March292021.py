"""Quiz: Take input from user
if age=18 come to office for licence
if age>18 he can drive
if age<18 you cantdrive
"""
agecust1=int(input("Enter the age:"))

if (agecust1 < 18 or agecust1>80):
    print("Sorry you cannot drive")
elif (agecust1>18 and agecust1<80):
    print("You can drive")
else:
    print("Come to office for Driving License")