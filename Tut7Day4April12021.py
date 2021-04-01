"""list1=["Harry","Carry","Mary","Larry","Sharry","Marie"]

for item in list1:
    print(item)
"""
"""
#lets try via list of list
list1=[["Harry",1],["larry",2],["Carry",6],["Marie",250]]
dict1=dict(list1) #function to typecaste any data structure to dictionary
print(dict1)
for item,item2 in list1:
    print(item,"and number of candies is ",item2)

for item in dict1.values():
    if item>3:
        print(item)
    else:
        print("Sorry")
"""

#Quiz to print items of list which are number and greater than 6
list1=[1,2,3,4,5,6,7,3,34,34,3,43,1,24,25,45,3453,566,"Harrry","Larry","Sharry","Farry"]
for item in list1:
    if str(item).isnumeric() and item>6:
        print(item)
