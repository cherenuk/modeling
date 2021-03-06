import matplotlib.pyplot as plot


BLUE = '#000099'


def make_graph(y1, y2, x2):
    x1 = 0
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
