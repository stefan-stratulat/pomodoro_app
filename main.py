from tkinter import *
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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps +=1

    work_sec = 25 #WORK_MIN * 60
    short_break_sec = 5 #SHORT_BREAK_MIN * 60
    long_break_sec = 20 #LONG_BREAK_MIN * 60

    #if it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = "Break", fg=RED, bg=YELLOW, font=(FONT_NAME,50,'bold'))
    #if it's the 2nd/4th/6th
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text = "Break", fg=PINK, bg=YELLOW, font=(FONT_NAME,50,'bold'))
    else:
    #if it's the 1st/3rd/5th/7th rep
        count_down(work_sec)
        timer_label.config(text = "Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50,'bold'))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count/ 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0"+str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()
        global reps
        marks = " "
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        checkmark_label.config(text = marks, fg=GREEN, bg=YELLOW, font=(FONT_NAME,35,'bold'))


# ---------------------------- UI SETUP ------------------------------- #

#----window setup----#
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg= YELLOW)


#----canvas setup---#
tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white", font = (FONT_NAME,35,'bold'))

#----labels setup---#
timer_label = Label(text = "Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50,'bold'))
checkmark_label = Label(text = "", fg=GREEN, bg=YELLOW, font=(FONT_NAME,35,'bold'))

#----buttons setup---#
start_button = Button(text="Start",font=(FONT_NAME,10,'bold'),command=start_timer)
reset_button = Button(text="Reset",font=(FONT_NAME,10,'bold'))

#----grid setup----#
#column 0
start_button.grid(row=3,column = 0)
#column 1
timer_label.grid(row=0,column=1)
canvas.grid(row=1,column=1)
checkmark_label.grid(row=4,column=1)
#column 2
reset_button.grid(row=3,column=2)


window.mainloop()