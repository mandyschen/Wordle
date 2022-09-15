import random
from  wordlist_helper import getWordList

def aiPickGuess(numOfGuess, feedback, words, guessedWord):
    # if numOfGuess == 0:
    #     words.remove("audio")
    #     return [1, words, "audio"]

    blackLetter = []
    yellowLetter = []
    greenLetter = []

    for x in range(len(feedback)):
        if feedback[x] == "G":
            greenLetter.append(guessedWord[x])
        elif feedback[x] == "Y" and feedback[x] not in greenLetter:
            yellowLetter.append(guessedWord[x])
        else:
            blackLetter.append(guessedWord[x])

    print(blackLetter)
    print(yellowLetter)
    print(greenLetter)

    for x in range(len(words)-1, 0, -1):
        word = words[x]
        # print(word)
        # cont == True
        # while(cont == True):
        for y in range(len(blackLetter)):
            if word in words and blackLetter[y] in word:
                words.remove(word)
                break

        for a in range(len(greenLetter)):
            if word in words and greenLetter[a] not in word:
                words.remove(word)

        for b in range(len(yellowLetter)):
            if word in words and yellowLetter[b] not in word:
                words.remove(words[x])

            elif word in words and yellowLetter[b] == guessedWord[y]:
                words.remove(word)

    print(len(words))

    r = random.randrange(0, len(words))
    nextGuess = words[r]
    words.remove(nextGuess)

    numOfGuess += 1
    returnList = [numOfGuess, words, nextGuess]

    return returnList




    # for x in range(len(words)-1, 0, -1):
    #     word = words[x]
    #     if x < len(blackLetter) and blackLetter[y] in word:
    #         print("bl")
    #         print(x)
    #         words.remove(word)
    #         x+=1
    #     elif x < len(greenLetter) and greenLetter[a] not in word:
    #         print("gl")
    #         print(x)
    #         words.remove(word)
    #         x+=1
    #     elif x < len(yellowLetter) and yellowLetter[b] not in word:
    #         print("yl1")
    #         print(x)
    #         words.remove(words[x])
    #         x+=1
    #     elif x < len(yellowLetter) and yellowLetter[b] == guessedWord[y]:
    #         print("yl2")
    #         print(x)
    #         words.remove(word)
    #         x+=1


#
# numOfGuess = 0
# words = getWordList()
# nextGuess = ""
#
# returnList = aiPickGuess(0, "YBGYY", words, "HELLO")
#
# numOfGuess = returnList[0]
# words = returnList[1]
# nextGuess = returnList[2]
# #
# print("numGuess", numOfGuess, "word", words, "next", nextGuess)
