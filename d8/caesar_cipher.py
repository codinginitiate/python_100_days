alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_text = "" # blank str to place decoded/encoded message.

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# argument for parameter text_plain
text = input("Type your message:\n").lower()
# argument for parameter shift_amount
shift = int(input("Type the shift number:\n"))

def ceasar_cipher(coding_direction, plain_text, shift_amount):
    new_text = ""
    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.index(letter)
'''
            if coding_direction == "encode":
                new_index = (index + shift_amount) % 26
            else:
                new_index = (index - shift_amount) % 26
'''
            if coding_direction = "decode":
                shift_amount *= -1
            new index = index + shift_amount
            new_letter = alphabet[new_index]
            new_text += new_letter
        else:
            # If the character is not a letter (e.g., space or punctuation), leave it unchanged.
            new_text += letter
    return new_text

# print returned encoded/decoded message
print(ceasar_cipher(coding_direction = direction, plain_text = text, shift_amount = shift ))
