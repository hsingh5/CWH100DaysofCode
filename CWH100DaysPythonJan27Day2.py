"""
This is a multi-line comment
"""

# This is a single line comment

print("Hello world")  # print line statement
print("I am here to learn Python")
"""
After every print statement there is a new line character by default 
To avoid it,we can use ,end=" " 
"""
print("I will learn python in 100 days", end=" ")
print("I will push everything to Github")

print("Hello1", "Hello2", "Hello3", end="@")

print("C:\narry")  # this will give us error and not print what we expected
print("C:\\narry")  # we used "\" as escape sequence character
print("C:\'Harjeet\'")  # Another example of using "\" as escape sequence character

"""
Variables- Variables are like boxes or containers which can store something
"""
var1 = "Hello"
var2 = "World"
var3 = "40"
var4 = 50
var5 = 60
var6 = 37.6

print(type(var1))  # Here type function is used to know the type of var1
print(type(var2))  # Here type function is used to know the type of var2
print(type(var3))  # Here type function is used to know the type of var3
print(type(var4))  # Here type function is used to know the type of var4
print(type(var5))  # Here type function is used to know the type of var5
print(type(var6))  # Here type function is used to know the type of var6
# Can we add them? yes,if we add 2 strings they are concatenated
print(var1 + var2)
print(3 * "Hello\n")  # Here we used a escape sequence character of \n which is new line
print(var4 + var5)  # Here 2 int variables will be added resulting in Addition
# We can also do Typecasting
print(type(int(var4)))  # Here we typecasted the var4 from String to int

# Input function
var7 = input("Enter the number:")
print("You entered:", var7)
print(type(var7))
# By default,input function is string so to change its type we will have to typecaste

var8 = int(input("Enter the number:"))
print("You entered:", var8)
print(type(var8))
# Here the input function has been typcasted to int
