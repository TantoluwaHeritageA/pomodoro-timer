from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 25
LONG_BREAK_MIN = 20
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text , text="00:00")
    label_title.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0
    # timer_text = 00:00
    # title_label = "Timer
    # reset check marks


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1  # first repetition

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # if it's the 8th rep:
        count_down(long_break_sec)
        label_title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # if it's 2nd/4th/6th rep:
        count_down(short_break_sec)
        label_title.config(text="Break", fg=PINK)
    else:
        # if it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        label_title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global my_timer
    # print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # if count_sec == 0:
    #     count_sec = "00"

    canvas.itemconfig(timer_text , text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = window.after(1000 , count_down , count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50 , bg=YELLOW)

# after 1 second, call function, then pass in "hello"
# def say_something(thing):
#     print(thing)
# window.after(1000,say_something,"Hello")


label_title = Label(text="Timer" , font=(FONT_NAME , 50) , fg=GREEN , bg=YELLOW)
label_title.grid(column=1 , row=0)

canvas = Canvas(width=202 , height=224 , bg=YELLOW , highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100 , 112 , image=tomato_img)
timer_text = canvas.create_text(100 , 130 , text="00:00" , fill="white" , font=(FONT_NAME , 35 , "bold"))
canvas.grid(column=1 , row=1)

start_button = Button(text="Start" , highlightthickness=0 , command=start_timer)
start_button.grid(column=0 , row=2)

reset_button = Button(text="Reset" , highlightthickness=0,command=reset_timer)
reset_button.grid(column=3 , row=2)

check_label = Label( fg=GREEN , bg=YELLOW)
check_label.grid(column=1 , row=3)

window.mainloop()
