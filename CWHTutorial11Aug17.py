# Break and Continue
# Break
print("Program to demonstrate Break")
i = 0
while (1):  # It is going to run as long as the condition is satisfied
    print(i + 1, end=" ")
    if (i == 44):
        break  # Break means stop and break the loop,after using break
    i = i + 1
# Applying Break will come here

# Continue
print("\nProgram to demonstrate Continue")
i = 0
while (1):
    i = i + 1
    if i < 5:
        continue  # Continue will go to the starting of the loop without going down
    elif i == 44:
        break
    else:
        print(i, end=" ")
