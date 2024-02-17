
import random
word_list = ["aardvark"]
display = []

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
for letter in chosen_word:
    display.append("_")

guessed_letter = input("Guess a letter: ").lower()
'''
i=0
for letter in chosen_word:
  i += 1
  if guess == letter:
    display[i-1] = guess
for position in range(word_length):
    letter = chosen_word[position]
    if guessed_letter == letter:
        display[position] = guessed_letter
'''
# above code block can be used for this code block
for position in range(word_length):
    letter = chosen_word[position]
    if guessed_letter == letter:
        display[position] = guessed_letter

