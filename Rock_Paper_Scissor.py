#Dictionaries in python stores key-value pair
#dict = {key : value}
# accesing dict : dict_name [key] will return value


#List in python is surrounded by bracket and each item  is seperated by ','
#my_list = [list_items, ...,]

#this project is for studying importing libraries, functions & variables 
#importing libraries is used using keyword 'import' and library name

# refactoring of code is keeping code functionality same and make code more readable
#random library hav method choice that picks any item randomly from the list
# description: classic rock, paper and scissors game
# start

"""
**Rock-Paper-Scissors** is a simple hand game that is often used to make decisions or resolve a dispute between two people. The game involves three possible hand signs, each of which can either win, lose, or tie against the other signs.

### Basic Rules:
1. **The Hand Signs:**
   - **Rock**: Represented by a closed fist.
   - **Paper**: Represented by an open hand, palm facing downward.
   - **Scissors**: Represented by a fist with the index and middle fingers extended to mimic scissors.

2. **Game Play:**
   - Two players face each other and count down (typically by saying “Rock, Paper, Scissors, Shoot!”).
   - On "Shoot!", both players reveal one of the three hand signs simultaneously.

3. **Outcome:**
   The result is determined by the interaction of the two hand signs, based on the following rules:
   - **Rock crushes Scissors**: Rock wins.
   - **Scissors cut Paper**: Scissors win.
   - **Paper covers Rock**: Paper wins.
   - **Same signs (Rock vs. Rock, Paper vs. Paper, etc.)**: It's a tie, and the game is typically replayed.

4. **Winning Conditions:**
   - The player whose sign defeats the opponent's sign is the winner.
   - If both players use the same sign, it’s a tie, and the round is usually replayed until there's a winner.

### Game Strategy:
Rock-Paper-Scissors is largely a game of chance, but players sometimes try to predict or bluff their opponent’s next move, making it a mix of luck and psychological tactics. 

It's a quick, fun, and fair way to settle minor decisions!
"""
import random

def get_choices() -> dict[str:str]: 
    player_choice = input("Enter a choice (rock , paper , scissors):")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    choices = {'player' : player_choice , 'computer' : computer_choice}

    return choices

def check_win(player:str , computer:str)-> str:
    #this is fstring in python
    print(f"your's choice :{player} and computer's choice :{computer}")
    if player == computer :
        return "it's a tie!!"
    if( player == 'paper' and computer == 'rock') or (player == 'scissor' and computer == 'paper' ) or (player == 'rock' and computer == 'paper'):
        return "you win!!"
    else:
        return "you loose,play again"

choices = get_choices()
result = check_win(choices['player'], choices['computer'])

print(result)
# end