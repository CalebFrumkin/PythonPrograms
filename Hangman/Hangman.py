import random
import sys

start=input('Welcome to Hangman.\nWould you like to play?:(y/n)')
if start!='y':
    exit()
while True:
    words=open('Words.txt').readlines()
    guessesleft=int(input('How many incorrect guesses would you like?:'))
    usedword=words[random.randint(0,len(words)-1)]
    wordsplit=list(usedword)
    hiddensplit=list(usedword)
    wordsplit.remove('\n')
    hiddensplit.remove('\n')
    for i in range(len(hiddensplit)):
        if hiddensplit[i]!=' ':
            hiddensplit[i]='_'
    print('Here is your phrase:\n',' '.join(hiddensplit),'\nYou have',guessesleft,'wrong guesses available.')
    while True:
        change=0
        guess=input('Enter your guess:')
        for i in range(len(wordsplit)):
            if guess==wordsplit[i]:
                hiddensplit[i]=guess
                change=1
        if change==0:
            guessesleft=guessesleft-1
        print(' '.join(hiddensplit),'\nYou have',guessesleft,'wrong guesses left.')
        if guessesleft<1:
            print('Game Over!\nYour phrase was:',usedword)
            if input('play again?: (y/n)')=='n':
                exit()
            break
        if '_' not in hiddensplit:
            print('Congratulations! Your phrase was:',usedword)
            if input('play again?: (y/n)')=='n':
                exit()
            break
