from tkinter import *
import asyncio
import Chess

def start_game():
    fr.destroy()
    Chess.start_game(root)

root = Tk()
root.title('Chess')
root.geometry('700x500')

fr = LabelFrame(text="aboba")
fr.pack(pady=50, fill=Y)
Button(fr, text = "Start",
        width=50,
        command= start_game).pack()
Button(fr, text = "Exit",
        width=50).pack()
root.mainloop()