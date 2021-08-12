"""
Make a dictionary of 4 words.Take user input from user and return the meaning
"""
dic1 = {"Cat": "A domestic animal that can meow", "Dog": "A domestic animal that can bark",
        "Tuple": "A data structure of python which has immutable elements"}
input_by_user = input("Enter the word:")
# print(dic1.get(word_by_user))
word_request = input_by_user.capitalize()
print(dic1[word_request])
