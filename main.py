import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
      "Rock vs paper = paper wins \n"
      "Rock vs scissor = Rock wins\n"
      "paper vs scissor = scissors wins \n")
while True:
    print("Enter your choice: \n "
          "R for Rock\n "
          "P for paper\n "
          "S for scissors\n")
    possible_choice = ["rock", "paper", "scissors"]
    user_input = input("select your choice: ")
    while user_input not in ["R", "P", "S"]:
        user_input = input("Enter valid input:")

    if user_input == "R":
        user_choice = "rock"
    elif user_input == "P":
        user_choice = "paper"
    else:
        user_choice = "scissors"

    computer_choice = random.choice(possible_choice)
    print("You chose " + user_choice, "and", "computer chose " + computer_choice)

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")

    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
        break
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
        break
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
        break
