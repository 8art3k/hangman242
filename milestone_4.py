import random

word_list = ['apples', 'bananas', 'oranges', 'grapefruits', 'grapes']

def random_choice():
    word = random.choice(word_list)
    return word

word = random_choice()

class Hangman():
    def __init__ (self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word 
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

        

    def check_guess(self,guess):
        guess.lower()
        if guess in word:
            print(f'Good guess! {guess} is in the word.')
            for idx, letter in enumerate(self.word):
                if letter == guess:
                   self.word_guessed[idx] == guess 
            self.num_letters -= 1
            print(self.word_guessed)    #added line
        else:
            print(f'Sorry, {guess} is not in the word.')
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        while True:
            guess = input('Please guess a letter: ')
            if not guess.isalpha() or len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)        
        
game1 = Hangman(word_list)
print(game1.word)
print(game1.word_guessed)
print(game1.num_lives)
print(game1.num_letters)
print(game1.list_of_guesses)

game1.ask_for_input()

