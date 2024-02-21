alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_text = ""

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    new_text = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + shift) % 26
            new_letter = alphabet[new_index]
            new_text += new_letter
        else:
            # If the character is not a letter (e.g., space or punctuation), leave it unchanged.
            new_text += letter
    return new_text

if direction == "encrypt":
    message = encrypt(text, shift)

print(message)
