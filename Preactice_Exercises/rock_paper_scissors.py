import random

rock = "rock"
paper = "paper"
scissors = "scissors"
options = ["rock", "paper", "scissors"]

computer = random.choice(options)

user = input(str("Select rock, paper or scissors: ")).lower()

if user == computer:
    print(f"Computer: {computer}")
    print("It's a tie")
elif user == "rock" and computer == "scissors":
    print(f"Computer: {computer}")
    print("User Wins")
elif user == "paper" and computer == "rock":
    print(f"Computer: {computer}")
    print("User Wins")
elif user == "scissors" and computer == "paper":
    print(f"Computer: {computer}")
    print("User Wins")
else:
    print(f"Computer: {computer}")
    print("Computer Wins")
