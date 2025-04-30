# Imported the 'random' python module in order to select a word randomly from the list
import random

# The following code segment called 'pickTheWord()' is used for reading and splitting words from a '.txt' file into a list
# The code is from a GeeksforGeeks article called:
# "Pulling a random word or string from a line in a text file in Python"
# Here is the link: https://www.geeksforgeeks.org/pulling-a-random-word-or-string-from-a-line-in-a-text-file-in-python/
# I modified it to return a list of words that I can randomly sort through for my Wordle game.
def pickTheWord():
    with open("words.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        return words

# Checks if the guess is the correct length of 5 letters
def checkLength(userInput):
    if len(userInput) != 5:
        print("Try again! Your guess must be exactly 5 letters long.")
        return True
    return False

# Checks if the input is a real word by cross-checking with the 5-letter word list
def checkReal(userInput, wordList):
    if userInput not in wordList:
        print("The word entered is not real. Please try a different word.")
        return True
    return False

# Function that creates feedback symbols for the user
def createFeedback(userInput, wordle):
    feedbackSymbol = ""
    for i in range(5):
        # Shows that the letter is correct and in the right position.
        if userInput[i] == wordle[i]:
            feedbackSymbol = feedbackSymbol + "$"
        # Shows that the letter is right, but is in the wrong position
        elif userInput[i] in wordle:
            feedbackSymbol = feedbackSymbol + "%"
        # Shows that the letter is not in the word
        else:
            feedbackSymbol = feedbackSymbol + "*"
    return feedbackSymbol

# Selecting the wordle word from the word list (.txt file)
wordList = pickTheWord()
wordle = random.choice(wordList)

# Introduction to the game for the user
print("Welcome to Wordle! You have 6 attempts to guess the 5-letter word. \n\nThe $ symbol will represent letters that "
      "were placed in the right position.\nThe * symbol will represent letters that are not found within the word.\n"
      "The % symbol will represent letters that are in the word, but wasn't placed in the right spot.\n")

# Variable to track number of tries the user is at
tries = 0

while tries < 6:
    userInput = input("\nEnter a 5-letter word: ").lower()

    # Calls upon two functions to check whether the word length is proper and the word itself is real
    if checkLength(userInput):
        continue
    if checkReal(userInput, wordList):
        continue

    # Calls a function that gives the user feedback on the input they gave
    feedbackSymbol = createFeedback(userInput, wordle)
    print("Feedback: " + feedbackSymbol)

    tries = tries + 1

    # Checks whether the user input was the right word. If it is, the code then returns a 'win' message
    if userInput == wordle:
        print("You guessed the word! Good job.")
        break

# Returns 'loss' message if all attempts are used up
if tries == 6:
    print("\nGame over - You have used up all of your tries! The word was: " + wordle)