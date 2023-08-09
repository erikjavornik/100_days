import pandas

data = pandas.read_csv("./Day_30_Errors_and_JSON/nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

loop = True

while loop:
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
    else:
        print(output_list)
        loop = False

