from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    reps = 0
    window.after_cancel(timer)
    label_1.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_title, text=f"{WORK_MIN}:00")
    label_2.config(text=" ")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        label_1.config(text="LONG BREAK", fg=GREEN)
        timer_start(long_break_sec)
        reps = 0
    elif reps % 2 == 0:
        label_1.config(text="WORK", fg=RED)
        timer_start(work_sec)
    else:
        label_1.config(text="SHORT BREAK", fg=PINK)
        timer_start(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer_start(count):
    global reps, timer
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = "0"+str(count_seconds)

    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"

    if not count < 0:
        canvas.itemconfig(timer_title, text=f"{count_minutes}:{count_seconds}")
        timer = window.after(1000, timer_start, count-1)
    else:
        reps += 1
        if not reps % 2 == 0:
            label_2.config(text="✔︎"*int(reps / 2 + 1))
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
#Creating a new window and configurations
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_title = canvas.create_text(100, 130, text=f"{WORK_MIN}:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
#canvas.pack()

label_1 = Label(text="TIMER", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 35), highlightthickness=0)
label_1.grid(column=1, row=0)

start = Button(text="start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

label_2 = Label(text=" ︎", foreground=RED, bg=YELLOW, font=(FONT_NAME, 35), highlightthickness=0)
label_2.grid(column=1, row=3)

window.mainloop()
