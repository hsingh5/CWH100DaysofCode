# Operators in Python
"""
1)Arithmetic operator
2)Assignment operator
3)Comparison operator
4)Logical operator
5)Identity operator
6)Membership operator
7)Bitwise operator
"""
# Arithmetic operator
print("5+6=", 5 + 6)  # Returns sum
print("5-6=", 5 - 6)  # Returns difference
print("5*6=", 5 * 6)  # Returns product
print("5%6=", 5 % 6)  # Returns remainder operator
print("5/6=", 5 / 6)  # Returns exact value in decimals
print("5//6=", 5 // 6)  # Returns integer value also called Floor Division Operator
print("5^6=", 5 ** 6)  # Returns power product/exponential operator

# Assignment Operator
print("Assignment Operator")
x = 5  # this means that the value of 5 is being assigned to the variable x
x += 7  # this means x=x+7
x %= 7  # this means x=x%7

# Comparison Operator
# These operators can be >,>=,<,<=,==
print("Comparison Operatora=")
i = 6
print(i < 5)  # Less than < symbol
print(i > 5)  # Greater than > symbol
print(i >= 5)  # Greater than or equal to symbol
print(i <= 5)  # Less than or equal to symbol

# Logical Operator
print("Logical Operator")
a = True
b = False
print(a and b)
print(a or b)

# Identity operator
print("Identity Operator")
print(5 is 5)  # This means if 5 is 5? If its Yes,it is True
print(5 is not 10)  # This means if 5 is 10? If its Yes,it is True

# Membership Operator
# in,not in
list1 = [1, 2, 3, 4, 5, 6]
if 5 in list1:
    print("Yes")
else:
    print("no")

print(4 in list1)

# Bitwise operator
