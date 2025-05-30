from tkinter import *
#import time
import  math

#from networkx.algorithms.distance_measures import radius

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 #25
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
text_mark = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_labels.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    print(reps)
    if reps == 8:
        count_down(long_break_min)
        timer_labels.config(text="Break", fg=RED)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_min)
        timer_labels.config(text="Break", fg=PINK)
    else:
        count_down(work_min)
        timer_labels.config(text="Work", fg=GREEN)

    """if reps % 8 == 0:
        count_down(long_break_min)
        timer_labels.config(text="Break", fg= RED)
    elif reps % 2 == 0:
        count_down(short_break_min)
        timer_labels.config(text="Break", fg=PINK)
    else:
        count_down(work_min)
        timer_labels.config(text="Work", fg=GREEN)"""


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    #print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        """if reps % 2 == 0:
            marks += text_mark
            checkmarks.config(text=marks)
        else:
            pass"""
        marks= ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += text_mark
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
spaces = " "
window.title(spaces * 50 + "Pomodoro")


#window.after(1000, )
#window.minsize(width=500, height=300)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=225, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill= "white", font=(FONT_NAME, 30, "bold"))
#canvas.pack()
canvas.grid(column=1, row=1)


timer_labels = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_labels.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks = Label(fg=GREEN, bg=YELLOW, font=("Arial", 15))
checkmarks.grid(column=1, row=3)



window.mainloop()
