# created by Allison Dixon
# last modified November 14, 2019
# unit 7 project

alphabet = "abcdefghijklmnopqrstuvwxyz"
encoded_word = []
decoded_word = []


def shift():
    """
    This function shifts the alphabet however much the user wants.
    :return: the new alphabet
    """
    user_shift = int(input("How many letters do you want to shift the alphabet (1-25)?"))
    first = alphabet[0:user_shift]
    last = alphabet[user_shift:]
    alphabet_two = last + first
    return alphabet_two


def encode():
    """
    This function takes a word or sentence from the user and encodes it using the shifted alphabet and prints it.
    :return: nothing
    """
    new_alphabet = shift()
    user_word = input("What word do you want to encode?")
    user_word = user_word.lower()
    final_encoded = ""
    for letter in user_word:
        if letter not in alphabet:
            encoded_word.append(letter)
        else:
            position = alphabet.index(letter)
            position_final = new_alphabet[position]
            encoded_word.append(position_final)
        final_encoded = "".join(encoded_word)
    print(final_encoded)


def decode():
    """
    This function takes an encoded word or sentence from the user and decodes it and prints it.
    :return: nothing
    """
    new_alphabet = shift()
    user_decode_word = input("What word do you want to decode?")
    user_decode_word = user_decode_word.lower()
    final_decoded = ""
    for letter in user_decode_word:
        if letter not in alphabet:
            decoded_word.append(letter)
        else:
            position = new_alphabet.index(letter)
            position_final = alphabet[position]
            decoded_word.append(position_final)
        final_decoded = "".join(decoded_word)
    print(final_decoded)


def main():
    while True:
        user_input = input("Press 'e' to encode, 'd' to decode, or 'q' to quit.")
        if user_input == "e":
            encode()
        elif user_input == "d":
            decode()
        elif user_input == "q":
            print("Thanks anyways.")
            break


main()
