alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_text = ""
'''
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
'''
text = "hello"
shift = 3
def encrypt(text):
    for letter in text:
        for i in range(0,26):
            if letter == alphabet[i]:
                new_letter = alphabet[i+shift]
                new_text += new_letter



    return new_text




print(encrypt(text))

