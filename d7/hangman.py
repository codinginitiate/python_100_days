
import random
word_list = ["aardvark", "baboon", "camel"]
display = []

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
for letter in chosen_word:
    display.append("_")

while "_" in display:
    guessed_letter = input("Guess a letter: ").lower()
    '''
    for position in range(word_length):
        letter = chosen_word[position]
        if guessed_letter == letter:
            display[position] = guessed_letter
    '''
    # above code block can be used for this code block
    for letter in chosen_word:
        if guessed_letter == letter:
            display[chosen_word.index(letter)] = guessed_letter
    vprint(display)
print("You win!")
