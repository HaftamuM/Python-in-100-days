alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction= input(f"Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input(f"Type your message:\n")
shift = int(input("Type the shift numbers:\n"))

#Todo-1 : Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs. 

if direction == 'encode':
    def encrypt(plain_text, shift_amount):
        cipher_text = ""
#Todo-2 : Inside the 'encrypt' function, shift each letter of the 'text' forware in the alphabet by the shift amout 
# and print the encypted text.   
        for letter in plain_text: 
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")
    

#Todo-3 :call the encrpt function and pass in the user inputs. you should be able to test the code and encrypt a message 
        encrypt(plain_text = text, shift_amount = shift)