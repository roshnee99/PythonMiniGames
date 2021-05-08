import random


# let's learn how to write some python!
# Believe it or not, these are all the skills you need to write a fun command line game

def print_hello_world():
    # write a print statement below
    print("Hello World")


def print_a_statement(statement):
    # write a print statement that prints out the {statement}
    print(statement)


def print_input_from_user():
    # provide a user a prompt and print the statement
    user_input = input("Type whatever you want here")
    print_a_statement("I can repeat whatever you say!" + user_input)


def define_a_list():
    # write a method that creates and returns a list in python
    my_list = ["math", "english", "science"]
    return my_list


def generate_random_from_list(a_list):
    # given a list, return a random element from it
    return random.choice(a_list)


def check_element_in_list(element, a_list):
    # given an element and a list, check if the element is in a list and return the value
    return element in a_list


def write_an_if_statement(evaluation):
    # given an expression that evaluates to True or False, use an if statement
    # to print whether the value was true OR false
    if evaluation:
        print_a_statement("It was true!")
    else:
        print_a_statement("It was false!")


def create_a_while_loop(num_iterations):
    # make a loop that runs {num_iterations} times
    current_iteration = 1
    while current_iteration <= num_iterations:
        print_a_statement("I'm looping!")
        current_iteration = current_iteration + 1


if __name__ == '__main__':
    write_an_if_statement(True)
