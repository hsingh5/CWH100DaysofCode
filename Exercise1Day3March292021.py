#Exercise: Make a dictionry of 4 words.Take input from user and display the meaning
"""
dict1={"apple":"fruit","ball":"an object to play","cat":"a domestic animal which meows","dog":" a domestic animal which can bark"}
#sample dictionary created of 4 words

word1=input("Enter the word to be searched:")
print(dict1.get(word1))
"""

#Exercise: Create a dictionary inside a dictionary
dict2={"Harjeet's Daily eating":{"Breakfast":"Omelette","Lunch":"Rajma Rice","Evening":"Qdoba"}}
print("New created dictionary",dict2)
print(dict2["Harjeet's Daily eating"]["Breakfast"])
dict2["Harjeet's Daily eating"]["Breakfast"]="Momos"
print(dict2)
#We cannot use update function and get method when using nesting in Dictionaries