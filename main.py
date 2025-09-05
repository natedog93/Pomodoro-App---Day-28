from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
"""
Below codes are pulling from color pallet website, which you can alter if you would like
"""
PINK = "#e2979c"
RED = "#DC2525"
GREEN = "#06923E"
YELLOW = "#f7f5dd"
FONT_NAME = "Helvetica"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(1500)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
"""
Think of a GUI program as Even Driven program, meaning it has to be receptive to user interaction, such as the click of
a button or mouse movement. You cannot sleep the screen or use the import time module above as you need to be able to stop, start, 
or reset the program when the GUI is interacted with. This program is driven through our .mainloop() at the end of code.
"""
def count_down(count):
    #calculating what the count is equivalent to in minutes and seconds and - 1 sec each time
    count_min = math.floor(count / 60) # gives us number of minutes
    count_sec = count % 60 # remainder of seconds after we have cleanly divided by 60
    #Dynamic Typing - changing int(count_sec) to str(count_sec)
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}") #how to get timer text to count down? -assign timer text a variable
    if count > 0:
        window.after(1000, count_down, count - 1) #passing "hello" as input to function, or any *arg you use

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()#Creating the window
window.title("Study Bitch!")
# bg is == Background, which you can set to hexcodes above and pulled from teh color pallet website
window.config(padx = 100, pady= 50, bg= YELLOW)

#Canvas Widget
canvas = Canvas(width = 220, height= 224, bg=YELLOW, highlightthickness= 0) #highlightthickness kwarg gets rid of window background
#To create the canvas image, tkinter needs the name of image - Photo Image Class
tomato_img = PhotoImage(file = "tomato.png")
# Aiming to have image in the center of the canvas, so placing half the x and y below
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 25, "bold"))
canvas.grid(column = 1, row = 1)

#timer and checkmark label
timer_label = Label(text ="TIMER", fg=GREEN, bg= YELLOW, highlightthickness=0, font= (FONT_NAME, 30, "bold"))
timer_label.grid(column= 1, row = 0, sticky="s")

checkmark_label = Label(text ="✔", fg=GREEN, bg= YELLOW, highlightthickness=0, font= (FONT_NAME, 20, "bold"))
checkmark_label.grid(column = 1, row = 3, sticky ="n")

# Start and reset button
start_button = Button(text="Start", command= start_timer) #don't need parenthesis at the end because we are not calling the function
start_button.grid(column= 0, row=2, sticky= "e")

reset_button = Button(text="Reset")
reset_button.grid(column= 2, row = 2, sticky = "w")


window.mainloop()