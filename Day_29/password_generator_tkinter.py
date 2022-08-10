from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def auto_geneate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for _ in range(nr_letters)] + [choice(symbols) for _ in range(nr_symbols)] + [choice(numbers) for _ in range(nr_numbers)]
    shuffle(password_list)
    password_entry.insert(0, "".join(password_list))
    pyperclip.copy("".join(password_list))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def del_entries():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

def valid_fields():
    if website_entry.get() == '':
        messagebox.showerror(title="Field missing", message="Website field can't be empty")
        return False
    elif email_entry.get() == '':
        messagebox.showerror(title="Field missing", message="Email field can't be empty")
        return False
    elif password_entry.get() == '':
        messagebox.showerror(title="Field missing", message="Password field can't be empty")
        return False
    return True

def save_password():
    if valid_fields():
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"The entered details are:\n"
                                                                          f"Website: {website_entry.get()}\n"
                                                                          f"Email: {email_entry.get()}\n"
                                                                          f"Password: {password_entry.get()}\n"
                                                                          f"SAVE THEM????")
        if is_ok:
            new_data = {
                website_entry.get(): {
                    "email": email_entry.get(),
                    "password": password_entry.get()
                }
            }
            try:
                with open("password_file.json", mode="r") as file:
                    data = json.load(file)  #read the json file ~ json->dictionary
                    data.update(new_data)
                    new_data = data
            except FileNotFoundError:
                print("File not found. Creating a new file")
            except:
                print("Empty file; populating with the data")
            finally:
                with open("password_file.json", mode="w") as file:
                    # file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                    json.dump(new_data, file, indent=4)
                    messagebox.showinfo(title="SAVED PASSWORD", message="Details saved")
                    del_entries()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(column=1, row=0)

website = Label(text="website: ", font=(FONT_NAME, 15), highlightthickness=0)
website.grid(column=0, row=1)
website_entry = Entry(width=35, highlightthickness=1)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()  # auto cursor i=on launch

email = Label(text="Email/Username: ", font=(FONT_NAME, 15), highlightthickness=0)
email.grid(column=0, row=2)
email_entry = Entry(width=35, highlightthickness=1)
email_entry.grid(column=1, row=2, columnspan=2)

password = Label(text="Password: ", font=(FONT_NAME, 15), highlightthickness=0)
password.grid(column=0, row=3)
password_entry = Entry(width=18, highlightthickness=1)
password_entry.grid(column=1, row=3)
generate_password = Button(text="Generate Password", highlightthickness=0, command=auto_geneate_password)
generate_password.grid(column=2, row=3)

add_password = Button(text="ADD", width=20, highlightthickness=0, command=save_password)
add_password.grid(column=1, row=4, columnspan=2)
window.mainloop()
