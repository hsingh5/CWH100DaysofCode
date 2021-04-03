#Number Guessing Game


correctnumb1=99
no_of_attempts=9

while (True):
    guessnumb1 = int(input("Enter the number to be guessed: \n"))
    if guessnumb1 < correctnumb1:
        print("Sorry you entered a number less that the number to be guessed")
        no_of_attempts = no_of_attempts - 1
        print("No of attempts remaining:", no_of_attempts)
        print("Try again!")
        if no_of_attempts == 0:
            print("Sorry you have reached the max no of attempts")
            break
        else:
            continue
    elif guessnumb1>correctnumb1:
        print("Sorry you entered a number greater that the number to be guessed")
        no_of_attempts = no_of_attempts - 1
        print("No of attempts remaining:", no_of_attempts)
        print("Try again!")
        if no_of_attempts==0:
            print("Sorry you have reached the max no of attempts")
            break
        else:
            continue
    else:
        print("Congratulations you have guessed the right number which is \n",guessnumb1)
        no_of_attempts=no_of_attempts-1
        print("Number of attempts remaining",no_of_attempts)
        print("Congratulations!")
        break