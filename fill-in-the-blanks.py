# IPND Stage 2 Final Project

import sys

easy_quiz = "In Python, use the __1__ sign to assign values to variables. Python syntax is simple. For example, type in __2__ 'Hello, world!' to print the string. Functions start with keyword __3__ and take in any __4__ parameters."
easy_answers = ["equal", "print", "def", "input"]

medium_quiz = "The five types of variables are __1__, string, lists, tuples, and dictionary. Strings are defined as characters represented in __2__ marks. __3__ store many items separated by commas and enclosed within square brackets. The values stored in lists can be changed meaning they are __4__. Tuple is similar to lists but a key difference is that the values enclosed are read-only. This means tuples are __5__."
medium_answers = [ "numbers", "quotation","lists", "mutable", "immutable"]

hard_quiz = "In order to create a function, it must be __1__ before it is used. The function __2__ starts with keyword def, followed by a given __3__, and then __4__. Functions can use any number of __5__ that respond to the __6__ in the parentheses."
hard_answers = ["defined", "block", "name", "parentheses", "arguments", "parameters"]


# After user selects difficulty level, play_game runs through the quiz and answer.
# The game gives them 5 attempts to complete the quiz before it's game over.
# User is prompted for a response to fill in the missing blanks. If they're incorrect,
# they lose an attempt and are prompted to try again.

def play_game(test_string, missing_values):
    attempts_allowed = 5
    for word in test_string.split():
        if word.startswith("__"):
            while attempts_allowed > 0:
                user_input = raw_input("What should be substituted for " + word)
                if user_input == missing_values[0]:
                    test_string = test_string.replace(word, user_input)
                    missing_values.remove(user_input)
                    print "\nCorrect!" "\n" + test_string
                    break
                else:
                    attempts_allowed = attempts_allowed - 1
                    print 'You have ' + str(attempts_allowed) + ' attempts remaining.'
            if attempts_allowed == 0:
                print "You ran out of attempts! Game over!"
                sys.exit()

    print "\nYou won!"

# One of the following are executed depending on the user's choice of difficulty
def difficulty_level(level):
    if level == 'easy':
        print "You've selected " + level + "!"
        print ('\n' "You get 5 guesses for each problem.")

        print "The current paragraph reads as follows:" + '\n' + easy_quiz
        play_game(easy_quiz, easy_answers)

    if level == 'medium':
        print "You've selected " + level + "!"
        print ('\n' "You get 5 guesses for each problem.")

        print "The current paragraph reads as follows:" + '\n' + medium_quiz
        play_game(medium_quiz, medium_answers)

    if level == 'hard':
        print "You've selected " + level + "!"
        print ('\n' "You get 5 guesses for each problem.")

        print "The current paragraph reads as follows:" + '\n' + hard_quiz
        play_game(hard_quiz, hard_answers)

#User is asked for difficulty level and then call on difficulty_level.
print "Please type a game difficulty to get started!"
level = raw_input("Possible choices include easy, medium, and hard.")
difficulty_level(level)




