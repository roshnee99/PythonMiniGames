"""
This script will define some helpful methods that we can put together to run a game of tic tac toe

The concept is simple. All the "grid" will be represented in one single array, and depending on where the
X's and O's are placed, we are to determine the winner.

We will also create a method for an AI player, who will be trying to make moves the maximize the possibility
of winning. This will not be an unbeatable AI.

BOARD VALUES:
|1|2|3|
|4|5|6|
|7|8|9|

"""

import random
import time

# Define constants here

x = "X"
o = "O"
blank = " "
bar = "|"
dash = "-"
corner_positions = [1, 3, 7, 9]
center_position = 5


def insert_token_to_board(letter, pos, possible_board):
    """
    In the board array, add the letter in its position
    :param possible_board: board to enter the letter into
    :param letter: X or O, depending on the player who made move
    :param pos: position in the board where inserting letter
    """


def is_space_free(pos, board):
    """
    :param board: Board on which to check if position is free
    :param pos: Place in board array to check
    :return: True if the space has no letter currently occupying the space
    """


def check_player_move_is_number(string):
    """
    Checks if the string value is an instance of an integer
    :param string: The player input
    :return: True if value is an integer
    """


def check_player_move_in_range(num):
    """
    Checks if valid position
    :param num: position user entered
    :return: True if num greater than or equal to 1 or less than or equal to 9
    """


def validate_move(string, board):
    """
    Takes in input string from player and sees the following conditions
    (1) Value is a number
    (2) Number is in range 1...9
    (3) Position on board is blank
    :param board: The board player is making move on
    :param string: Given player choice, check if input is valid
    :return: True if valid move
    """


def player_move(board):
    """
    Accepts an input from the user (1, 2, 3...9) which is the space where they will place "X"
    Should continue to keep asking the user for a position if they didn't type it in properly
    (ex. if they type in 10, that is not a valid position, or if the space was already occupied)
    @:param board: The board player will be making a move against
    :return: None
    """


def choose_random_position(possible_moves):
    """
    Randomly chooses a move from possible actions
    :param possible_moves: list of number positions in the board
    :return: a random move from the list of possibilities
    """


def get_empty_positions(board):
    """
    Finds all the empty positions in the board
    @:param: board that game is being hosted on
    :return: positions that are blank
    """


def get_possible_corners(possible_moves):
    """
    Returns all the possible positions that are corners
    :param possible_moves: list of possible positions
    :return: subset of possible positions that are corners
    """


def get_possible_middle(possible_moves):
    """
    Check if center position is available
    :param possible_moves: list of possible moves
    :return: True if center move possible, False if not
    """


def computer_move(board):
    """
    The algorithm for this is simple
    (0) Find all possible empty positions in the board
    (1) If there are no possible moves, that means board is full. Game is tied.
    (2) If any of the possible moves result in computer winning, choose that move
    (3) If the player can win in the next round, then make that move (to block player)
    (4) Choose a corner move. If multiple available, choose at random
    (5) Choose the center
    (6) Otherwise return a random move
    @:param board: The board computer is choosing a move from
    :return: the position the computer is moving into (0 if no possible moves)
    """
    # Get all possible moves

    # if board is empty, then it's a tie

    # check if add 'O' to possible position, is it a winning board? Return move

    # check if x is added to any of the possible positions, would player win? Return move

    # return random corner position if available

    # check if center position is available

    # return a random move if no better move is found


def is_board_full(board):
    """
    Checks if the main board has any available moves
    @:param: The board against which moves are being checked
    :return: True if the board has no more moves, False otherwise
    """


# ________________________________ Given methods ________________________________________________________


def does_player_want_to_play_again():
    """
    Asks player if they want to play again, accepts "y" or "n"
    :return: True if player wants to play again, False otherwise
    """
    player_input = input("Do you want to play again? (y/n) ")
    return player_input == "y"


def print_board(board_to_print):
    """
    Prints the board as it stands with all positions filled
    :return: None
    """
    print(blank + blank + blank + bar + blank + blank + blank + bar)
    print(blank + board_to_print[1] + blank + bar + blank + board_to_print[2] + blank + bar + blank + board_to_print[3])
    print(blank + blank + blank + bar + blank + blank + blank + bar)
    print(dash * 11)
    print(blank + blank + blank + bar + blank + blank + blank + bar)
    print(blank + board_to_print[4] + blank + bar + blank + board_to_print[5] + blank + bar + blank + board_to_print[6])
    print(blank + blank + blank + bar + blank + blank + blank + bar)
    print(dash * 11)
    print(blank + blank + blank + bar + blank + blank + blank + bar)
    print(blank + board_to_print[7] + blank + bar + blank + board_to_print[8] + blank + bar + blank + board_to_print[9])
    print(blank + blank + blank + bar + blank + blank + blank + bar)
    return


def is_winning_board(possible_board, letter):
    """
    Looking at the board, checks if the player with that letter has won.
    We check a potential board because this is not necessarily the move that is made - will be helpful
    during the computer's algorithm.
    The ways to win are across, vertical, or diagonal - so need to check all combinations
    :param possible_board: A board array with element in spot.
    :param letter: X or O
    :return: True if the board is a winning combination
    """
    # check if filled the top row
    if possible_board[1] == letter and possible_board[2] == letter and possible_board[3] == letter:
        return True
    # check if filled the second row
    if possible_board[4] == letter and possible_board[5] == letter and possible_board[6] == letter:
        return True
    # check if filled the third row
    if possible_board[7] == letter and possible_board[8] == letter and possible_board[9] == letter:
        return True
    # check if filled the first column
    if possible_board[1] == letter and possible_board[4] == letter and possible_board[7] == letter:
        return True
    # check if filled the second column
    if possible_board[2] == letter and possible_board[5] == letter and possible_board[8] == letter:
        return True
    # check if filled the third column
    if possible_board[3] == letter and possible_board[6] == letter and possible_board[9] == letter:
        return True
    # check if won diagonal left to right
    if possible_board[1] == letter and possible_board[5] == letter and possible_board[9] == letter:
        return True
    # check if won diagonal right to left
    if possible_board[3] == letter and possible_board[5] == letter and possible_board[7] == letter:
        return True
    return False


def generate_board():
    """
    @:return A new board that is all blank
    """
    return [blank] * 10


def starting_message():
    print("Get ready to play tic-tac-toe! The way this will work is simple.\n"
          "We will show you the board, and in order to put down an 'X', you will need to specify the position."
          "The top left position is 1 and so on, just like below")
    example_board = [blank] * 10
    for i in range(1, 10):
        example_board[i] = str(i)
    print()
    print_board(example_board)
    print("\n\n")


# ________________________________ Methods to run game ________________________________________________________


def run_round(board):
    """
    Runs a round of tic tac toe
    """
    pass


def play_game():
    starting_message()
    play_again = True
    while play_again:
        board = generate_board()
        print_board(board)
        run_round(board)
        play_again = does_player_want_to_play_again()
    print("Thanks for playing!")


if __name__ == '__main__':
    play_game()
