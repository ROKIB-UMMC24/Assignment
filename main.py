import random # for generating random number


# Randomly select a number between 1 and 100
winning_number = random.randint(1, 100)
print(winning_number)  # This is to check the number for the programmer. This number will be unknown to the player

# Initialize a guess counter
guess_count = 0

while True:
    guess_number = input("Enter your guess between 1 to 100 or 'q' to quit: ")

    try:
        # Convert the input to an integer
        guess_number = int(guess_number)

        # For every guess increment the guess_count
        guess_count += 1

        # Check if the guess is within the valid range (1 to 100). Just mentioning the rules to the player.
        if guess_number < 1 or guess_number > 100:
            print("The guess must be between 1 and 100.")
            continue  # Skip to the next iteration if out of range

        # Game on with valid Guess
        if guess_number < winning_number:
            print("The number guessed by the player is less than the correct number to win.")

        elif guess_number > winning_number:
            print("The number guessed by the player is greater than the correct number to win.")

        else:
            print(f"Bravo! You are the winner. It took you {guess_count} guesses.")
            break  # finish the loop when the player guess the number correctly

    except ValueError:
        # Catch any ValueErrors and display a message
        print("Invalid input! Please enter a valid number or 'q' to quit.")

    # For Quit The Game at Anytime
        if guess_number.lower() == 'q':
            print("Thank you for participating. Goodbye!")
            break