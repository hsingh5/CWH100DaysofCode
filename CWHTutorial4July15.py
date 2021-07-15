"LIST in Python"
grocery = ["Harpic", "vimbar", "bhindi", "lollypop", "Deodrant", 786, 23]  # This is a mixed list
print(grocery)
print(type(grocery))
print(grocery[6])  # Accessing the list members
numberslist1 = [4, 56, 3, 24, 54, 6, 546, 5, 2345, 35, 66, 575, 2]
print("the length is :", len(numberslist1))
print(numberslist1[4])  # Accessing the list members
numberslist1.sort()  # This method will change the original list and we can see the list sorted if we print it
numberslist1.reverse()  # This method will change the original list and we can see the list reversed if we print it
print(numberslist1)
# Slicing in List
print(numberslist1[:])  # By default,on left it will take 0 and it will run till the length of the list which is 13
print(numberslist1[1:4])  # Answer is 575,546,66.It will start from 1 but will go till 3 and not 4
"""
NOTE:Slicing will always return a new list BUT it wont touch the original list 
but if we use methods like sort and reverse it will change the orinal list
"""
# Extended Slicing
print(numberslist1[
      ::2])  # So in first blank it will be default zero,the second blank will be the length of the list and third blank will skip n-1 which is 1 and print the contents of list
print(numberslist1[::-1])  # Shortcut to reverse the list
print(numberslist1[1:5:-3])
print("The original list:", numberslist1)
"""
NOTE:Negative slicing should only be done till -1 and not any number greater than that otherwise it can return in an empty list.
"""
# in Built methods in List
# Method To find out the length of the list
print("The length of the list is:", len(numberslist1))
# Method To find out the max value in the list
print("The maximum number in the list is:", max(numberslist1))
# Method To append in the list which means to add in the end of list:
numberslist1.append(6)
print(numberslist1)
"""
However if we want to append it 6 times,we will have to write the function 6 times
"""
# Method to insert
numberslist1.insert(3, 33)  # first we give the index value and then we give the value to be inserted
print(numberslist1)
# Method to remove any member of the list
numberslist1.remove(2345)  # we cant give index value here in remove function
print("The new list is", numberslist1)
# Method to POP which means to remove the last list member
numberslist1.pop()
print("List after POP is ", numberslist1)
# Method to change value of the list
numberslist1[0] = 0
print(numberslist1)
