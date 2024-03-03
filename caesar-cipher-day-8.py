#100 days of code: The copmplete Python Pro Bootcamp

#Caesar cipher - day 8 project


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift_amount):
    caesar_text = ""
    for character in text:
        if character in alphabet:
            position = alphabet.index(character)
            if direction == "encode":
                new_position = position + shift_amount
                if new_position > 25:
                    new_letter = alphabet[new_position - 26]
                else:
                    new_letter = alphabet[new_position]
            elif direction == "decode":
                new_position = position - shift_amount
                if new_position < 0:
                    new_letter = alphabet[new_position + 26]
                else:
                    new_letter = alphabet[new_position]
            caesar_text += new_letter
        else:
            caesar_text += character
    print(f"Text after changes is: {caesar_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
            
    caesar(direction, text, shift_amount=shift)

    restart = input('Do you want to restart the program? Type "yes" or "no": ').lower()
    if restart == "no":
        break
    print("\n")

        

