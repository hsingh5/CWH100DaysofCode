# Writing in the file
"""f=open("hj1.txt","a") #opened the file in write mode
f.write("\nHarjeet is learning python and web dev") #wrote to be added in file
f.close() #file closed hence freeing up resources
"""

f = open("hj1.txt", "r+")
content = f.write("H1arjeet and Navneet are getting married\n")
content1 = f.read(5)
for line in content1:
    print(line.isalnum())
print(content1)
f.close()
