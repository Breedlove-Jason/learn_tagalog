from tkinter import *

window = Tk()
window.title("Tagalog Flash Cards")
window.geometry("800x600")
window.config(bg="white", padx=50, pady=50)
canvas = Canvas(width=800, height=526, bg="white", highlightthickness=0)
canvas.grid(row=0, column=1)


window.mainloop()
