"""
Take input from the user as "Age"
If age>18,user can drive
If age<18,user connot drive
If age=18,user has to go to RTO Office
"""
age_user = int(input("Enter the age:"))

if age_user > 18 and age_user < 80:
    print("You can drive!")
elif age_user >= 1 and age_user < 18:
    print("You are not eligible")
else:
    print("Come to Office for Documents for review")
