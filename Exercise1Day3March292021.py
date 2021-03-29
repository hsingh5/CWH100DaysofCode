#Exercise: Make a dictionry of 4 words.Take input from user and display the meaning

dict1={"apple":"fruit","ball":"an object to play","cat":"a domestic animal which meows","dog":" a domestic animal which can bark"}
#sample dictionary created of 4 words

word1=input("Enter the word to be searched:")
print(dict1.get(word1))
