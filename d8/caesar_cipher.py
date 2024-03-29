alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_text = "" # blank str to place decoded/encoded message.

from art import logo
print(logo)

should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # argument for parameter text_plain
    text = input("Type your message:\n").lower()
    # argument for parameter shift_amount
    shift = int(input("Type the shift number:\n"))

    def ceasar_cipher(coding_direction, plain_text, shift_amount):
        new_text = ""
        if coding_direction == "decode":
            shift_amount *= -1 # used to change shift_amount to negative number, so only one line of code is needed at line 17
        for char in plain_text:
            if char in alphabet:
                index = alphabet.index(char)
                new_index = (index + shift_amount) % 26
                new_letter = alphabet[new_index]
                new_text += new_letter
            else:
                # If the character is not a letter (e.g., space or punctuation), leave it unchanged.
                new_text += char
        return new_text

    # print returned encoded/decoded message
    print(ceasar_cipher(coding_direction = direction, plain_text = text, shift_amount = shift ))

    answer = input("Do you wish to continue? (yes or no) ")
    if answer == 'no':
        should_end = True
        print("Goodbye")
