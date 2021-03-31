"""Quiz: Take input from user
if age=18 come to office for licence
if age>18 he can drive
if age<18 you cantdrive

agecust1=int(input("Enter the age:"))

if (agecust1 < 18 or agecust1>80):
    print("Sorry you cannot drive")
elif (agecust1>18 and agecust1<80):
    print("You can drive")
else:
    print("Come to office for Driving License")
"""


#Exercise- To use the above quiz in list and use IN and NOT IN keyword
drivage=[18,19,20,21,22,23,24,25,26,27,28,29,30]
agecust2=int(input("Enter your age:"))
if (agecust2 in drivage):
    print("You can drive!")
elif (agecust2 not in drivage):
    print("You cannot drive!")
elif (agecust2 < 18):
    print("Come to office and we will evaluate")
