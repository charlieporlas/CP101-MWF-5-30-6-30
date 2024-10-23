import random

# Generate a random number between 1 and 20
number_to_guess = random.randint(1, 20)

# Set the number of attempts
max_attempts = 3

print("Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 20.")
print(f"You have {max_attempts} attempts to guess it correctly.")

# Loop through the guessing process
for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == number_to_guess:
        print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempt} attempt(s).")
        break
    elif guess < number_to_guess:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    if attempt == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}.")
