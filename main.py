import random

#the "import random" line imports the "import" module, allowing the computer to choose a random choice between rock, paper, and scissors.

def print_welcome_message():
  print("Hello, {}! WELCOME TO THE ROCK, PAPER, SCISSORS GAME!!!\n".format(
      user_name))
  print("The rules are simple:\n")
  print(
      "Rock beats scissors, scissors beats paper, and paper beats rock. Both players simultaneously choose one of the three options. The winner is determined by the interactions: rock crushes scissors, scissors cuts paper, and paper covers rock.\n"
  )
  print("Now let's start the game!")

# the "print_welcome_message" function prints a welcome message to the user. It uses the "format" function to insert the user's name into the message.

def get_user_choice():
  user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
  while user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please enter rock, paper, or scissors.")
    user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
  return user_choice

#this function doesnt only prompt the user to choose between rock, paper, and scissors, but also checks if the user's input is valid. If the user's input is not valid, the function prompts the user to enter a valid choice.This is possible, thanks to the "while" loop.

def determine_winner(user_choice, computer_choice):
  global user_score
  global computer_score

  #the "global" keyword is used to define a global variable. In this case, the "user_score" and "computer_score" variables are global variables, which means they can be accessed and modified from anywhere in the program.

  print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

  if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. IT'S A TIE!")
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
    print(f"{user_choice.capitalize()} beats {computer_choice}. YOU WIN!")
    user_score += 1
  else:
    print(f"{computer_choice.capitalize()} beats {user_choice}. YOU LOSE!")
    computer_score += 1

#the following determine_winner function checks if the user's choice and the computer's choice are the same. If they are, then according to game rules, it is a tie. If the user's choice is rock and the computer's choice is scissors, or paper, the user wins. If the computer's choice is rock and the user's choice is scissors, or paper, the computer wins.

def display_scoreboard():
  print(
      f"\nScoreboard - {user_name}: {user_score} | Computer: {computer_score}\n"
  )

user_name = input("Please enter your name: ")
user_score = 0
computer_score = 0

#the function prints the score board, comparing the user, and the computers scores.

print_welcome_message()

while True:
  user_choice = get_user_choice()
  computer_choice = random.choice(["rock", "paper", "scissors"])

  determine_winner(user_choice, computer_choice)
  display_scoreboard()

  play_again_choice = input(
      "Enter a choice (play again, stop playing): ").lower()

  #after each round, the user is asked if they want to play again, or stop playing. If the user enters "play again", the game loops again. If the user enters "stop playing", the game ends.

  if play_again_choice == "stop playing":
    print("Goodbye! We hope you enjoyed this game! Please play again!")
    break

#if the user enters "stop playing", the game ends.

  