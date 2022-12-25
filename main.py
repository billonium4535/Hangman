from collections import Counter

# Reads all english words into word_array
file = open("english.txt", "r")
word_array = []
for word in file:
    word_array.append(word.strip())
file.close()

# Defines arrays, variables and dictionaries
letter_frequency = {}
guess_word = ""
guessed_letters = []
wrong_letters = []

# User inputs how many letters their word is
print("How many letters is your word?")
word_length = int(input(">"))


def remove_len_words():
    wrong_words = []
    for current_word in word_array:
        if len(current_word) != word_length:
            wrong_words.append(current_word)
    while len(wrong_words) != 0:
        word_array.remove(wrong_words[0])
        wrong_words.remove(wrong_words[0])


remove_len_words()

guess_word = "_" * word_length  # test word "poppy"


# Function to replace _ characters with correct letters
def replace(original_string, index, new_character):
    chars = list(original_string)
    chars[index] = new_character
    new_string = "".join(chars)
    return new_string


# function to output table for user
def print_table():
    print(" " + "_ _ " * word_length)
    for k in range(word_length):
        print("| " + "{} ".format(guess_word[k]), end="")
    print("|")
    for i in range(1, word_length + 1):
        if i < 10:
            print(" ", i, end=" ")
        elif i == 10:
            print(" ", i, end=" ")
        else:
            print(" " + str(i), end=" ")
    print("\n")


def fill_in_letters(letter):
    global guess_word

    print("How many '{}'s are there in your word?".format(letter))
    for j in range(int(input(">"))):
        print("Enter occurrence {}".format(j + 1))
        position = input(">")
        guess_word = replace(guess_word, int(position) - 1, letter)
        print_table()
    remove_right_letters(letter)


def remove_wrong_letters(removed_letter):
    wrong_words = []
    for current_word in word_array:
        if removed_letter in current_word:
            wrong_words.append(current_word)
    while len(wrong_words) != 0:
        word_array.remove(wrong_words[0])
        wrong_words.remove(wrong_words[0])


def remove_right_letters(removed_letter):
    global guess_word

    wrong_words = []
    for current_word in word_array:
        if removed_letter not in current_word:
            wrong_words.append(current_word)
        elif [pos for pos, char in enumerate(current_word) if char == removed_letter] != [pos for pos, char in enumerate(guess_word) if char == removed_letter]:
            wrong_words.append(current_word)

    while len(wrong_words) != 0:
        word_array.remove(wrong_words[0])
        wrong_words.remove(wrong_words[0])

    print("Possible words: {}".format(word_array))


def count_letters():
    global letter_frequency

    for current_word in word_array:
        for letter in current_word:
            if letter not in guessed_letters:
                if letter in letter_frequency:
                    letter_frequency[letter] += 1
                else:
                    letter_frequency[letter] = 1
    print(letter_frequency)

    highest_letter = str(Counter(letter_frequency).most_common()[1]).split(", ")[0].strip("('")
    guessed_letters.append(highest_letter)

    print("does your word have an '" + highest_letter + "' in it?")
    if input("y/n >").lower() == "y":
        fill_in_letters(highest_letter)
    else:
        wrong_letters.append(highest_letter)
        remove_wrong_letters(highest_letter)

    letter_frequency = {}


def main_game():
    while len(guess_word.replace("_", "")) != word_length:
        print_table()
        count_letters()


main_game()
