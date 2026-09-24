# rock papar scissor
"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""
import random

item_list = ["Rock" ,"Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor :- ")
comp_choice = random.choice(item_list)

print(f"user choice is = {user_choice}, comp_choice is = {comp_choice}")

if user_choice == comp_choice:
    print("Both choose same : Match Tie")
    
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("paper cover rock = computter win")
    else:
        print("ROck smash scissor =  you win")
        
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cut paper = Computer win")
    else:
        print("paper cover rock = You win")
        
elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smash scissor = Computer win")
    else:
        print("Scissor cut paper = You win")
        



