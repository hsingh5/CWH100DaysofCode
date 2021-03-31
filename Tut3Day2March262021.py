
"""A sample list of grocery.List can also have numbers and string characters"""
grocery=["Harpic","Vimbar","lollypop","milk","coca cola",566,555,550]
print(grocery)
print(type(grocery))


#Lets declare a sample number list
numbers=[4,22,5,6,7,23,45,76,12,23,3]
print(numbers)
print(type(numbers))
#method to sort the list by inbuilt method
numbers.sort()
print(numbers,"Here is the sorted list")

#method to reverse the list by inbuilt method
numbers.reverse()
print(numbers,"Here is the reveresd list")

#NOTE:BOth the methods will change the original list

#List Slicing
"""NOTE:String slicing will return a new list but it wont change the original list.
Inbuilt methods like Sorting and reversing will change the original list"""

print(numbers,"Here is the original list")
print(numbers[:])
#First blank will take 0 and second blank will go till the end of length of list
#Slicing is same as done in string.
#Never take negative slicing more than -1.It will raise issues


#Inbuilt functions of list

#to find out length of list
print(len(numbers))

#to find out max of list
print(max(numbers))

#to find out min of list
print(min(numbers))

#to append in list-means to add in end
numbers.append(555)
print(numbers)

#to insert in the list at particular index
numbers.insert(7,99999)
print(numbers)

#to POP the list-to remove from the end
numbers.pop()
print(numbers)

#to make a blank list
numbers2=[]
print(numbers2)

#to remove a particular number
numbers.remove(99999)
print(numbers)

#to extend the list 
abc=["a","b"]
abc.extend("canada")
print(abc,"Here is the new llist after using extend function")



#TUPLE-Immutatble list-whose elements cant be changed

tup1=(1,2,3,4,5)
print(tup1)
print(type(tup1))
print(len(tup1))
#To create an empty 1 element tuple we use following way
tup2=('a',)
print("New created tuple is ",tup2,"and the type is ",type(tup2))