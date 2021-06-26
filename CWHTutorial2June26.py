var1 = "Hello World"  # string variable
print(var1)  # Hello World string is stored in var1
var2 = 4  # integer variable
var3 = 36.7  # decimal variable
print(type(var3))
var4 = "harjeet"
print(var1 + var4)  # this will concatenate the strings
var5 = "4"  # Caution: this is a string and not a integer variable
print(type(var5))
# Lets try var3 + var 5 and see the result!
# print(var3+var5) This will give an error since we cant add an integer variable and a string variable
# Can we convert string to int?.. Yes we can but by type casting
var6 = "54"
var7 = "32"
print(type(int(var6)))  # This is called type casting where we converted a string variable to integer variable
print(int(var6) + int(var7))

"""How to print Hello world 10 times?"""
print("Hello world" * 10)
print("Bye world")

"""Lets use a input function"""
print("Enter any number:")
inpnum = input()  # Whatever input we use it will be going in as a STRING and not as a INTEGER
print(inpnum)
print(type(inpnum))

inpnum1 = int(input("Enter any number"))  # Here we type casted the input into integer
