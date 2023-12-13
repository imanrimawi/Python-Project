import random


def print_welcome_message():
    print("Hello, {}! WELCOME TO THE ROCK, PAPER, SCISSORS GAME!!!\n".format(user_name))
    print("The rules are simple:\n")
    print(
        "Rock beats scissors, scissors beats paper, and paper beats rock. Both players simultaneously choose one of the three options. The winner is determined by the interactions: rock crushes scissors, scissors cuts paper, and paper covers rock.\n"
    )
    print("Now let's start the game!")


def get_user_choice():
    user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    if user_choice == "fireball":
        print("FIREBALL BEATS EVERY MOVE! YOU WIN!")
    elif user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = get_user_choice()
    return user_choice


def determine_winner(user_choice, computer_choice):
    global user_score
    global computer_score

    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice == "fireball":
        user_score += 1
    elif user_choice == computer_choice:
        print(f"Both players selected {user_choice}. IT'S A TIE!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print(f"{user_choice.capitalize()} beats {computer_choice}. YOU WIN!")
        user_score += 1
    else:
        print(f"{computer_choice.capitalize()} beats {user_choice}. YOU LOSE")
        computer_score += 1
    return user_score, computer_score


def display_scoreboard():
    print(f"\nScoreboard - {user_name}: {user_score} | Computer: {computer_score}\n")


user_name = input("Please enter your name: ")
user_score = 0
computer_score = 0

print_welcome_message()

while True:
    user_choice = get_user_choice()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    determine_winner(user_choice, computer_choice)
    display_scoreboard()

    if user_score == 3:
        print(
            "CONGRADULATIONS!!!!!! You have won three rounds, and you now have access to THE FIREBALL for one round only. It beats every other move."
        )
        user_choice = input(
            "Enter a choice (rock, paper, scissors, FIREBALL): "
        ).lower()
        while user_choice not in ["rock", "paper", "scissors", "FIREBALL"]:
            print("Invalid choice. Please enter rock, paper, scissors, or FIREBALL.")
            user_choice = input(
                "Enter a choice (rock, paper, scissors, FIREBALL): "
            ).lower()
        determine_winner(user_choice, computer_choice)
        display_scoreboard()

    play_again_choice = input("Would you like to play again? (Yes or No): ").lower()

    if play_again_choice == "no":
        print("Goodbye! We hope you enjoyed this game! Please play again!")
        break
    while play_again_choice not in ["yes", "no"]:
        print("Invalid choice. Please either type yes or no.")
        play_again_choice = input("Enter a choice (yes, no): ").lower()
