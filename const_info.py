import tkinter as tk
from PIL import ImageTk, Image


def main(root):
    window = tk.Toplevel(root)
    window.geometry('1060x420+400+100')
    window.resizable(width=False, height=False)
    window.title('Табличные значения')
    photo = ImageTk.PhotoImage(Image.open('images/const_logo.ico'))
    window.iconphoto(False, photo)

    info = ImageTk.PhotoImage(Image.open('images/const1.png'))
    background = tk.Label(window, image=info)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    window.mainloop()