import random

from chatbot import *
from chatbot.matchers.ExactMatch import *
from chatbot.matchers.KeywordEncoder import *
from chatbot.matchers.GoogleSentenceEncoder import *
from chatbot.TrainingSamples import training_samples
from rps.play_game import run_game as play_rock_paper_scissors
from tic_tac_toe.play_game import play_game as play_tic_tac_toe

encoder = ExactMatch()
threshold = 0


def get_text_input():
    pass


def user_says_bye(user_input):
    pass


def get_max_similarity(samples, user_input):
    pass


def get_top_intent(intent_to_score_dict):
    pass


def get_user_intent(user_input):
    pass


def get_favorite_subject_response():
    pass


def get_feeling_response():
    pass


def get_name_response():
    pass


def get_game_response():
    pass


def get_default_response():
    pass


def run_bot():
    pass


if __name__ == '__main__':
    run_bot()
    print("I enjoyed getting to know you!")

