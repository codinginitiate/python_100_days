
import random
word_list = ["aardvark"]
display = []

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

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
for letter in chosen_word:
    display.append("_")
while "_" in display:
    guessed_letter = input("Guess a letter: ").lower()
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

print("You win!")
