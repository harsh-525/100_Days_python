# TODO 1: open the letter template
with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    contents = letter.read()

# TODO 2: open the names
with open("./Input/Names/invited_names.txt", mode='r') as file:
    names = file.read()
    names = names.split("\n")

# TODO 3: Iterate over the names to generate new files
for name in names:
    file_name = "Letter_for_" + name + ".txt"
    with open(f"./Output/Ready_to_send/{file_name}", mode="w") as temp:
        # TODO 4: Write the contents replacing the name
        for _ in contents:
            if _ == 'X':
                temp.write(name)
            else:
                temp.write(_)
