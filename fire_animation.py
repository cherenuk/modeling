import tkinter as tk

W = 500
H = 280


def main(root):
    window = tk.Toplevel(root)
    window.geometry(f'{W}x{H}+100+100')
    window.resizable(width=False, height=False)

    frameCnt = 12
    frames = [tk.PhotoImage(file='images/bg.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

    bg = tk.Label(window)
    bg.place(x=0, y=0, relwidth=1, relheight=1)

    def update(ind, bg):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        bg.configure(image=frame)
        window.after(100, update, ind, bg)

    window.after(0, update, 0, bg)
    window.mainloop()

if __name__ == '__main__':
    main()
