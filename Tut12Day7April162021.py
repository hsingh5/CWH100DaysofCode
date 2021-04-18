# FILE IO in Python
"""
There are diff modes in which files are opened in Python

a)"r"- this mode is only used for reading the file
b)"w"- this mode is only used for writing the file
c)"a"- this more is only used for appending in the file.This means content is already there and we are appending it only
d)"t"- this mode opens text only files
e)"b"- this mode opens binary file only
f)"x"- this mode will check for existing file.If file is there,it will file.If file doesn't exists,it will create a new file
g)"+"- read and write both




"""
f = open("hj.txt", "rt")
# content=f.read()
"""
If we iterate f and we try it,it wont run since the f pointer is stored in content.
If we iterate content,it will iterate character by character"""
for line in f:
    print(line)

for line1 in f:  # it wont print anything since f pointer is empty now
    print(line1, "Hello")
"""content1=f.read(3)
print(f)
print("1",content)
print(type(f))
print(type(content))
print("2",content1)"""
f.close()  # we need to close the file to free up the resources taken to open the file
