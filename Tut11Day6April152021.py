# Try Except Formula

a = (input("Enter the value of a:"))
b = (input("Enter the value of b:"))

try:
    sum = int(a) + int(b)
    print("The sum is ", sum)

except Exception as e:
    print(e)  # will print the error or exception line as string

print("This line is very important")
