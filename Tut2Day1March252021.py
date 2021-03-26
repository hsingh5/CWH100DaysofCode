mystr="Harry is a Good Boy" #Example of a ssample string
print(mystr)
print(type(mystr))
print("Value at 4th character",mystr[4])
print("Value at 5th character",mystr[5])

#now introducing STRING SLICING

print(mystr[0:4])
"""
this string slicing will include the string character at 0th place but will exclude the string character at 4th place
so it will only run from 0 to 3"""

"""What if we try to print the following?"""
#print(mystr[78])
"""Will give error since it will say the string index out of range but actually the range is till 19 characters."""
"""What is we try to print the following?"""
print(mystr[0:78])
"""This will print the whole string till 19th character and not 78"""

print(mystr[0:5:2])
"""Now this will perform string slicing and will skip (2-1) character and print """

print(mystr[0:])
"""Now this will perform string slicing till the length of the string"""

print(mystr[:5])
"""Now this will perform string slicing from 0 till 4th character.It will exclude 5th character"""

print(mystr[::])
"""Now this will perform string slicing from 0 to the whole length of string and will take by default 1 in third hence skipping 
n-1 whichis 0 value"""


print("x",mystr[-19:-2])
"""Now this will perform negative indicing.Whatever positive indexes we give to the character in string ,it reverses
and then prints"""
print(mystr[::-2])
"""What will happen if we try to print this?
output:if there is negative in the third value,it will reverse the string and then calculate"""

#print("y",mystr[-7:-1:-2]) need to check on the net

"""shorrtcut to reverse the string"""
print(mystr[::-1])


"""Inbuilt functions in STRING"""

print(mystr.isalnum())
"""
this will return boolean value whether the string as alphanumeric characters or no
In this case it will be False since our string as a space character as well"""
print(mystr.isalpha())
"""This function will also return a boolean function whether the string has alpha characters or no.In this case it will be 
false since our string also has spaces"""

print(mystr.endswith("Boy"))
"this inbuilt function will check and return a boolean answer whether our string ends with the particular characters or no" \
"Note:It is highly case sensitive"

print(mystr.find("Boy"))
"""This function will find the arguement in the string and return with the index position"""

print(mystr.replace("is","are"))
"""This function will replace the "is" in the string and replace it with "are" and then print the new string"""

print(mystr.count("o"))
"""This function can count the number of arguements and will return with the number"""

print(mystr.index("B"))
"""This function can return the index value of the required argument"""

print(mystr.upper())
"""this function will return the string in upper case"""

print(mystr.lower())
"""this function will return the string in lower case"""
