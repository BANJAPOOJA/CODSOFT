import random

def game():
    user_score = 0
    computer_score = 0
    round_num = 1

    while True:
        user_action = input(f"Round {round_num}: Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win this round!")
                user_score += 1
            else:
                print("Paper covers rock! Computer wins this round.")
                computer_score += 1
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win this round!")
                user_score += 1
            else:
                print("Scissors cuts paper! Computer wins this round.")
                computer_score += 1
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win this round!")
                user_score += 1
            else:
                print("Rock smashes scissors! Computer wins this round.")
                computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}\n")

        play_again = input("Play another round? (yes/no): ")
        if play_again.lower()!= "yes":
            break
        round_num += 1

    print(f"Final Score - You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("You win the game!")
    elif user_score < computer_score:
        print("Computer wins the game!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    game()