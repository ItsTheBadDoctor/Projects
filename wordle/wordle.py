import re

def load_word_list(filename):
    with open(filename, "r") as words_file:
        return [word.strip() for word in words_file]

wordList = load_word_list("wordle-La.txt")

def input_guess():
    while True:
        guess = input("What is your guess? ").lower()
        if re.match("^[a-z]{5}$", guess):
            return guess
        else:
            print("Please ensure your guess is 5 letters long and only contains letters.")

def result(guess, wordList):
    while True:
        result = input("What was the result? ").lower()
        if all(letter in "byg" for letter in result):
            break
        else:
            print("Please ensure your result only uses b, y, and g. A proper entry looks like: bbybg")

    newWordList = wordList.copy()
    for i in range(5):
        if result[i] == 'g':
            newWordList = [word for word in newWordList if word[i] == guess[i]]
        elif result[i] == 'y':
            newWordList = [word for word in newWordList if guess[i] in word and word[i] != guess[i]]
        else:
            newWordList = [word for word in newWordList if word.count(guess[i]) <= guess.count(guess[i]) - 1]
    
    return newWordList

for i in range(6):
    wordList = result(input_guess(), wordList)
    if len(wordList) == 1:
        print(f"The solution is: {wordList[0]}")
        break
    print(wordList)
