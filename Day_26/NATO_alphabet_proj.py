import pandas as pd

data = pd.read_csv('NATO-alphabet-start/nato_phonetic_alphabet.csv')

# TODO 1: Create a dictionary of NATO alphabets
nato_dict = {rows.letter: rows.code for (index, rows) in data.iterrows()}
# print(nato_dict)

# TODO 2: Create a list of NATO words from User input
user_input = input("Type a word containing only letters: ")
result = [nato_dict[_.upper()] for _ in user_input]
print(result)
