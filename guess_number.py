number = 10
remaining = 3

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while remaining > 0 and guess != number:
    remaining -= 1
    print(f'remaining guesses: {remaining + 1}')
    guess = input("Nope! Try again or write \"q\" to exit: ")

    if (guess == "q") or (number == int(guess)):
        break
    elif int(guess) > number:
        print("Too high!", end = " ")
    elif int(guess) < number:
        print("Too low!", end = " ")

if guess == "q":
    print(f"You decided to quit! The number was {number}.")
elif int(guess) == number:
    print("Congratulations! You guessed the right number.")
else:
    print(f"Sorry! The number was {number}.")