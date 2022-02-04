import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

keep_generating = True

while keep_generating:
    word = input("Enter a word to generate NATO phonetic alphabet or 'exit' to exit: ").upper()
    if word == "EXIT":
        keep_generating = False
    else:
        output_list = [phonetic_dictionary[letter] for letter in word]
        print(output_list)
