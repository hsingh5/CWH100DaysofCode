# Number guessing game
no_to_be_guessed = 100
no_of_attempts = 5
while (1):
    input_from_user = int(input("Enter the number to be guessed:"))
    if input_from_user == no_to_be_guessed:
        print("Congratulations! You guessed the right number!")
        no_of_attempts = no_of_attempts - 1
        print("No. of attempts:", no_of_attempts)
        break
    elif input_from_user > no_to_be_guessed:
        print("Sorry! You entered a number greater than number to be guessed")
        print("Try Again!")
        no_of_attempts = no_of_attempts - 1
        print("No. of attempts:", no_of_attempts)
        if no_of_attempts == 0:
            print("Maximum number of attempts reached! Sorry")
            break
        else:
            continue
    elif input_from_user < no_to_be_guessed:
        print("Sorry! You entered a number lesser than number to be guessed")
        print("Try Again!")
        no_of_attempts = no_of_attempts - 1
        print("No. of attempts:", no_of_attempts)
        if no_of_attempts == 0:
            print("Maximum number of attempts reached! Sorry Try agein")
            break
        else:
            continue
