import tkinter as tk
from PIL import ImageTk, Image


def main(root):
    window = tk.Toplevel(root)
    window.geometry('530x510+400+100')
    window.resizable(width=False, height=False)
    window.title('О программе')
    photo = ImageTk.PhotoImage(Image.open('images/program_logo.ico'))
    window.iconphoto(False, photo)

    info = ImageTk.PhotoImage(Image.open('images/program1.png'))
    background = tk.Label(window, image=info)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    window.mainloop()
