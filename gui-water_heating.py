import tkinter as tk
from tkinter import ttk
import water_heating
import graph_temp
from PIL import ImageTk, Image


BLUE = '#87CEEB'
DARK_BLUE = '#58C0EC'

W = 700
H = 517
W_FIGURE = 460

FONT = 'Arial 12'
FONT_ENTRY = 'Arial 14'
FONT_COMMANDS = 'Arial 12 italic'
FONT_RESULT = 'Arial 14 italic'

title = 'Калькулятор расчета времени кипения воды \n на газовой горелке'
ready_text = 'ᐅ  Нажмите готово для получения результата'
graph_text = 'ᐅ  График, чтобы увидеть зависимость температуры \n от времени'
extra_text = 'ᐅ  В верхнем меню есть дополнительная информация'
test_text = '---------------------------------------------------------------------------'


def enter_color(event, but):
    but['bg'] = DARK_BLUE


def leave_color(event, but):
    but['bg'] = BLUE


def result(boiler_index, boiler_mass, start_temp, burner_power, water_volume):
    time = water_heating.main(boiler_index, boiler_mass, start_temp, burner_power, water_volume)
    return time


def show_result(canvas, item1, item2, item3, time):
    canvas.delete(item1, item2, item3, 'past_result')
    canvas.create_text(220, 110, text=f'Время кипения воды: \n \n ➤{"%.2f" % time} мин',
                       justify=tk.CENTER, font=FONT_RESULT, tag='past_result')


def show_graph(start_temp, time):
    graph_temp.make_graph(start_temp, 100, time)


def main():
    window = tk.Tk()
    photo = tk.PhotoImage(file='images/kettle.ico')
    bowler_img = ImageTk.PhotoImage(Image.open('images/bowler1_main.jpg'))
    window.geometry(f'{W}x{H}+400+100')
    window.resizable(width=False, height=False)
    window.title('Кипение воды')
    window.iconphoto(False, photo)

    mainmenu = tk.Menu(window)
    window.config(menu=mainmenu)
    author = mainmenu.add_command(label='Об авторе')
    program = mainmenu.add_command(label='О программе')
    reference = tk.Menu(mainmenu, tearoff=0)
    mainmenu.add_cascade(label='Справочные данные', menu=reference)
    reference.add_command(label='Табличные значения')
    reference.add_command(label='Формулы')
    reference.add_command(label='Газовая горелка?')

    figure = tk.Canvas(window, bg='white', bd=3, highlightthickness=1, relief='ridge')
    figure.place(x=0, y=0, relx=0, rely=0, width=W_FIGURE, height=H-20)
    title_look = figure.create_text(220, 30, text=title, justify=tk.CENTER, font=FONT_ENTRY)
    test_look = figure.create_text(230, 55, text=test_text, justify=tk.CENTER, font=FONT_ENTRY)
    ready_look = figure.create_text(200, 80, text=ready_text, font=FONT_COMMANDS)
    graph_look = figure.create_text(230, 140, text=graph_text, justify=tk.CENTER, font=FONT_COMMANDS)
    extra_look = figure.create_text(225, 200, text=extra_text, justify=tk.CENTER, font=FONT_COMMANDS)
    figure.create_image(W_FIGURE//2, H-150, image=bowler_img)

    material = tk.Label(font=FONT, text='Материал котелка/чайника:')
    material.grid(row=0, column=0, pady=10, padx=20, sticky=tk.E)

    material_list = ttk.Combobox(width=20, font=FONT,
                                 values=water_heating.materials)
    material_list.grid(row=1, column=0, padx=15, sticky=tk.E)

    mass_text = tk.Label(font=FONT, text='Масса котелка/чайника(кг):')
    mass_text.grid(row=2, column=0, pady=10, padx=21, sticky=tk.E)
    mass = tk.Entry(font=FONT_ENTRY, width=5)
    mass.grid(row=3, column=0, padx=80, sticky=tk.E)

    temp_text = tk.Label(font=FONT, text='Начальная температура(C°):')
    temp_text.grid(row=4, column=0, pady=10, padx=5, sticky=tk.E)
    temp = tk.Scale(font=FONT_ENTRY, orient='horizontal', from_=1, to=99)
    temp.grid(row=5, column=0, padx=55, sticky=tk.E)

    power_text = tk.Label(font=FONT, text='Мощность горелки(кВт):')
    power_text.grid(row=6, column=0, pady=10, padx=40, sticky=tk.E)
    power = tk.Entry(font=FONT_ENTRY, width=5)
    power.grid(row=7, column=0, padx=80, sticky=tk.E)

    volume_text = tk.Label(font=FONT, text='Объем воды(л):')
    volume_text.grid(row=8, column=0, pady=10, padx=95, sticky=tk.E)
    volume = tk.Entry(font=FONT_ENTRY, width=5)
    volume.grid(row=9, column=0, padx=80, sticky=tk.E)

    ready = tk.Button(text='Готово', bg=BLUE, width=30, height=2,
                      relief='raised', borderwidth=3)
    ready.bind('<Enter>', lambda e: enter_color(e, ready))
    ready.bind('<Leave>', lambda e: leave_color(e, ready))
    ready['command'] = lambda: show_result(figure, ready_look, graph_look, extra_look,
                                           result(material_list.get(), float(mass.get()),
                                                   float(temp.get()), float(power.get()),
                                                   float(volume.get())))

    ready.grid(row=10, column=0, padx=10, sticky=tk.SE)

    graph_but = tk.Button(text='График', bg=BLUE, width=30, height=2,
                          relief='raised', borderwidth=3)
    graph_but.bind('<Enter>', lambda e: enter_color(e, graph_but))
    graph_but.bind('<Leave>', lambda e: leave_color(e, graph_but))
    graph_but['command'] = lambda: show_graph(int(temp.get()), result(material_list.get(), float(mass.get()),
                                                                      float(temp.get()), float(power.get()),
                                                                      float(volume.get())))
    graph_but.grid(row=11, column=0, padx=10, pady=10, sticky=tk.SE)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(10, weight=1)

    window.mainloop()


if __name__ == '__main__':
    main()
