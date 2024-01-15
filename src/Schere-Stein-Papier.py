import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
def winner():
    if user_action == computer_action:
        print("Both players selected" + user_action + " . It's a tie")
    elif user_action == "rock" and computer_action == "scissors":
        print("You win!")
    elif user_action == "paper" and computer_action == "rock":
        print("You win!")
    elif user_action == "scissors" and computer_action == "paper":
        print("You win!")
    elif user_action == "rock" and computer_action == "paper":
        print("Sorry but you lose!")
    elif user_action == "paper" and computer_action == "scissors":
        print("Sorry but you lose!")
    elif user_action == "scissors" and computer_action == "rock":
        print("Sorry but you lose!")

winner()