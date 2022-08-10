import pandas as pd

data = pd.read_csv('NATO-alphabet-start/nato_phonetic_alphabet.csv')

# TODO 1: Create a dictionary of NATO alphabets
nato_dict = {rows.letter: rows.code for (index, rows) in data.iterrows()}


# print(nato_dict)

def generate_phonetic():
    # TODO 2: Create a list of NATO words from User input
    user_input = input("Type a word containing only letters: ")
    try:
        result = [nato_dict[_.upper()] for _ in user_input]
    except KeyError as msg:
        print(f"Missing key={msg}")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
