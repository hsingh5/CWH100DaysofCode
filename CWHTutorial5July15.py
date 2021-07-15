# Tuple in list
"""
Lists are mutable
Tuple are immutable
"""
tp = (1, 2, 3, 4, 5, 5, 6)
print(tp)
# tp[1] = 89  # Tuple is immutable which means we cant change the value of a tuple
print(type(tp))
# To make a tuple of 1 element we always use one extra comma or ,
tp1 = (1,)
print(tp1)
print(type(tp1))

# Shortcut to swap 2 variables
a = 1
b = 2
c = 3
d = 4
# we can even do swapping with 3 numbers or more than that
a, b, c, d = d, c, b, a
print("Value of a:", a)
print("Value of b:", b)
print("Value of c:", c)
print("Value of d:", d)
