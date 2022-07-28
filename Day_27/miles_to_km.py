from tkinter import *


def action():
    val = float(entry.get())
    res['text'] = val*1.609

#Creating a new window and configurations
window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=230, height=200)


# entry
entry = Entry(width=10)
entry.insert(END, string="enter")
entry.grid(column=2, row=0)

label_1 = Label(text="miles")
label_1.grid(column=3, row=0)

label_2 = Label(text="is_equal_to")
label_2.grid(column=0, row=1)
label_3 = Label(text="kms")
label_3.grid(column=3, row=1)

res = Label(text="_")
res.grid(column=2, row=1)

button = Button(text="convert", command=action)
#button.pack()
button.grid(column=2,row=2)

window.mainloop()