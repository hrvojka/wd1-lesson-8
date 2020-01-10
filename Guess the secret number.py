secret = 3
guess = int(input("Enter a number from 1 to 10 and see if you can guess the secret number: "))

if guess == secret:
    message = "Congratulations, 3 is the secret number!!!"
else:
    message = f"Sorry, {guess} is not the secret number. The secret number is {secret}!"

print(message)


