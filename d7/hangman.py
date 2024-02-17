
import random
word_list = ["aardvark", "baboon", "camel"]
display = []

chosen_word = random.choice(word_list)
for letter in chosen_word:
    display.append("_")

guessed_letter=input("Guess a letter: ").lower()
for letter in chosen_word:
    if guessed_letter == letter:
        display[chosen_word.index(letter)] = guessed_letter

print(display)
