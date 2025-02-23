#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    return letter in word

    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    return word[spot] == letter 

    return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback = []
    for i, letter in enumerate(myGuess):
        if inSpot(letter, word, i): 
            feedback.append(letter.upper())
        elif inWord(letter, word):
            feedback.append(letter.lower())
        else:
            feedback.append('*')
    return ''.join(feedback)


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    #User should get 6 guesses to guess
    for attempt in range(6): 
        guess = input(f"Attempt {attempt + 1}/6 - Enter your 5-letter word guess: ").strip().lower()

        if len(guess) != len(todayWord): 
            print("Invalid input.")
            continue 

        feedback = rateGuess(guess, todayWord)
        print("Feedback:", feedback)

        if guess == todayWord: 
            print("Congratulations")
            return 

    #Ask user for their guess
    #Give feedback using on their word:





if __name__ == '__main__':
  main()
