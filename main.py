import random

#the "import random" line imports the "import" module, allowing the computer to choose a random choice between rock, paper, and scissors.

import csv
#the "import csv" line imports the "csv" module, allowing the code to save and show leader board score.

import os
#the "import os" line imports the "os" module, allowing the code to check for files


def print_welcome_message():
  print("Hello! WELCOME TO THE ROCK, PAPER, SCISSORS GAME!!!\n")
  print("The rules are simple:\n")
  print(
      "Rock beats scissors, scissors beats paper, and paper beats rock. Both players simultaneously choose one of the three options. The winner is determined by the interactions: rock crushes scissors, scissors cuts paper, and paper covers rock.\n"
  )
  print("Now let's start the game!")


# the "print_welcome_message" function prints the welcome message to the user. It uses the "format" function to insert the user's name into the message.


def determine_winner(user_choice, computer_choice):
  computer_score = 0
  player_score = 0

  print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

  if user_choice == "fireball":
    print("FIREBALL BEATS EVERY MOVE! YOU WIN!")
    player_score += 1
  elif user_choice == computer_choice:
    print(f"Both players selected {user_choice}. IT'S A TIE!")
  elif ((user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")):
    print(f"{user_choice.capitalize()} beats {computer_choice}. YOU WIN!")
    player_score += 1
  else:
    print(f"{computer_choice.capitalize()} beats {user_choice}. YOU LOSE")
    computer_score += 1
  return player_score, computer_score


# the following "determine_winner" function checks if the user's choice and the computer's choice are the same. If they are, then according to the game rules, it is a tie. If the user's choice is rock and the computer's choice is scissors or paper, the user wins. If the computer's choice is rock and the user's choice is scissors or paper, the computer wins.


def display_scoreboard(user_name, user_score, computer_score):
  print(
      f"\nScoreboard - {user_name}: {user_score} | Computer: {computer_score}\n"
  )


#the function prints the score board, comparing the user and the computer's score.


def get_user_choice(player_name):
  user_choice = input(
      f"{player_name}, enter a choice (rock, paper, scissors): ").lower()
  while user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please enter rock, paper, or scissors.")
    user_choice = input(
        f"{player_name}, enter a choice (rock, paper, scissors): ").lower()
  return user_choice


# this function doesn't only prompt the user to choose between rock, paper, scissors, but also checks if the user's input is valid. If the user's input is not valid, the function prompts the user to enter a valid choice.


def get_user_choice_fireball(player_name):
  user_choice = input(
      f"{player_name}, enter a choice (rock, paper, scissors, FIREBALL): "
  ).lower()
  while user_choice not in ["rock", "paper", "scissors", "fireball"]:
    print("Invalid choice. Please enter rock, paper scissors, or FIREBALL")
    user_choice = input(
        f"{player_name}, enter a choice (rock, paper, scissors, FIREBALL): "
    ).lower()
  return user_choice


# this function prompts the user to choose between rock, paper, scissors, and FIREBALL and checks if the user's input is valid. If it is not, the function prompts the user to enter a valid choice.


def get_players():
  global player_names

  while True:
    try:
      player_count = int(input("Enter the number of players: "))
      if player_count > 0:
        break
      else:
        print("Please enter a valid number of players (greater than 0).")
    except ValueError:
      print("Please enter a valid number of players.")

  player_names = [
      input(f"Enter the name for Player {i+1}: ") for i in range(player_count)
  ]


# this function prompts the user to enter the number of players and their names. It also checks if the number of is greater than 0.


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
          print(
              f"===> Player: {saved_player['name']}, Score: {saved_player['score']}"
          )
      else:
        print("Previous Top Players: ")
        for saved_player in data_sorted:
          print(
              f"===> Player: {saved_player['name']}, Score: {saved_player['score']}"
          )
      # this displays the last top 3 players and their scores from the CSV file.
      # If there are less than 3 players, it will only display the top players.

      for player in player_names:
        for saved_player in data_sorted:
          if saved_player['name'] == player:
            player_scores[player] = int(saved_player['score'])
            computer_scores[player] = int(saved_player['computer_score'])
      # this updates player_scores and computer_scores with the data from the CSV file.
  else:
    print(f"No previous scores, let's play!")
  # if there are no previous saved scores, the top players will not be displayed and this text will instead.


def save_scores_to_file(file_path, player_name, player_score, computer_score):
  header_written = os.path.exists(file_path)

  data = []
  # this starts data as an empty list.

  if header_written:
    with open(file_path, 'r') as file:
      reader = csv.reader(file)
      header = next(reader)
      data = [dict(zip(header, row)) for row in reader]

    for i, player in enumerate(data):
      if player['name'] == player_name:
        data[i]['score'] = str(player_score)
        data[i]['computer_score'] = str(computer_score)
        break
      #this updates the existing player's score

    else:
      data.append({
          'name': player_name,
          'score': str(player_score),
          'computer_score': str(player_score)
      })
  else:
    data.append({
        'name': player_name,
        'score': str(player_score),
        'computer_score': str(player_score)
    })

  with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'score', 'computer_score'])
    for row in data:
      writer.writerow([row['name'], row['score'], row['computer_score']])
  #this writes the data to the CSV file.


def do_continue(player_name):
  play_again_choice = input(
      "Would you like to play again? (yes or no): ").lower()
  if play_again_choice == "no":
    print(
        f"Goodbye {player_name}! We hope you enjoyed this game! Please play again soon!"
    )
    return False
  while play_again_choice not in ["yes", "no"]:
    print("Invlid choice. Please enter yes or no")
    play_again_choice = input("Enter a choice (yes or no): ").lower()
  # this function checks to make sure the user's answer is valid. If it is not, the function prompts the user to enter a valid choice (yes or no).
  if play_again_choice == "no":
    print(
        f"Goodbye {player_name}! We hope you enjoyed this game! Please play again soon!"
    )
    return False
  return True


# this function asks the user if they want to play again. If the user says no, the game for that specific user will stop, but if they say yes, it will not. In both scenarios, the game moves on to the next player if there is one.

scores_filename = "rock_paper_scissors_scores.csv"

player_names = []
# this is a list to store player names

print_welcome_message()

load_and_display_top_players(scores_filename)

get_players()

player_fireball_score = {player_name: 0 for player_name in player_names}
player_scores = {player_name: 0 for player_name in player_names}
computer_scores = {player_name: 0 for player_name in player_names}

index = 0

while len(player_names) != 0:
  index += 1
  if index >= len(player_names):
    index = 0

  if player_fireball_score[player_names[index]] < 3:
    player_choice = get_user_choice(player_names[index])
  else:
    print(
        "CONGRATULATIONS!!!!! You have won three rounds, and now have access to the FIREBALL for one round only. It beats every other move."
    )
    # this checks that the player has won 3 rounds (and can therefore use the fireball option) and informs the user they have access to it.
    player_choice = get_user_choice_fireball(player_names[index])
    if player_choice == "fireball":
      player_fireball_score[player_names[index]] = 0

  computer_choice = random.choice(["rock", "paper", "scissors"])
  # this function randomly chooses a move for the computer.
  [player_score, computer_score] = determine_winner(player_choice,
                                                    computer_choice)
  # this determines the winner of the round

  player_fireball_score[player_names[index]] += player_score
  player_scores[player_names[index]] += player_score
  computer_scores[player_names[index]] += computer_score

  display_scoreboard(player_names[index], player_scores[player_names[index]],
                     computer_scores[player_names[index]])

  if not do_continue(player_names[index]):
    save_scores_to_file(scores_filename, player_names[index],
                        player_scores[player_names[index]],
                        computer_scores[player_names[index]])
    player_names.remove(player_names[index])
  # removes user if they don't want to play again
