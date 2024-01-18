from art import alphabet 

direction= input(f"Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input(f"Type your message:\n").lower()
shift = int(input("Type the shift numbers:\n"))
 ## combine this to a 1 function when u get the time 

def encrypt (plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text: 
        position = alphabet.index(letter)
        new_position = position + shift_amount 
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt (plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount 
        new_letter = alphabet[new_position]
        cipher_text += new_letter 
    print(f"The decoded text is {cipher_text}")

if direction == 'encode'.lower(): 
    encrypt (plain_text = text,shift_amount = shift)
elif direction == "decode".lower():
    decrypt (plain_text = text,shift_amount = shift)

