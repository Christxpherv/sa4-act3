number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while guess != number:
    guess = input("Nope! Try again or write \"q\" to exit: ")
    if guess == "q":
        break
    guess = int(guess)

if guess == number:
    print("Congratulations! You guessed the right number.")
else:
    print(f"Sorry! The number was {number}.")