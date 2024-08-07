import random

options = ("rock", "paper", "scissors")

running = True

while running:
    player = None 
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
        
        if player not in options:
            print("Invalid input, please enter rock, paper, or scissors.")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You Win!!")
    else:
        print("You Lose")

    if input("Play again? (y/n): ").lower() != "y":
        running = False

print("Thanks for Playing")
