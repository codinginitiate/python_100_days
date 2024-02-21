import random
import hangman_art
import hangman_words
word_list = ["aardvark"]
display = []
guesses = []
lives = 6
end_of_game = False

chosen_word = random.choice(word_list)
print(hangman_art.logo)
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
        pass
    if guessed_letter not in guesses:
        guesses += guessed_letter
    else:
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

    print(f"{' '.join(display)}")

    print(f"\n The letters you have used: {', '.join(guesses)}")

    if guessed_letter not in chosen_word:
        lives -= 1
    print(hangman_art.stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win!")

    if lives == 0:
        end_of_game = True
        print("You lose.")


