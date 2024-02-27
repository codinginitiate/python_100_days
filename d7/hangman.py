import random
import hangman_art
import hangman_words
import pyfiglet
import os

os.system('clear')

word_list = hangman_words.word_list
guesses = []
display  = []
lives = 6
end_of_game = False

chosen_word = random.choice(word_list)

result = pyfiglet.figlet_format("hangman", font = "big" )
print(result)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

word_length = len(chosen_word)
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guessed_letter = input("Guess a letter: ").lower()
    print("")


    if guessed_letter in guesses:
        print("You have used that letter already. Choose again.")
        print(f"The letters you have used: {', '.join(guesses)}\n")
        continue
    if guessed_letter not in guesses:
        guesses += guessed_letter

    '''
    i=0
    for letter in chosen_word:
        if guess == letter:
            display[i] = guess
        i += 1
    '''

    # above code block can be used for below code block
    for position in range(word_length):
        letter = chosen_word[position]
        if guessed_letter == letter:
            display[position] = guessed_letter

    print(f"{' '.join(display)}")

    print(f"\n The letters you have used: {', '.join(guesses)}")

    if guessed_letter not in chosen_word:
        lives -= 1
    print(hangman_art.stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win!\n")

    if lives == 0:
        end_of_game = True
        print("You lose.")
        print(f"The word was '{chosen_word}'\n")


