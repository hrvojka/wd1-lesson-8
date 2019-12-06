secret = 3
guess = input("Enter a number from 1 to 10 and see if you can guess the secret number: ")

if secret == guess:
    print("Congratulations, you have guessed the secret number!!!")
else:
    print("Sorry, "+str(guess)+" is not the secret number. The secret number is "+str(secret)+"!")

