# created by Allison Dixon
# last modified November 12, 2019
# unit 7 project

alphabet = "abcdefghijklmnopqrstuvwxyz"
encoded_word = []


def shift():
    user_shift = int(input("How many letters do you want to shift the alphabet?"))
    first = alphabet[0:user_shift]
    last = alphabet[user_shift:]
    alphabet_two = last + first
    return alphabet_two


def encode(new_alphabet):
    user_word = input("What word do you want to encode?")
    user_word = user_word.lower()
    for letter in user_word:
        position = alphabet.index(letter)
        position_final = new_alphabet[position]
        encoded_word.append(position_final)
        final_encoded = "".join(encoded_word)
    print(final_encoded)


def main():
    new_alphabet = shift()
    user_input = input("Press 'e' to encode, 'd' to decode, or 'q' to quit.")
    encode(new_alphabet)


main()

