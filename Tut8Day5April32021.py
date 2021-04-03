#While loop
"""
i=0
while(i<40):

    print(i)
    i = i + 1
    """

#break and continue
#break means break the loop
#continue means ignore the rest of the lines and go back to the beginning of loop

i=1
while(i>0):
    i=i+1
    if i<5:
        continue
    print("Value of i is ",i)
    if i==20:
        break

