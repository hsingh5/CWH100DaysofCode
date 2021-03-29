#Sets are those data type which have unique values
s=set()
"""s.add(1)
print(s)
print(type(s))
list=[1,2,3,4,5,6,34,3,34,21,3,4,5,6,3,2,3,4]
set_from_list=set(list)
print(set_from_list)
"""
#to add element in the set
s.add(1)
s.add(2)
s.add(3)
s.add(34)
print(s)
#to remove element in the set
s.remove(34)
print("after removval",s)
print(type(s))
s1=s.union({1,2,3,4})
s2=s.intersection({1,2,3,4,5,6,7,8,9,11,12,13,14})
print("Set s is",s)
print("Set s1 after uniion is",s1)
print("Set s2 after intersectino is ",s2)