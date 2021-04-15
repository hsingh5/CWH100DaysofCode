# Functions
"""
def function1(a,b):
    """"""This function determines the average of 2 numbers""""""
    average=(a+b)/2
    return  average

avg=function1(2,4)
print(avg)
print(function1.__doc__)
"""


# Simple arithmetic calculator via funtions

def addition(x, y):
    """This function determines sum of 2 numbers and returns the result"""
    result = x + y
    return result


def subtraction(x, y):
    """This function determins subtraction of 2 numbers and returns the result"""
    result = x - y
    return result


def multiplication(x, y):
    """This function determines product of 2 numbers and returns the result"""
    result = x * y
    return result


x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
a = addition(x, y)
print("Result after addition is ", a)
print(addition.__doc__)
b = subtraction(x, y)
print("Result after subtraction is ", b)
print(subtraction.__doc__)
c = multiplication(x, y)
print("Result after multiplication is ", c)
print(multiplication.__doc__)
