number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while int(guess) != number:
    if guess == "q":
        break
    elif int(guess) > number:
        print("Too high!", end = " ")
    elif int(guess) < number:
        print("Too low!", end = " ")
    guess = input("Try again or write \"q\" to exit: ")

if int(guess) == number:
    print("Congratulations! You guessed the right number.")
else:
    print(f"Sorry! The number was {number}.")