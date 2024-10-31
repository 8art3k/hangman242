import random

def random_choice():
    word = random.choice(word_list)
    return word

word_list = ['apples', 'bananas', 'oranges', 'grapefruits', 'grapes']

guess = input('Enter a single letter: ')


if len(guess) == 1 and guess.isalpha() == True:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
    

        
