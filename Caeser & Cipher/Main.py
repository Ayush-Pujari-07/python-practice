alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

condition = "yes"


# Function for Encoding and decoding the words given as input
def caesar(start_text, shift_amount, cipher_direction):
    """
    This will allow the user to encode or decode the code with the desired direction provided.
    :param start_text:
    :param shift_amount:
    :param cipher_direction:
    :return:
    """
    end_text = ""

    if cipher_direction == 'decode':
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"The {cipher_direction}d text is {end_text}")


while condition == 'yes':

    direction = input("Type 'encode' to encrypt and 'decode to decrypt.\n")
    text = input("Type your message here:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    condition = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if condition == 'no':
        print("Goodbye")
        break
    else:
        continue
