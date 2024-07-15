import random

RPS = ["rock", "paper", "scissors"]
RPS_Image = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

def play_game():
    # Computer turn
    computer_choose = random.randint(0, 2)
    computer_output = RPS[computer_choose]
    computer_image = RPS_Image[computer_choose]

    # My turn
    try:
        my_choose = int(input(f"{RPS_Image[0]} :enter '1' for ROCK, \n{RPS_Image[1]} :enter '2' for PAPER, \n{RPS_Image[2]} :enter '3' for SCISSORS\n")) - 1
        if my_choose < 0 or my_choose > 2:
            print("Invalid input. Please choose 1, 2, or 3.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

    my_output = RPS[my_choose]

    # Rules
    if computer_output == my_output:
        print(f"{computer_image}\nComputer chose {computer_output}, DRAW")
        return "draw"
    elif (computer_output == "rock" and my_output == "scissors") or \
         (computer_output == "paper" and my_output == "rock") or \
         (computer_output == "scissors" and my_output == "paper"):
        print(f"{computer_image}\nComputer chose {computer_output}, YOU LOSE")
        return "lose"
    else:
        print(f"{computer_image}\nComputer chose {computer_output}, YOU WIN")
        return "win"

# Main game loop
while True:
    round = 0
    score = 0
    while round < 3:
        result = play_game()
        if result is None:
            continue  # Invalid input, retry this round
        if result == "win":
            score += 1
        round += 1
        print(f"Your score is {score}/3")
    
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        break
