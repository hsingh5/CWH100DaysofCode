#Exercise:Faulty Calculator
"""
These 3 computation should be wrong
45*3=555
56+9=77
56/6=4
"""
print("Welcome to Calculator!")
var1=int(input("Enter the first number:"))
var2=int(input("Enter the second number:"))

computation=input("Which computation would you like to do?")
computation_list=["Addition","Subtraction","Division","Multiplication"]
if computation in computation_list:
    if computation=="Addition":
        sum1=var1+var2
        if ((var1==56 and var2==9) or (var1==9 and var2==56)):
            print("The sum is",77)
        else:
            print("The sum is ",sum1)

    elif computation=="Subtraction":
        diff1=var1-var2
        print("The difference is:",diff1)

    elif computation=="Multiplication":
        prod1=var1*var2
        if((var1==45 and var2==3) or (var1==3 or var2==45)):
            print("The product is ",555)
        else:
            print("The product is :",prod1)
    elif computation=="Division":
        div1=var1/var2
        if(var1==56 and var2==4):
            print("The answer is ",4)
        else:
            print("The answer is ",div1)
else:
    print("Sorry computation not available! Try something else")