import random

def number_guessing_game_enhanced():
    """
    An enhanced version of the number guessing game that includes:
    1. Difficulty Levels (easy, medium, hard)
    2. A limited number of guesses based on difficulty.
    3. A "Play Again" feature.
    """
    
    # Game settings for each difficulty level
    difficulty_settings = {
        'easy': {'range': 50, 'guesses': 10},
        'medium': {'range': 100, 'guesses': 10},
        'hard': {'range': 1000, 'guesses': 10}
    }

    # Main game loop to allow playing again
    while True:
        print("\n--- Welcome to the Enhanced Number Guessing Game! ---")
        
        # --- DIFFICULTY SELECTION ---
        level = ''
        while level not in difficulty_settings:
            level = input("Choose a difficulty (easy, medium, hard): ").lower()
            if level not in difficulty_settings:
                print("Invalid difficulty. Please choose easy, medium, or hard.")

        max_number = difficulty_settings[level]['range']
        allowed_guesses = difficulty_settings[level]['guesses']
        
        # Generate the secret number based on the chosen difficulty
        secret_number = random.randint(1, max_number)
        
        print(f"\nI'm thinking of a number between 1 and {max_number}.")
        print(f"You have {allowed_guesses} guesses to find it. Good luck!")
        print("---------------------------------------------")

        # --- GUESSING LOOP WITH LIMITED ATTEMPTS ---
        guess_correct = False
        for guess_num in range(1, allowed_guesses + 1):
            try:
                # Prompt the player to enter their guess
                player_guess_input = input(f"Guess #{guess_num}: ")
                player_guess = int(player_guess_input)

                # Compare the player's guess to the secret number
                if player_guess < secret_number:
                    print("Too low! Try a higher number.")
                elif player_guess > secret_number:
                    print("Too high! Try a lower number.")
                else:
                    # This block runs if the guess is correct
                    print(f"\n🎉 Congratulations! You guessed the number!")
                    print(f"The secret number was {secret_number}.")
                    print(f"It took you {guess_num} guesses.")
                    guess_correct = True
                    break # Exit the loop since the game is won
            
            except ValueError:
                # This block runs if the player enters something that is not a number
                print("Invalid input. Please enter a whole number.")

        # --- GAME OVER (IF GUESSES RUN OUT) ---
        if not guess_correct:
            print("\n😥 Game Over! You've run out of guesses.")
            print(f"The secret number was {secret_number}.")

        # --- PLAY AGAIN FEATURE ---
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes' and play_again != 'y':
            print("Thanks for playing!")
            break # Exit the main game loop

# This line checks if the script is being run directly.
# If it is, it calls the game function to start the game.
if __name__ == "__main__":
    number_guessing_game_enhanced()
