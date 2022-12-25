word_list = open("english.txt", "r")
word_array_file = open("english_array.txt", "w")

word_array = []

for word in word_list:
    word_array.append(word.strip())

print(word_array)

# word_array_file.write((str(word_array)).replace('\\n', ''))
