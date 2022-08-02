alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt and 'decode to decrypt.\n")
text = input("Type your message here:\n").lower()
shift = int(input("Type the shift number:\n"))


# Function for Encoding the words given as input
def encrypt(plain_text, shift_amount=0):
    """
    Inside this function, shift each letter of the 'text' forwards in the alphabetical order by shifting the shift
    amount and print the encrypted text.

    :param plain_text:
    :param shift_amount:
    :return: str:
    """
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"The Encoded Text is {cipher_text}")
    # return cipher_text


def decrypt(cipher_text, shift_amount=0):
    """
        Inside this function, shift each letter of the 'text' backward in the alphabetical order by shifting the shift
        amount and print the decrypted text.

        :param cipher_text:
        :param shift_amount:
        :return: str:
        """
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter

    print(f"The Decoded text is {plain_text}")
    # return plain_text


if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)

elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)
