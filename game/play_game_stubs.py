import random

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
possible_actions = [ROCK, PAPER, SCISSORS]


def get_user_input():
    # generate a prompt that returns the value of rock, paper, or scissors depending on what user types
    return


def get_computer_input():
    # choose a random action from the possible actions for computer to take
    return


def determine_winner(user_choice, computer_choice):
    """
    Create some logic that determines who is the winner of rock, paper, scissors
    Provide a helpful print statement saying "Rock smashes scissors! You win!" or something
    to make the game feel a little more interactive
    :param user_choice: string if user chose rock, paper, or scissors
    :param computer_choice: computers string of rock, paper, or scissors
    :return: 1 if user wins, 0 if tie, -1 if computer wins
    """
    return


def player_play_again():
    # create a prompt that returns True or False if user wants to continue to play
    return


def validate_input(user_choice):
    # determine if user_choice is in the list of possible values
    return


def run_game():
    print("Get ready to play rock, paper scissors!")
    # do logic here for running the game
    print("Thank you for playing!")


if __name__ == '__main__':
    run_game()
