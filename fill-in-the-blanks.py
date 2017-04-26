# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

print "Please type a game difficulty to get started!" #User is asked for difficulty level
level = raw_input("Possible choices include easy, medium, and hard.")

missing_blanks = ["Aang", "the last airbender"]

test_string1 = "___1___ is a young air nomad and is ___2___!"

guesses = 5

# sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
# adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
# don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
# tuple, and ___4___ or can be more complicated such as objects and lambda functions.'

def word_in_blanks (word, missing_blanks):
    for blanks in missing_blanks:
        if blanks in word:
            return blanks
    return None

def play_game (word_string, missing_blanks):
    blankReplaced = []
    test_string1 = test_string1.split()
    for word in word_string:
        replacement = word_in_blanks(word, missing_blanks)
        user_input = raw_input("What should be substituted in for __1__?")
        if user_input == "captain falcon":
            # replace the __1__ in test_string1 with captain falcon from missing_blanks
            test_string1 = test_string1.replace("captain")
            blankReplaced.append(test_string1)
        else:
            blankReplaced.append(test_string1) #need to change if user doesn't get the correct answer so loop back
    blankReplaced = " ".join(blankReplaced)
    return blankReplaced

if level == 'easy':
    print "You've selected " + level + "!"
    print ('\n' "You get 5 guesses for each problem.")

    print "The current paragraph reads as follows:" + '\n' + test_string1 #sample
        #probably use loop for guesses depending if correct or wrong guesses

    #print answerEasy

# if level == 'medium':
#   print "You've selected " + level + "!!"
# if level == 'hard':
#   print "You've selected " + level + "!!!"




# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
