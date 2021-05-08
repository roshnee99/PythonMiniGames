from tkinter import *
from play_game import *


# methods for dynamic part of UI
def determine_winner_from_user(user_choice):
    computer_choice = get_computer_input()
    return determine_winner(user_choice, computer_choice), computer_choice


def generate_ui_output(user_choice):
    winner, computer_choice = determine_winner_from_user(user_choice)
    player_choice_label.config(fg="red", text="Player Choice : " + str(user_choice))
    computer_choice_label.config(fg="green", text="Computer Choice : " + str(computer_choice))
    if winner == 1:
        outcome_label.config(fg="blue", text="Outcome : Player Won")
    elif winner == 0:
        outcome_label.config(fg="blue", text="Outcome : It's a Draw")
    else:
        outcome_label.config(fg="blue", text="Outcome : Computer Won")


# Generate the UI

# generate the window
main_screen = Tk()
main_screen.title("Rock Paper Scissors")

Label(main_screen, text="Rock, Paper, Scissors", font=("Calibri", 14)).grid(row=0, sticky=N, pady=10, padx=200)
Label(main_screen, text="Please select an option", font=("Calibri", 12)).grid(row=1, sticky=N)
player_choice_label = Label(main_screen, font=("Calibri", 12))
player_choice_label.grid(row=3, sticky=W)
computer_choice_label = Label(main_screen, font=("Calibri", 12))
computer_choice_label.grid(row=3, sticky=E)
outcome_label = Label(main_screen, font=("Calibri", 12))
outcome_label.grid(row=3, sticky=N)

# Buttons
Button(main_screen, text="Rock", width=15, command=lambda: generate_ui_output(ROCK)).grid(row=4, sticky=W, padx=5,
                                                                                          pady=5)
Button(main_screen, text="Paper", width=15, command=lambda: generate_ui_output(PAPER)).grid(row=4, sticky=N, pady=5)
Button(main_screen, text="Scissors", width=15, command=lambda: generate_ui_output(SCISSORS)).grid(row=4, sticky=E,
                                                                                                  padx=5,
                                                                                                  pady=5)

main_screen.mainloop()
