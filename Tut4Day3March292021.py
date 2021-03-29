#DICTIONARY- it is like a regular dictionary with Key value pairs
#It is declared under {} with key value pairs
#How to declare a dictionary
dic1={"apple":"a fruit","ball":"an object to play","cat":"a domestic animal which can meow","dog":"a domestic animal which can bark"}
print(dic1)
print(type(dic1))
#There are 2 ways to insert items(key value pair) in dictionary
#Normal way
dic1["egg"]="a oval white object which can be eaten"
print(dic1)
#using built in method
dic1.update({"flower":"it grows in garden"})
print(dic1)
#Method to print all keys
print(dic1.keys())
#method to print all key value pairs
print(dic1.items())
#DEL method to delete any item in dictionary
del dic1["egg"]
print(dic1)
#POP method is also there to delete the inserted item
dic1.pop("apple")
print(dic1)
#GET method to get any value from dictionary
print(dic1.get("cat"))