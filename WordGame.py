'''

Programmer: Baadshah Verma
Date: October 5th, 2018

This program is a word game. The user is given two letters to start, which they
will have to take and come up with a word that starts with the first letter and
ends with the second letter. This word will be validated to see if it is in the
list of cleansed words and scored accordingly. The score will be kept throughout
the game.

'''

#import necessary modules to begin program
import urllib.request
import random

#reads file from the webpage and stores all words into a list
def readWordList():
    response = urllib.request.urlopen("http://www.mit.edu/~ecprice/wordlist.10000")
    html = response.read()
    data = html.decode('utf-8').split()
    return data

#cleans list up and appends valid words to new_list
def cleanse(data = readWordList()):
    new_list = []
    for word in data:
        if len(word) >= 1 and len(set(word)) >= 2: #adds words according to criteria
            new_list.append(word)
        elif len(word) == 1 and len(set(word)) == 1:
            new_list.append(word)
    return new_list

#tests the cleanse function with a list of different cases - prints result
def test():
    cleanedList = cleanse(['aa','bcds','hello','jury','bbb'])
    print(cleanedList)

#chooses a random letter from the alphabet and returns it
def randomNum():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    position = random.randint(0,25) 
    letter = alphabet[position] #selecting letter based upon random index number
    return letter

#criteria to gainpoints
def gainPoints(wordGuess, letterA, letterB):
    new_list = cleanse()
    
    roundScore = 0
    gameScore = 0
    letter_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1, 'f': 5, 'g': 2, 'h': 3, 'i': 1, 'j': 9, 'k': 5, 'l': 1, 'm': 2, 'n': 2, 'o': 1, 'p': 4, 'q': 15, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 8, 'w': 4, 'x': 15, 'y': 4, 'z': 15} 

    #premium added for words over 6 letters 
    if len(wordGuess) == 6:
        roundScore = roundScore + 3
    elif len(wordGuess) == 7:
        roundScore = roundScore + 4
    elif len(wordGuess) == 8:
        roundScore = roundScore + 5
    elif len(wordGuess) > 8:
        roundScore = roundScore + 6
    else:
        if letterA == letterB:  #checking if first and last letters are the same; bonus 10 points
            roundScore = roundScore + 10

    #checks every letter in wordGuess for letter_values, adding each value to the roundScore
    for letter in wordGuess:
        for key in letter_values:
            if letter == key:
                roundScore = roundScore + letter_values[key]
    gameScore = gameScore + roundScore

    #print out round and overall game score
    print("Your score this round is: " + str(roundScore))
    print("Your overall score this round is: " + str(gameScore))

#criteria to losepoints
def losePoints(wordGuess,letterA,letterB):
    new_list = cleanse()
    roundScore = 0
    gameScore = 0

    #score reduced for stated criterion
    if wordGuess not in new_list:
        roundScore = roundScore - 10
    elif wordGuess[0] != letterA and wordGuess[-1] != letterB:
        roundScore = roundScore - 2
    else:
        if wordGuess[0] != letterA or wordGuess[-1] != letterB:
            roundScore = roundScore - 2
    gameScore = gameScore + roundScore

    #print out round and overall game score
    print("Your score this round is: " + str(roundScore))
    print("Your overall score is: " + str(gameScore))

#this runs and initiatiates the game. The user is asked for an input and it is put through scoring criteria
def userTurn():
    print("Welcome to the word game! I hope you have fun!")
    new_list = cleanse()

    #loop to initiate 5 rounds
    for i in range(5):

        #random first and last letter
        letterA = randomNum()
        letterB = randomNum()

        #gets word input from user 
        wordGuess = input("Enter a word that begins with " + letterA + " and ends with " + letterB + ": ")        

        #checks if word is in list or not and calculates score by calling appropriate function
        if wordGuess in new_list:
            gainPoints(wordGuess,letterA,letterB)
            print("This word is valid, congrats")
            userMove = input("Would you like to 'Continue' or 'Quit' ? ")
            if userMove == "Continue":
                print("Moving to the next round")
                continue
            #assume that if you get the word wrong, the game ends
            else:
                print("Good Game!")
                return
        else:
            losePoints(wordGuess,letterA,letterB)
            print("This word is invalid")
            print("Good Game!")
            return

userTurn()