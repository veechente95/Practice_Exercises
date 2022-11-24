import random

rock = "rock"
paper = "paper"
scissors = "scissors"
options = ["rock", "paper", "scissors"]

computer = random.choice(options)

selection = input(str("Select rock, paper or scissors: ")).lower()
