import random

# The List of random words

from Hangman_word_list import word_list
from Hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Print the logo

print(logo)

# Code Testing

print(f'This is the chosen word {chosen_word}')

# Create the Blank space
display = []
for i in range(word_length):
    display += '_'

while not end_of_game:
    guess = input('Guess a letter: ').lower()

    if guess in display:
        print(f'you have already guessed letter: {guess}')
    #
    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter

    if guess not in chosen_word:
        print(f'The guessed letter {guess}, not in the word you loose a life.')
        # If lives are zero you loose
        lives -= 1
        # This will check if u have any life left
        if lives == 0:
            end_of_game = True
            print('You Loose!!')
        # If all blanks in display are filled you won without dying.
        if '_' not in display:
            end_of_game = True
            print('You WOn !!!!!')
        # this will show the stage of live you left
        print(stages[lives])
