
print("")
print("""\
        /$$
        | $$
        | $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$
        | $$__  $$ |____  $$| $$__  $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$__  $$
        | $$  \ $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$  \ $$
        | $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$  | $$
        | $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$  | $$
        |__/  |__/ \_______/|__/  |__/ \____  $$|__/ |__/ |__/ \_______/|__/  |__/
                                    /$$  \ $$
                                    |  $$$$$$/
                                    \______/
""")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
word_list = ["aardvark"]
display = []
guesses = []
lives = 6
end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
for letter in chosen_word:
    display.append("_")


while not end_of_game:
    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in guesses:
        print("You have used that letter already. Choose again.")
        pass

    '''
    i=0
    for letter in chosen_word:
    i += 1
    if guess == letter:
        display[i-1] = guess
    '''
    # above code block can be used for below code block
    for position in range(word_length):
        letter = chosen_word[position]
        if guessed_letter == letter:
            display[position] = guessed_letter

    print(display)

    print(f"\n The letters you have used: {guesses}")

    if guessed_letter not in chosen_word:
        lives -= 1
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win!")

    if lives == 0:
        end_of_game = True
        print("You lose.")


