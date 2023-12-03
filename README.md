# Python-Project- ROCK PAPER SCISSORS
[Link of Video - Program Running](https://drive.google.com/file/d/1nhUstwwuPlSxkA1hzbjwGpFb59yCVny4/view?usp=sharing)

## Description of the program's purpose:
##### The presumed audience of this game is for children, or teenagers who have access to computers, and want to play a game. The main purpose of its existence is for users who don’t have another person to play rock paper scissors with, but can rather play alone with a program run by the computer's random choice). 

*****

## Summary of the program's functionality:
##### 1. The function starts by importing “random.”  * This allows the computer to choose a random choice between rock, paper, scissors. 
##### 2. Next, the function introduces the rock, paper, scissors game to the user. It gives a run down of the rules, and asks the user for their name. 
##### 3. Next, the computer will randomly choose from rock, paper, or scissors, and then the user is given the choice to select one of the same options. The program will only accept one of those three choices. If not, it will ask the user to select again. 
##### 4. The following determine_winner function checks if the user's choice and the computer's choice are the same. If they are, then according to game rules, it is a tie. If the user's choice is rock and the computer's choice is scissors, or paper, the user wins. If the computer's choice is rock and the user's choice is scissors, or paper, the computer wins. It will display the score board accordingly, and will end by asking if the user wants to play another round, or not. If they do want to play again, the process will repeat without the introduction, but if not, it will end.

*****

## A description with code segments:

##### ' ' '  def get_user_choice():
##### user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
##### while user_choice not in ["rock", "paper", "scissors"]:
##### print("Invalid choice. Please enter rock, paper, or scissors.")
#####  user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
#####  return user_choice  ' ' ' 
  
##### The above code depicts the syntax error that we had to include in the program, for if the user inputs something other than “rock, paper, or scissors.” A problem we encountered while creating this code was by making it an “if” statement, rather than a “while loop.” What this did was simply ask again, without informing the user that their input was an invalid choice. We were super stuck, because we didn’t really know why the “if” statement wasn’t doing what we wanted it to do, but after researching and converting it, our problem was solved, and the code was then able to do what we wanted it to do. 

*****

