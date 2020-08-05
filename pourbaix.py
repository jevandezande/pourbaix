#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


SLOPE = -0.059
ROTATION = -8


def water(plot=None, phases=True, reactions=True, x1=0, x2=14):
    fig, ax = plt.subplots() if plot is None else plot

    drop = np.array([SLOPE*x1, SLOPE*x2])
    ax.plot([x1, x2], drop + 1.229, 'C0--')
    ax.plot([x1, x2], drop, 'C1--')

    if phases:
        ax.text(10,  1.00, 'Oxygen')
        ax.text( 6,  0.20, 'Water')
        ax.text( 2, -0.55, 'Hydrogen')

    if reactions:
        # Oxygen evolution
        ax.text(0.1, 1, 'O$_2$ + 4H$^+$ + 4e$^-$ $\\rightleftharpoons$ 2H$_2$O', rotation=ROTATION)
        ax.text(8.7, 1 + SLOPE*8.6, 'O$_2$ + 2H$_2$O + 4e$^-$ $\\rightleftharpoons$ 4OH$^-$', rotation=ROTATION)

        # Hydrogen evolution
        ax.text(0.1, -0.15, '2H$^+$ + 2e$^-$ $\\rightleftharpoons$ H$_2$', rotation=ROTATION)
        ax.text(8.7, -0.25 + SLOPE*8.6, '2H$_2$O + 2e$^-$ $\\rightleftharpoons$ H$_2$ + 2OH$^-$', rotation=ROTATION)

    return fig, ax


def Al(plot=None, phases=True, reactions=True, x1=0, x2=14):
    fig, ax = plt.subplots() if plot is None else plot

    ax.plot([4, 4], [-1.6, 100], 'C3')
    ax.plot([8.5, 8.5], [-1.6 + SLOPE*4.5, 100], 'C5')
    ax.plot([x1, 4], [-1.6, -1.6], 'C2')
    ax.plot([4, x2], [-1.6, -1.6 + SLOPE*(x2 - 4)], 'C4')

    if phases:
        ax.text(1.5, 0.4, 'Al$^{3+}$')
        ax.text(5.3, 0.4 + SLOPE*3.8, 'Al$_2$O$_3$·H$_2$O')
        ax.text(10.5,  0.4 + SLOPE*9, 'AlO$_2^-$')
        ax.text(3.5, -2.1, 'Al')

    if reactions:
        pass

    return fig, ax


def Ir(plot=None, phases=True, reactions=True, x1=0, x2=14):
    fig, ax = plt.subplots() if plot is None else plot

    drop = np.array([SLOPE*x1, SLOPE*x2])
    ax.plot([x1, x2], drop + 0.95, 'C6')

    if phases:
        ax.text(7.6,  0.55, 'IrO$_2$')
        ax.text(5.7,  0.15, 'Ir')

    if reactions:
        pass

    return fig, ax


def Ru(plot=None, phases=True, reactions=True, x1=0, x2=14):
    fig, ax = plt.subplots() if plot is None else plot

    drop = np.array([SLOPE*x1, SLOPE*x2])
    ax.plot([x1, x2], drop + 0.78, 'C2')
    ax.plot([x1, x2], drop + 0.95, 'C3')
    ax.plot([x1, 11.2], [1.00, 1.00], 'C4')
    ax.plot([11.2, 11.2], [1.0, 1.5], 'C5')
    ax.plot([11.2, 14], [1.0, 1.0 + SLOPE*(x2 - 11.2)], 'C4')

    if phases:
        ax.text(5.7,  0.05, 'Ru')
        ax.text(6.0,  0.66, 'RuO$_2\cdot2$H$_2$O', rotation=ROTATION)
        ax.text(5.9,  0.47, 'Ru(OH$_3$)', rotation=ROTATION)
        ax.text(5.7,  1.25, 'RuO$_4$')
        ax.text(10.0, 0.85, 'RuO${_4}^{-}$', rotation=-7)
        ax.text(12.5, 0.60, 'RuO${_4}^{-2}$', rotation=ROTATION)
        ax.text(12.0, 1.25, 'HRuO${_5}^{-}$')

    if reactions:
        pass

    return fig, ax


def pic(plot=None, name='', x1=0, x2=14, y1=-1, y2=1.5):
    fig, ax = plt.subplots() if plot is None else plot

    ax.set_xlim([x1, x2])
    ax.set_ylim([y1, y2])

    make_ticks = lambda start, end, tw: np.arange(int(start/tw)*tw, int(end/tw + 1)*tw, tw)

    #ax.set_yticks(make_ticks(y1, y2, 0.5))

    if name:
        ax.set_title(name)
    ax.set_ylabel('Potential E(V) vs SHE')
    ax.set_xlabel('pH')


def water_pic(plot=None):
    plot = plt.subplots() if plot is None else plot

    pic(plot, 'Water Pourbaix Diagram')
    water(plot)
    plot[0].savefig('water.pdf')
    plot[0].show()


def Al_pic(plot=None):
    plot = plt.subplots() if plot is None else plot

    pic(plot, 'Al Pourbaix Diagram', y1=-2.5, y2=1.5)
    water(plot, phases=False)
    Al(plot)
    plot[0].savefig('Al_water.pdf')
    plot[0].show()


def Ir_pic(plot=None):
    plot = plt.subplots() if plot is None else plot

    pic(plot, 'Ir Pourbaix Diagram')
    water(plot, phases=False)
    Ir(plot)
    plot[0].savefig('Ir_water.pdf')
    plot[0].show()


def Ru_pic(plot=None):
    plot = plt.subplots() if plot is None else plot

    pic(plot, 'Ru Pourbaix Diagram')
    water(plot, phases=False, reactions=False)
    Ru(plot)
    plot[0].savefig('Ru_water.pdf')
    plot[0].show()


water_pic()
Al_pic()
Ir_pic()
Ru_pic()
