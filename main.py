from tkinter import *
import asyncio
import Chess

def start_game():
        fr.destroy()
        Chess.start_game(root)

root = Tk()
root.title('Chess')
root.geometry('700x500')

fr = Frame(root)
fr.pack(pady=50)
Button(fr, text = "Start",
        width=50,
        command= start_game).pack()
Button(fr, text = "Exit",
        width=50,
        command=root.quit).pack()
root.mainloop()