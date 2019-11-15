# by Allison Dixon
# last updated November 15, 2019
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
    your_list = sentence.split(" ")
    new_list = []
    for your_word in your_list:
        title_your_word = your_word[0].upper() + your_word[1:]
        new_list.append(title_your_word)
    phrase = " ".join(new_list)
    return phrase


print(title_case())

# problem 7


def replace(your_sentence):
    split_sentence = your_sentence.split(" ")
    the_new_list = []
    for each_word in split_sentence:
        if len(each_word) == 4:
            each_word = "#$%@"
            the_new_list.append(each_word)
        else:
            the_new_list.append(each_word)
    new_phrase = " ".join(the_new_list)
    return new_phrase


print(replace("Scout is a fake friend."))

# problem 8


def bubble_sort(names):
    switched = True
    while switched:
        switched = False
        swaps = 0
        for x in range(len(names)-1):
            if names[x] > names[x + 1]:
                switched = True
                temp = names[x + 1]
                names[x + 1] = names[x]
                names[x] = temp
                swaps += 1
    return names


print(bubble_sort(["Liana", "Allison", "Ariana", "Scout"]))
