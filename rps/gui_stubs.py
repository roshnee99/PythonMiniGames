from tkinter import *
from play_game import *

# Define our static variables
main_screen = Tk()
player_choice_label = Label(main_screen, font=("Calibri", 12))
computer_choice_label = Label(main_screen, font=("Calibri", 12))
outcome_label = Label(main_screen, font=("Calibri", 12))


# methods for dynamic part of UI
def determine_winner_from_user(user_choice):
    """
    :param user_choice: One of possible actions
    :return: computer choice and a key dictating who the winner of game is
    """
    return


def generate_ui_output(user_choice):
    """
    After a button click, populate player_choice_label, computer_choice_label, and outcome_label
    :param user_choice: based on button clicked, will be one of possible_actions
    :return: None
    """
    return


# Generate the UI
def generate_ui():
    main_screen.title("Rock Paper Scissors")
    # create title label
    Label(main_screen, text="Rock, Paper, Scissors", font=("Calibri", 14)).grid(row=0, sticky=N, pady=10, padx=200)
    # create instruction label
    Label(main_screen, text="Please select an option", font=("Calibri", 12)).grid(row=1, sticky=N)
    # place empty labels on main screen (for now they have no text)
    player_choice_label.grid(row=3, sticky=W)
    computer_choice_label.grid(row=3, sticky=E)
    outcome_label.grid(row=3, sticky=N)
    # create rock button
    Button(main_screen, text="Rock", width=15, command=lambda: generate_ui_output(ROCK)).grid(row=4, sticky=W, padx=5, pady=5)
    # create paper button
    Button(main_screen, text="Paper", width=15, command=lambda: generate_ui_output(PAPER)).grid(row=4, sticky=N, pady=5)
    # create scissors button
    Button(main_screen, text="Scissors", width=15, command=lambda: generate_ui_output(SCISSORS)).grid(row=4, sticky=E, padx=5, pady=5)


# generate the window
if __name__ == '__main__':
    generate_ui()
    main_screen.mainloop()

