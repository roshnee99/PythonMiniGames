import random

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
possible_actions = [ROCK, PAPER, SCISSORS]


def get_user_input():
    return input("Enter a choice (rock, paper, scissors): ")


def get_computer_input():
    return random.choice(possible_actions)


def determine_winner(user_choice, computer_choice):
    """
    :param user_choice: string if user chose rock, paper, or scissors
    :param computer_choice: computers string of rock, paper, or scissors
    :return: 1 if user wins, 0 if tie, -1 if computer wins
    """
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
        return 0
    elif user_choice == ROCK:
        if computer_choice == SCISSORS:
            print("Rock smashes scissors! You win!")
            return 1
        else:
            print("Paper covers rock! You lose.")
            return -1
    elif user_choice == PAPER:
        if computer_choice == ROCK:
            print("Paper covers rock! You win!")
            return 1
        else:
            print("Scissors cuts paper! You lose.")
            return -1
    elif user_choice == SCISSORS:
        if computer_choice == PAPER:
            print("Scissors cuts paper! You win!")
            return 1
        else:
            print("Rock smashes scissors! You lose.")
            return -1


def player_play_again():
    return input("Do you want to play again? (y/n): ") == 'y'


def validate_input(user_choice):
    return user_choice in possible_actions


def run_game():
    print("Get ready to play rock, paper scissors!")
    play_again = True
    while play_again:
        user = get_user_input()
        while not validate_input(user):
            print("Please choose between rock, paper, or scissors")
            user = get_user_input()
        computer = get_computer_input()
        determine_winner(user, computer)
        play_again = player_play_again()
    print("Thank you for playing!")


if __name__ == '__main__':
    run_game()
