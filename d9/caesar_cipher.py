alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
position_1 = ""
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
                position_1 += new_letter



    return position_1




print(encrypt(text))

