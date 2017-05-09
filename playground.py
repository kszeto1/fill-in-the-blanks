import sys

easy_quiz = "In Python, use the __1__ sign to assign values to variables. Python syntax is simple. For example, type in __2__ 'Hello, world!' to print the string. Functions start with keyword __3__ and take in any __4__ parameters."
easy_answers = ["equal", "print", "def", "input"]

print "Please type a game difficulty to get started!"
level = raw_input("Possible choices include easy, medium, and hard.") #User is asked for difficulty level

def play_game (test_string, missing_values):
    output = ''
    attempts_allowed = 5
    for word in test_string.split():
        if word.startswith("__"):
            while attempts_allowed > 0:
                user_input = raw_input("fill in the blank for " + word)
                if user_input == missing_values[0]:
                    output += ' ' + user_input
                    missing_values.remove(user_input)
                    print "\nCorrect!"
                    break
                else:
                    attempts_allowed = attempts_allowed - 1
                    print 'You have '+ str(attempts_allowed) + ' attempts remaining.'
            if attempts_allowed == 0:
                print "You ran out of attempts! Game over!"
                sys.exit()
        else:
            output += ' ' + word

    print output.lstrip() + "\nYou won!"

if level == 'easy':
    print "You've selected " + level + "!"
    print ('\n' "You get 5 guesses for each problem.")

    print "The current paragraph reads as follows:" + '\n' + easy_quiz
    print play_game(easy_quiz, easy_answers)