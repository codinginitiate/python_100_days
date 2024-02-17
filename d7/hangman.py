
import random
word_list = ["aardvark", "baboon", "camel"]
display = []

chosen_word = random.choice(word_list)

guessed_letter=input("Guess a letter: ").lower()
for letter in chosen_word:
    if guessed_letter == letter:
        print("Right")
    else:
        print("Wrong")
