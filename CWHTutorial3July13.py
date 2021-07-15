mystr = "Harry is a good boy"
print(mystr[5])
print(mystr)
print(mystr[0:5])  # this will print from 0 to 4 and it will exclude 5
# print(mystr[65]) #this will give an error since its out of range
print(mystr[0:65])  # this will print all the values between 0 to 64 and not 65
print(mystr[0:])  # this will print the whole string
print(mystr[:8])  # this will make the range from 0 to 7
print(mystr[:])  # this will print the whole string
print("Case where the all the 3 places are blank: ",
      mystr[::])  # if the third place after : is blank,it will take default as 1
# ADVANCED STRING SLICING
print(mystr[0:5:2])  # It will print from 0 to 4 and then it will skip 1 value from 0th value position
# NEGATIVE STRING SLICING
print("After negative slicing:", mystr[-10:-2:5])
# Shortcut to Reverse String
print("Reversed String:", mystr[::-1])
# Function to return Alphanumeric string and it will return the result in True/False
print(mystr.isalnum())  # it will return False since it has spaces.If it has no spaces,it will return TRUE
mystr1 = "harjeetisagoodboy2804 and a nbice boy"
print(mystr1.isalnum())
# Function to check whether the string ends with the digit or no.It will return it either True or False
print(mystr1.isdigit())
# Function to check whether the string ends with particular character
print(mystr.endswith("boy"))
# Function to count a particular string
print(mystr1.count("e"))
# Function to find a particular string and it returns the index value
print(mystr1.find("28"))
# Function to capitalize the whole string.Capitalize means it will start from Capital Letter
print(mystr1.capitalize())
# Function to convert the whole string to small letters.
print(mystr1.lower())
# Function to convert the whole string to capital
print(mystr1.upper())
# Function to replace a particular string from the whole string
print(mystr1.replace("nbice", "nice"))
# Function to find a string at a particular index
print("The value is :", mystr1.index("2804"))
