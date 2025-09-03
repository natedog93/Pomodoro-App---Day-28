from tkinter import *

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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()#Creating the window
window.title("Study Bitch!")
# bg is == Background, which you can set to hexcodes above and pulled from teh color pallet website
window.config(padx = 100, pady= 50, bg= YELLOW)

#Command for foreground color is going to be 'fg' =

#Canvas Widget
canvas = Canvas(width = 220, height= 224, bg=YELLOW, highlightthickness= 0) #highlightthickness kwarg gets rid of window background
#To create the canvas image, tkinter needs the name of image - Photo Image Class
tomato_img = PhotoImage(file = "tomato.png")
# Aiming to have image in the center of the canvas, so placing half the x and y below
canvas.create_image(100, 112, image = tomato_img)
canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 25, "bold"))
canvas.grid(column = 1, row = 1)

#timer and checkmark label
timer = Label(text = "TIMER",fg=GREEN, bg= YELLOW, highlightthickness=0, font= (FONT_NAME, 30, "bold"))
checkmark = Label(text = "✔",fg=GREEN, bg= YELLOW, highlightthickness=0, font= (FONT_NAME, 20, "bold"))
timer.grid(column= 1, row = 0, sticky= "s")
checkmark.grid(column = 1, row = 3, sticky = "n")

# Start and reset button
start_button = Button(text="Start") #don't need parenthesis at the end because we are not calling the function
reset_button = Button(text="Reset")
start_button.grid(column= 0, row=2, sticky= "e")
reset_button.grid(column= 2, row = 2, sticky = "w")



window.mainloop()