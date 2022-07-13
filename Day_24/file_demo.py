file = open("my_file.txt")  # open hte file
contents = file.read()  # read the file contents
print(contents)  # print the contents
file.close()  # close the opened file - need to avoid resources wastage

#  'with' helps in automatic closing of file
with open("new_file.txt", mode="w") as file:  # modes = r, w, a
    for _ in range(10):
        file.write(f"{_}")

with open("./Input/Letters/starting_letter.txt", mode="w") as file:
    file.write("Dear X\nYou are invited to my birthday this saturday\nHope you can make it!\nAngela")


