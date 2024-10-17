import random
def roll_dice():
    # Generate a random number between 1 and 6
    return random.randint(1, 6)
def main():
    print("Welcome to the Dice Roll Simulator!")
    while True:
        input("Press Enter to roll the dice...")  # Wait for the user to press Enter
        result = roll_dice()  # Roll the dice
        print(f"You rolled a {result}!")  # Display the result

        # Ask the user if they want to roll again
        roll_again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if roll_again != 'yes':
            print("Thank you for using the Dice Roll Simulator! Goodbye!")
            break  # Exit the loop if the user doesn't want to roll again
# Run the main program
if __name__ == "__main__":
    main()
