import flask  # single line to import flask package
import pandas  # single line to import pandas package

print("Hello World")

"""This is a multiline comment.For multiline comment we use triple commas"""
# For single line comment we can just use hash

print("Hello this is line 1")  # By default there is a new line character and the second line with come in a new line
print("Hello this is line 2")

"""To avoid new line character we can use end="" .The space between ""  in end can be anything"""
"""For example"""
print("Hello this is line 3", end="@")
print("Hello this is line 4")
"""As a result,after line 3 there will be a @ symbol"""

"""We can also have multiple print statements together"""
print("Hello this is line 5", "Hello this is line 6")  # By default there will be a space
print("Hello this is line 7")  # BY default this will come as a new line

print("C:\narry")  # Here it will take \n as a by default new line character,to avoid this we use a \ (forward slash)
print("C:\\narry")  # Here the backward slash will ignore
"""Some escape sequence characters are \n which is for new line
\t is for a new tab.Thats y escape sequence characters are those which are used in string and they behave special"""
