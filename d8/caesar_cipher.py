alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_text = "" # blank str to place decoded/encoded message.

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# argument for parameter text_plain
text = input("Type your message:\n").lower()
# argument for parameter shift_amount
shift = int(input("Type the shift number:\n"))
# function to encode message
def encrypt(plain_text, shift_amount):
    new_text = ""
    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + shift_amount) % 26
            new_letter = alphabet[new_index]
            new_text += new_letter
        else:
            # If the character is not a letter (e.g., space or punctuation), leave it unchanged.
            new_text += letter
    return new_text
# function to decode message
def decrypt(plain_text, shift_amount):
    new_text = ""
    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index - shift_amount) % 26
            new_letter = alphabet[new_index]
            new_text += new_letter
        else:
            # If the character is not a letter (e.g., space or punctuation), leave it unchanged.
            new_text += letter
    return new_text
# determine which function to use
if direction == "encode":
    message = encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
    message = decrypt(plain_text = text, shift_amount = shift)
# if direction is wrong
else:
    message = "Sorry, try again."
# print returned encoded/decoded message
print(message)

def ceasar_cipher(coding_direction, plain_text, shift):
    new_text = ""
    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == "encode":
                new_index = (index + shift_amount) % 26
            else:
                new_index = (index - shift_amount) % 26
            new_letter = alphabet[new_index]
            new_text += new_letter
        else:
            # If the character is not a letter (e.g., space or punctuation), leave it unchanged.
            new_text += letter
    return new_text
