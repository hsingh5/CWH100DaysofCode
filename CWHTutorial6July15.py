# Dictionary in Python
# Dictionary is nothing but all about key value pair
dic1 = {"Harjeet": "Cereals",
        "Navneet": "pasta",
        "Rohan": "burger", "skillf": "chowmein"}
print(dic1["Rohan"])  # This is case sensitive and we are searching for key
print(type(dic1))
# lets make dictionary in dictionary
dic2 = {"harjeet": {"Breakfast": "Cereals", "Lunch": "Paneer", "Dinner": "Dosa"}}
print(dic2["harjeet"]["Breakfast"])  # to print the value of value of [key1][key of key1]
dic1["Ankit"] = "Junk Food"
dic1["Aurangzeb"] = "kabab"
print(dic1)
# What if we want to delete dic1[Aurangzeb]?
del dic1["Aurangzeb"]
print(dic1)
# What if we copy the dictionary?
"""
dic3=dic1
print("Dictionary 3 is :",dic3)
del dic3["Harjeet"]
print("Updated Dictionary 3 is :",dic3)
print("Updated Dictionary 1 is :",dic1)
"""
# To avoid this
dic3 = dic1.copy()  # also called a shallow copy
print("Dictionary 3 is :")
del dic3["Harjeet"]
print("Updated Dictionary 3 is :", dic3)
print("Updated Dictionary 1 is :", dic1)
# Inbuilt methods in Dictionary
# GET Method
print(dic1.get("Harjeet"))
# Update Method
dic1.update({"HarjeetSingh": "Chicken Tikka"})
print(dic1)
dic1.update({"Rohan": "Tikki"})
print(dic1)
dic1["HarjeetSingh"] = "McAloo Tikki"
print(dic1)
# Method to get all keys
print(dic1.keys())
# Method to get all key value pairs
print(dic1.items())
