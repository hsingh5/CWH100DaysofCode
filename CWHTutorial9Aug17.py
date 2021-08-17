# For Loops
list1 = ["Harry", "Larry", "Carry", "Mary", "Harjeet"]
for item in list1:  # It will run as long as the list is there.Repition of this process is called ITERATION
    print(item)  # Indentation here means that we are inside the for loop

# Can we run For Loop in Tuple?
tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, "Carry", "Larry")
for item1 in tup1:
    print(item1)

# Yes we can run for loop in tuple

# Can we try in List of lists?
list3 = [["Harjeet", 1], ["Larry", 2], ["Carry", 3]]

for item2, lollypop in list3:
    print("name is ", item2, "and no of  lollypop is ", lollypop)  # This is called unpacking of List

dict1 = dict(list3)  # Type conversion from list of lists to Dictionary
print(dict1)
print(type(dict1))

for name, lollypops in dict1.items():
    print(name, lollypops)
"""We can perform the same packing and unpacking in dictionaries BUT
we need to be careful regarding usage of
dict1.items()
dict1.keys()
dict1.values()
"""
