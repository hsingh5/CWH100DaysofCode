# IF ELSE or ELSE IF
var1 = 6
var2 = 56

var3 = int(input("Enter the number:"))  # Note: By default the input is string but here we concatinated to int

if var3 > var2:  # Note: the colon ":" here means that we want to enter this statement
    print("Greater that var 2")  # Note: there is a space in the beginning...This is called INDENTATION

elif var3 == var2:
    print("They are equal")
else:
    print("It is smaller")
"""
if var2>var3:
    print("Smaller than var 2")
"""

"""
Note:Here there are 2 if's conditions.Now python will go in first if,if the condition is satisfied it will still run 
the other if conditions.Here it is okay but what if there are 150 if else conditions? 
To break that we use "elif" conditions which means if either of one condition is satisfied it will come out.
So I am commenting the second if condition and adding a "elif" condition.
"""

# IN Keyword
list1 = [1, 2, 3, 4, 5, 6]
if 5 in list1:
    print("Yes it is in the list")

# NOT IN keyword
list2 = [7, 8, 9, 10, 11]
if 6 not in list2:
    print("No it is not in list")
