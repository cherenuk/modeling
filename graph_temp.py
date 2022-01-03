import matplotlib.pyplot as plot
import numpy as np

BLUE = '#000099'


def make_graph(y1, y2, x2):
    x1 = 0
    # y1 = 20
    # x2 = 50
    # y2 = 100
    # x3 = 70
    # y3 = 100
    x = [x1, x2]
    y = [y1, y2]
    plot.plot(x, y, BLUE)
    show()


def show():
    plot.title('Зависимость температуры воды от времени')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k', lw=1)
    plot.axvline(x=0, color='k', lw=1)
    plot.xlabel('τ, мин')
    plot.ylabel('t, C°')
    plot.legend()
    plot.show()


if __name__ == '__main__':
    make_graph(20, 100, 50)