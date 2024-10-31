import random

word_list = ['apples', 'bananas', 'oranges', 'grapefruits', 'grapes']

def random_choice():
    word = random.choice(word_list)
    return word

word = random_choice()
print(word)

def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
    while True:
        guess = input('Please guess a letter: ')
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()
