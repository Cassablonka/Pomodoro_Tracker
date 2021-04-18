# Importing the required packages
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#5b8a72"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    """This function resets the timer upon clicking the Reset button."""
    global reps
    reps = 0

    # Resetting everything on the screen
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label.config(text='Timer', fg=GREEN)
    check.config(text='', fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    """This function starts the timer upon clicking the Start button."""
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down((LONG_BREAK_MIN * 60))
        label.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        count_down((SHORT_BREAK_MIN * 60))
        label.config(text='Short Break', fg=PINK)
    else:
        count_down((WORK_MIN * 60))
        label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """This function takes work/short_break/long_break time as an argument in seconds
    and start the countdown in reverse."""

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            mark = ''
            sprints = math.floor(reps / 2)
            for i in range(sprints):
                mark += '✔'
            check.config(text=mark, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #

# Creating the Tkinter Window
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# Creating the Label on screen
label = Label(text='Timer', font=('Courier', 35, 'bold'), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)
label.config(padx=5, pady=20)

# Creating the canvas for image and text
canvas = Canvas(width=220, height=225, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(110, 112, image=image)
timer_text = canvas.create_text(110, 130, text='00:00', font=('Courier', 34, 'bold'), fill='white')
canvas.grid(column=1, row=1)

# Creating the start button
start_button = Button(text='Start', font=('Courier', 18, 'bold'), bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Creating the restart button
reset_button = Button(text='Reset', font=('Courier', 18, 'bold'), bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Creating Checkmark symbol
check = Label(font=('Courier', 35, 'bold'), bg=YELLOW, fg=GREEN)
check.grid(column=1, row=3)
check.config(padx=5, pady=10)

# To keep the window running
window.mainloop()
