from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

#----window setup----#
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg= YELLOW)

#----canvas setup---#
tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100,130,text="00:00",fill="white", font = (FONT_NAME,35,'bold'))


#----labels setup---#
timer_label = Label(text = "Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50,'bold'))
checkmark_label = Label(text = "✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME,35,'bold'))

#----buttons setup---#
start_button = Button(text="Start",width=5,height=2,font=(FONT_NAME,10,'bold'))
reset_button = Button(text="Reset",width=5,height=2,font=(FONT_NAME,10,'bold'))

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