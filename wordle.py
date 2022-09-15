import random
from  wordlist_helper import getWordList

def pickHiddenWord():
    words = getWordList()
    r = words[0]
    r = random.randrange(0, len(words))
    return words[r]

def getPlayerGuess():
    playerGuess = input("Enter a guess: ").lower()
    while playerGuess not in getWordList():
        playerGuess = input("Your guess is not valid. Enter another: ").lower()

    return playerGuess

def generateFeedback(guess, hiddenWord):
    hiddenwordC = list(hiddenWord)
    guessList = [3,3,3,3,3]
    feedbacknew = ""

    for x in range(5):
        if guess[x] == hiddenwordC[x]:
            guessList[x] = 1
            hiddenwordC[x] = 0
    for x in range(5):
        if guess[x] in hiddenwordC and guess[x] != 1:
            guessList[x] = 2
    for x in range(5):
        if guessList[x] == 1:
            feedbacknew+="G"
        elif guessList[x] == 2:
            feedbacknew+="Y"
        else:
            feedbacknew+="B"

    return feedbacknew

def displayFeedback(feedback):

    print(feedback)

def playWordle():

    hiddenWord = pickHiddenWord()
    guesses = []
    guess = ""

    for x in range(6):
        guess = getPlayerGuess()
        while len(guess) != 5:
            print("Invalid input. Try again.")
            guess = getPlayerGuess()
        guesses.append(guess)
        displayFeedback(generateFeedback(guesses[x], hiddenWord))
        if generateFeedback(guesses[x], hiddenWord) == "GGGGG":
            break

    return hiddenWord, guesses


def playWordleAI(level):

    words = getWordList()
    hiddenWord = pickHiddenWord()
    comparisonFeedback = generateFeedback(hiddenWord, "abcde")
    comparisonFeedback2 = generateFeedback(hiddenWord, "fghij")
    comparisonFeedback3 = generateFeedback(hiddenWord, "klmno")
    comparisonFeedback4 = generateFeedback(hiddenWord, "pqrst")
    comparisonFeedback5 = generateFeedback(hiddenWord, "uvwyz")
    guesses = []

    if int(level) == 5:
        for x in range(len(words)):
            if generateFeedback(words[x], "abcde") == comparisonFeedback and \
                generateFeedback(words[x], "fghij") == comparisonFeedback2 and \
                generateFeedback(words[x], "klmno") == comparisonFeedback3 and \
                generateFeedback(words[x], "pqrst") == comparisonFeedback4 and \
                generateFeedback(words[x], "uvwyz") == comparisonFeedback5:
                guesses.append(words[x])
            if len(guesses) > 5 or words[x] == hiddenWord:
                break

    if int(level) == 4:
        for x in range(len(words)):
            if generateFeedback(words[x], "abcde") == comparisonFeedback and \
                generateFeedback(words[x], "fghij") == comparisonFeedback2 and \
                generateFeedback(words[x], "klmno") == comparisonFeedback3 and \
                generateFeedback(words[x], "pqrst") == comparisonFeedback4:
                guesses.append(words[x])
            if len(guesses) > 5 or words[x] == hiddenWord:
                break

    if int(level) == 3:
        for x in range(len(words)):
            if generateFeedback(words[x], "abcde") == comparisonFeedback and \
                generateFeedback(words[x], "fghij") == comparisonFeedback2 and \
                generateFeedback(words[x], "klmno") == comparisonFeedback3:
                guesses.append(words[x])
            if len(guesses) > 5 or words[x] == hiddenWord:
                break

    if int(level) == 2:
        for x in range(len(words)):
            if generateFeedback(words[x], "abcde") == comparisonFeedback and \
                generateFeedback(words[x], "fghij") == comparisonFeedback2:
                guesses.append(words[x])
            if len(guesses) > 5 or words[x] == hiddenWord:
                break

    if int(level) == 1:
        for x in range(len(words)):
            if generateFeedback(words[x], "abcde") == comparisonFeedback:
                guesses.append(words[x])
            if len(guesses) > 5 or words[x] == hiddenWord:
                break

    for x in range(6):
        print(guesses[x])
        displayFeedback(generateFeedback(guesses[x], hiddenWord))
        if generateFeedback(guesses[x], hiddenWord) == "GGGGG":
             break

    return hiddenWord, guesses

if __name__ == "__main__":

    aiOrNot = input("AI (1) or play (2) ?")
    if aiOrNot == "1":
        aiLevel = input("Level of AI (1 - 5) ?")
        hiddenWord, guesses = playWordleAI(aiLevel)
    else:
        hiddenWord, guesses = playWordle() 
    print("The correct word was: ", hiddenWord)

    if hiddenWord not in guesses[len(guesses)-1]:
        print("You lost.")
    else:
        print("You won in "+str(len(guesses))+ " guesses!")

    print("Your guesses:", guesses)