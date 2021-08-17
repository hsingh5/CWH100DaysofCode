# Create a list mixed one and to print only those list items which are numbers and bigger than 6

list1 = ["Harry", "Carry", "Larry", "Mary", 1, 2, 3, 4, 5, 6, 12, 13, 123, 123214, 1234, 7, 8, 9, 23, 24, 25, "Sharry"]

for item in list1:
    if str(item).isnumeric() and item > 6:
        print(item)
