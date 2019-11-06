# by Allison Dixon
# last updated November 6, 2019
# unit 7 daily exercises

# problem 1
original = "abcdefghij"
first = original[0:3]
last = original[3:]
final = first + last
print(final)

# problem 2
word = "Python"
for character in word:
    print(character)

# problem 3


def change(the_word):
    the_word = the_word[1:-1]
    return the_word


print(change("Hello"))
print(change("python"))
print(change("coding"))

# problem 4


def longest(list_words):
    biggest_word = ""
    for x in list_words:
        if len(x) > len(biggest_word):
            biggest_word = x
    return biggest_word


print(longest(["hi", "howdy", "hola", "bonjour", "yo"]))

# problem 5


def upper_lower():
    your_word = input("Give me a word.")
    print(your_word.upper())
    print(your_word.lower())


upper_lower()

# problem 6


def title_case():
    sentence = input("Give me a sentence.")
        sentence.split(" ")

    # split then join

