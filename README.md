# Python-Project- ROCK PAPER SCISSORS 
# VERSION 1
[Link of Video - (VERSION 1) Program Running](https://drive.google.com/file/d/1nhUstwwuPlSxkA1hzbjwGpFb59yCVny4/view?usp=sharing)
## Development plan:
### VERSION 1 of project - goals and individual tasks:
| Task / goal                    | Person Responsible      | 
| -------------                  |:-------------:| 
| Intro (rules) + get user input from user : (rock, paper, scissors)  | Sima |
| Code for program's random generator  | Masa           |         
| Program dictates who wins based off of rules (if, else, elif)           | Iman      |   
| Ask user if they want to play again + simple syntax error | Sima|
| Add comments along the way | Masa |
| Display scoreboard after each round | Iman |

#### COMPLETED WORK:
##### Milestone 1: intro + user input + random generator
##### Milestone 2: determine_winner function completed + ask user if they want to play again
##### Milestone 3: simply syntax error + scoreboard + 
##### (comments where written during every milestone)

*****

## Description of the program's purpose:
##### The presumed audience of this game is for children, or teenagers who have access to computers, and want to play a game. The main purpose of its existence is for users who don’t have another person to play rock paper scissors with, but can rather play alone with a program run by the computer's random choice. 

*****

## Summary of the program's functionality:
##### 1. The function starts by importing “random.”  * This allows the computer to choose a random choice between rock, paper, scissors. 
##### 2. Next, the function introduces the rock, paper, scissors game to the user. It gives a run down of the rules, and asks the user for their name. 
##### 3. Next, the computer will randomly choose from rock, paper, or scissors, and then the user is given the choice to select one of the same options. The program will only accept one of those three choices. If not, it will ask the user to select again. 
##### 4. The following determine_winner function checks if the user's choice and the computer's choice are the same. If they are, then according to game rules, it is a tie. If the user's choice is rock and the computer's choice is scissors, or paper, the user wins. If the computer's choice is rock and the user's choice is scissors, or paper, the computer wins. It will display the score board accordingly, and will end by asking if the user wants to play another round, or not. If they do want to play again, the process will repeat without the introduction, but if not, it will end.

*****

## A description with code segments (break through moment):

##### ' ' '  def get_user_choice():
##### user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
##### while user_choice not in ["rock", "paper", "scissors"]:
##### print("Invalid choice. Please enter rock, paper, or scissors.")
#####  user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
#####  return user_choice  ' ' ' 
  
##### The above code depicts the syntax error that we had to include in the program, for if the user inputs something other than “rock, paper, or scissors.” A problem we encountered while creating this code was by making it an “if” statement, rather than a “while loop.” What this did was simply ask again, without informing the user that their input was an invalid choice. We were super stuck, because we didn’t really know why the “if” statement wasn’t doing what we wanted it to do, but after researching and converting it, our problem was solved, and the code was then able to do what we wanted it to do. 

*****

# Python-Project- ROCK PAPER SCISSORS 
# VERSION 2
### [Link of Video - (VERSION 2) Program Running](https://drive.google.com/file/d/1a0EgLPEpw_4__HRfSuTq9wbdYGfJTElg/view?usp=sharing)

## Development plan:
### VERSION 2 of project - goals and individual tasks:
| Task / goal                    | Person Responsible      | 
| -------------                  |:-------------:| 
| Multi Player vs Computer  | Sima |
| Import CSV + store scoreboard data  | Masa           |         
| Unlock Fireball after 3 rounds won    | Iman      |   

*****

#### COMPLETED WORK:
##### Milestone 1: unlock fireball after winning three rounds - fireball beats all other plays
##### Milestone 2: import csv and create spreadsheet
##### Milestone 3: display csv after (stop playing)
##### Milestone 4: multiplayer - 2+ players can play vs the computer, and compete over who wins the most rounds
##### (comments where written during every milestone)

*****


## Description of the program's purpose:
##### The main purpose that distinguishes our version 1 of the game, from version 2, are the additional features that were added. The first one is the MultiPlayer feature vs the computer. This feature allows multiple players to play vs the computer at once, and see who can win first. Our second feature is the CSV document, and storing the scoreboard data. This allows for the user to see who is winning and the top three winners on the scoreboard. The CSV updates this list every time somebody plates. Our last and final key feature of version 2 was the fireball. When the user beats the computer by 3 points, they have the option to use a "fireball" for one round, which beats all other plays. All of these new additions allowed us to take our game to the next level. This way players are not only able to play rock paper scissors when they don't have a partner, but rather play more interactive and exciting rock paper scissors, which is unique to any other. Overall, this program was intended for people who want a more fun version of rock paper scissors which they won't be able to find anywhere else, and can be played with or without others. 

*****


## Summary of the program's functionality:
##### 1. The function starts by importing “random,” "os," and "csv."  * This allows the computer to choose a random choice between rock, paper, scissors, providing functions for interacting with the operating system, and  for saving and displaying leaderboard scores using a CSV file. 
##### 2. Next, the function introduces the rock, paper, scissors game to the user. It gives a run down of the rules, and asks the user for their name. 
##### 3. The game will ask if the user wants to play multiplayer, or alone. If the user chooses to play alone, the game will begin. If the user chooses multiplayer, they will enter the amount of players and the names of each player. Every single player will go in turns, and play one round vs the computer. 
###### 4. Next, the computer will randomly choose from rock, paper, or scissors (import random) , and then the user is given the choice to select one of the same options. The program will only accept one of those three choices. If not, it will ask the user to select again. 
##### 4. The following determine_winner function checks if the user's choice and the computer's choice are the same. If they are, then according to game rules, it is a tie. If the user's choice is rock and the computer's choice is scissors, or paper, the user wins. If the computer's choice is rock and the user's choice is scissors, or paper, the computer wins. It will display the scoreboard between the computer and user accordingly, and will end by asking if the user wants to play another round, or not. If they do want to play again, the process will repeat without the introduction, but if not, it will end.
##### 5. If the user wins by three, they will have the option to use the FIREBALL for one round which beats every other move.
##### 6. When and if the user is done playing, the scoreboard will display, representing the top three users at the very top of the scoreboard. 

*****

## Break through moment with code segments:
##### segment 1:
#####    def save_scores_to_file(file_path, player_name, player_score, computer_score):


##### segment 2:
 #####   display_scoreboard(player_names[index], player_scores[player_names[index]], computer_scores[player_names[index]])

  #####  if not do_continue(player_names[index]):
     #####   save_scores_to_file(scores_filename, player_names[index], player_scores[player_names[index]], computer_scores[player_names[index]])


##### The above code depicts some snippets which we included in order to use the CSV file and display a scoreboard. This part definitely took the longest. We used a lot of resources online to complete this and apply it to our personal code. This includes research coming from the python website (python.org) , as well as numerous youtube videos. The above code shows 2 small segments of code for the CSV component. The first segment defines a function (save_scores_to_file). The second segment displays a scoreboard and then checks if the player wants to continue playing. If the player doesn't want to, it saves scores using the function defined in the first segment. An issue we encountered was that once the game reached its end and a player didn't want to continue, the game wouldn't move on to the next player because of an error encountered while trying to save the data. We realized that in the save_scores_to_file function (in the second segment), it was being given 4 arguments whereas the definition of the function (in the first segment) was originally only given 3 parameters (there was no "computer_score" parameter). Once that was added in the definition, the function was now expecting to get 4 arguments, so saving the data became a success.





