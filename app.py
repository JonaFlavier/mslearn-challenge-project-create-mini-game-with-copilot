import random

"""
This is a simple rock, paper, and scissors game.
The rules are:

1. Run the minigame on the console with the python app.py command.

2. At the prompt, type one of the game options: rock, paper, or scissors.

3. The minigame should inform the player whether the player won, lost, or tied with the opponent.

4. Choose to continue playing.

5. At the prompt, type screen.

6. The minigame should inform the player if the option entered by the player is invalid.

7. Repeat steps 2 and 4 to play a few rounds and choose not to continue playing.

8. Check if the minigame is terminated and if it displays your score, informing you of the number of wins and rounds.

The Specifications are:

Rock beats scissors.
Scissors beat paper.
Paper beats rock.

"""

print("Hello, World!")

# Rock paper and scissors game
def play_game():
    options = ["rock", "paper", "scissors"]
    player_score = 0
    rounds = 0
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_choice not in options:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(options)
        print(f"Computer chooses: {computer_choice}")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "scissors" and computer_choice == "paper") or
            (player_choice == "paper" and computer_choice == "rock")
        ):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
        rounds += 1
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print(f"Game over! Your score: {player_score}/{rounds}")

play_game()