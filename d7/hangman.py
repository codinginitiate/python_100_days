
import random
word_list = ["aardvark", "baboon", "camel"]
display = []

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
for letter in chosen_word:
    display.append("_")

guessed_letter=input("Guess a letter: ").lower()
for position in range(word_length)
    for letter in chosen_word:
        if guessed_letter == letter:
            display[position] = guessed_letter


print(display)
