import random

#the "import random" line imports the "import" module, allowing the computer to choose a random choice between rock, paper, and scissors.

import csv
#the "import csv" line imports the "csv" module, allowing the code to save and show leader board score.

import os
#the "import os" line imports the "os" module, allowing the code to check for files

def print_welcome_message():
    print("Hello, {}! WELCOME TO THE ROCK, PAPER, SCISSORS GAME!!!\n".format(user_name))
    print("The rules are simple:\n")
    print(
        "Rock beats scissors, scissors beats paper, and paper beats rock. Both players simultaneously choose one of the three options. The winner is determined by the interactions: rock crushes scissors, scissors cuts paper, and paper covers rock.\n"
    )
    print("Now let's start the game!")

# the "print_welcome_message" function prints the welcome message to the user. It uses the "format" function to insert the user's name into the message.

def get_user_choice():
    user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = get_user_choice()
    return user_choice
# this function doesn't only prompt the user to choose between rock, paper, scissors, but also checks if the user's input is valid. If the user's input is not valid, the function prompts the user to enter a valid choice.

def determine_winner(user_choice, computer_choice):
    global user_score
    global computer_score

# the "global" keyword is used to define a global variable. In this case, the "user_score" and "compuer_score" variables are global variables, which means they can be accessed and modified from anywhere in the program.
  
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice == "fireball":
        print("FIREBALL BEATS EVERY MOVE! YOU WIN!")
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
# the following "determine_winner" function checks if the user's choice and the computer's choice are the same. If they are, then according to the game rules, it is a tie. If the user's choice is rock and the computer's choice is scissors or paper, the user wins. If the computer's choice is rock and the user's choice is scissors or paper, the computer wins.

def display_scoreboard():
    print(f"\nScoreboard - {user_name}: {user_score} | Computer: {computer_score}\n")

user_name = input("Please enter your name: ")
user_score = 0
computer_score = 0

def get_user_choice_fireball(player_name):
  user_choice=input(f"{player_name}, enter a choice (rock, paper, scissors, FIREBALL): ").lower()
  while user_choice not in ["rock", "paper", "scissors", "fireball"]:
    print("Invalid choice. Please enter rock, paper scissors, or FIREBALL")
    user_choice = input(f"{player_name}, enter a choice (rock, paper, scissors, FIREBALL):").lower()
  return user_choice

#the function prints the score board, comparing the user and the computer's score.

print_welcome_message()

player_fireball_score = {player_name: 0 for player_name in player_names}
player_score = {player_name: 0 for player_name in player_names}
computer_scores = {player_name: 0 for player_name in player_names}

index = 0 

while len(player_names) == 0 :
  index += 1
  if index >= len(player_names):
    index = 0

if player_fireball_score[player_names[index]] > 3:
  player_choice = get user_choice(player_names[index])
else:
  print(
    "CONGRATULATIONS!!!!! You have won three rounds, and now have access to the FIREBALL for one round only. It beats every other move."
  )
  player_choice = get_user_choice(player_names[index])
  if player_choice == "fireball":
    player_fireball_score[player_names[index]] = 0

computer_choice = random.choice (["rock", "paper", "scissors"])
[player_score, computer_score] = determine_winner(player_choice, computer_choice)

player_fireball_score[player_names[index]] += player_score
player_scores[player_names[index]] += player_score
computer_scores[player_names[index]] += computer_score

display_scoreboard(player_names[index], player_scores[player_names[index]],
computer_scores[player_names[index]] += computer_score

display_scoreboard(player_names[index], player_scores[player_names[index]], computer_scores[player_names[index]])

if not do_continue(player_names[index]):
  save_scores_to_file(scores_filename, player_names[index], player_Scores[player_names[index]], computer_scores[player_names[index]])
  player_names.remove(player_names[index])

def load_and_display_top_players(file_path):
    # checking that the file exists
    if os.path.exists(file_path):
        # declaring "global" variables
        global player_names
        global player_scores
        global computer_scores

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            # creates a CSV reader
            header = next(reader)
            data = [dict(zip(header, row)) for row in reader]
            # sorts data based on 'score'
            data_sorted = sorted(data, key=lambda x: int(x['score']), reverse=True)
            if len(data) >= 3:
                print("\nPrevious Top 3 Players: ")
                for saved_player in data_sorted[:3]:
                    print(f"===> Player: {saved_player['name']}, Score: {saved_player['score']}")
            else:
                print("Previous Top Players: ")
                for saved_player in data_sorted:
                    print(f"===> Player: {saved_player['name']}, Score: {saved_player['score']}")
            # this displays the last top 3 players and their scores from the CSV file. 
            # If there are less than 3 players, it will only display the top players.

            for player in player_names:
                for saved_player in data_sored:
                    if saved_player['name'] == player:
                        player_scores[player] = int(saved_player['score'])
                        computer_scores[player] = int(saved_player['computer_score'])
            # this updates player_scores and computer_scores with the data from the CSV file.
    else:
      print(f"No previous scores, let's play!")
      # if there are no previous saved scores, the top players will not be displayed and this text will instead.

def save_scores_to_file(file_path, player_name, player_score):
    header_writen = os.path.exists(file_path)

    data = []
    # this starts data as an empty list.

    if header_written:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = [dict(zip(header, row)) for row in reader]

        for i, player in enumerate(data):
            if player['name'] == str(player_score):
                data[i]['score'] = str(player_score)
                data[i]['computer_score'] = str(computer_score)
                break
            #this updates the existing player's score
      
        else:
            data.append({'name': player_name, 'score': str(player_score), 'computer_score': str(player_score)})
    else:
        data.append({'name': player_name, 'score': str(player_score), 'computer_score': str(player_score)})

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'score', 'computer_score'])
        for row in data:
            writer.writerow([row['name'], row['score'], row['computer_score']])
    #this writes the data to the CSV file.

# add function for saving scores to file

while True:
    if user_score == 3:
        print(
            "CONGRATULATIONS!!!!!! You have won three rounds, and you now have access to THE FIREBALL for one round only. It beats every other move."
        )
        user_choice = input(
            "Enter a choice (rock, paper, scissors, FIREBALL): "
        ).lower()
        while user_choice not in ["rock", "paper", "scissors", "fireball"]:
            print("Invalid choice. Please enter rock, paper, scissors, or FIREBALL.")
            user_choice = input(
                "Enter a choice (rock, paper, scissors, FIREBALL): "
            ).lower()
        determine_winner(user_choice, random.choice(["rock", "paper", "scissors"]))
        display_scoreboard()


        play_again_choice = input("Would you like to play again? (Yes or No): ").lower()
        if play_again_choice == "no":
            print("Goodbye! We hope you enjoyed this game! Please play again!")
            break
        while play_again_choice not in ["yes", "no"]:
            print("Invalid choice. Please either type yes or no.")
            play_again_choice = input("Enter a choice (yes, no): ").lower()
        if play_again_choice == "no":
            print("Goodbye! We hope you enjoyed this game! Please play again!")
            break

    user_choice = get_user_choice()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    determine_winner(user_choice, computer_choice)
    display_scoreboard()

    play_again_choice = input("Would you like to play again? (Yes or No): ").lower()
  #after each round, the user is asked if they want to play again or stop playing. If the user enters "yes", then the game loops again. If the user enters "no", then the game ends. No other words are accepted.

    if play_again_choice == "no":
        print("Goodbye! We hope you enjoyed this game! Please play again!")
        break
    while play_again_choice not in ["yes", "no"]:
        print("Invalid choice. Please either type yes or no.")
        play_again_choice = input("Enter a choice (yes, no): ").lower()

# if the user enters "stop playing", the game ends.