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
    return input()


def user_says_bye(user_input):
    return get_user_intent(user_input) == Goodbye


def get_max_similarity(samples, user_input):
    max_score = 0
    for sample in samples:
        similarity = encoder.similarity(user_input, sample)
        if similarity > max_score:
            max_score = similarity
    return max_score


def get_top_intent(intent_to_score_dict):
    top_score = 0
    top_intent = ""
    for intent, score in intent_to_score_dict.items():
        if score >= top_score:
            top_score = score
            top_intent = intent
    if top_score < threshold:
        return None
    return top_intent


def get_user_intent(user_input):
    intent_to_top_score = {}
    for intent, samples in training_samples.items():
        max_score = get_max_similarity(samples, user_input)
        intent_to_top_score[intent] = max_score
    top_intent = get_top_intent(intent_to_top_score)
    return top_intent


def get_favorite_subject_response():
    subjects = ["math", "science", "history", "english", "chemistry"]
    subject = random.choice(subjects)
    possible_responses = ["My favorite subject is " + subject, "I really like " + subject]
    return random.choice(possible_responses)


def get_feeling_response():
    feelings = ["happy", "sad", "content", "excited", "frustrated"]
    feeling = random.choice(feelings)
    possible_responses = ["I'm feeling " + feeling, feeling, "What's in a feeling anyway?"]
    return random.choice(possible_responses)


def get_name_response():
    name = "Jim"
    possible_responses = ["My name is " + name, "What's a name to you really?", name]
    return random.choice(possible_responses)


def get_game_response():
    possible_responses = ["I can play tic tac toe and rock paper scissors!",
                          "I love rock paper scissors and tic tac toe!"]
    return random.choice(possible_responses)


def get_default_response():
    possible_responses = ["I didn't understand what you said", "I'm sorry :( I'm still learning",
                          "Can you try repeating the question again?",
                          "The only things I know to do are " + str(training_samples.keys())]
    return random.choice(possible_responses)


def run_bot():
    print("Hi there!")
    user_input = get_text_input()
    while not user_says_bye(user_input):
        intent = get_user_intent(user_input)
        if intent == WhatName:
            print(get_name_response())
        elif intent == WhatGame:
            print(get_game_response())
        elif intent == PlayTicTacToe:
            play_tic_tac_toe()
            print("What else do you wanna do?")
        elif intent == PlayRockPaperScissors:
            play_rock_paper_scissors()
            print("What else do you wanna do?")
        elif intent == GetFeeling:
            print(get_feeling_response())
        elif intent == FavoriteSubject:
            print(get_favorite_subject_response())
        else:
            print(get_default_response())
        user_input = get_text_input()


if __name__ == '__main__':
    run_bot()
    print("I enjoyed getting to know you!")

