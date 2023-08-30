import random


def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"



def display_result(winner, user_choice, computer_choice):
    if winner == "tie":
        print("It's a tie!")
    else:
        print(
            f"{winner.capitalize()} wins! {winner.capitalize()} chose {user_choice}, Computer chose {computer_choice}.")


def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    total_rounds = int(input("How many rounds would you like to play? "))

    user_score = 0
    computer_score = 0

    for round_number in range(1, total_rounds + 1):
        print(f"\nRound {round_number}/{total_rounds}")

        user_choice = get_user_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        display_result(winner, user_choice, computer_choice)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Your score: {user_score} | Computer score: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Sorry, the computer won. Better luck next time!")
    else:
        print("It's a tie game!")



if __name__ == "__main__":
    main()
