s = set()
print(type(s))
# How to make a set from list
s_from_list = set([1, 2, 3, 4, 5, 6])
print(s_from_list)
print(type(s_from_list))

# Add elements to list
s.add(1)
s.add(1)  # Set only has UNIQUE VALUES and NO DUPLICATE Values
print(s)
# Functions in SET
# Union Function
s1 = s.union([1, 2, 3, 4, 5, 5, 6, 7])
print(s1)
# Intersection Functino
s2 = s1.intersection([1, 2, 3, 4, 5, 6, 7])
print(s2)
