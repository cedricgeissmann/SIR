# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from random import uniform

import numpy as np


def sir_modell(x, **kwargs):
    """Iterationsfunktion für das SIR-Modell."""
    x_elem = list(x)
    assert len(x_elem) == 4
    a = kwargs.get("a")
    b = kwargs.get("b")
    c = kwargs.get("c")
    d = kwargs.get('d', 0)
    daily_fluctuations = kwargs.get('daily_fluctuations', 0.1)

    a = a * uniform(1-daily_fluctuations, 1+daily_fluctuations)
    b = b * uniform(1-daily_fluctuations, 1+daily_fluctuations)
    c = c * uniform(1-daily_fluctuations, 1+daily_fluctuations)
    d = d * uniform(1-daily_fluctuations, 1+daily_fluctuations)

    S = x[0]
    I = x[1]
    R = x[2]
    V = x[3]

    S_new = S - a * S * I + b * I - d * S
    I_new = I + a * S * I - b * I - c * I
    R_new = R + c * I
    V_new = V + d * S

    return [S_new, I_new, R_new, V_new]


def iteration(f, x0, n=10, cond=lambda x: False, **kwargs):
    """
    Führt eine Iteration der Funktion f durch.

    f: ist die Funktion die als Iterationsmodell verwendet wird.
    x0: ist der Startwert der Iteration.
    cond: ist eine callback-Funktion welche die Iteration abbricht wenn sie
    erfüllt ist.
    n: ist die Anzahl Zeitschritte der Iteration (default=10).
    kwargs: Weitere argumente die der Iterationsfunktion übergeben werden.
    """
    x_list = [x0]
    for i in range(n):
        if cond(x_list):
            print("Bedingung erfüllt für Element x" + str(i))
            return
        x_elem = f(x_list[-1], **kwargs)
        x_list.append(x_elem)
    return x_list


def plot_iteration(iter_list):
    """
    Plottet die Iterationen des Räuber-Beute-Modells.

    iter_list: ist die Rückgabe der Funktion iteration.
    """
    plt.plot(iter_list)
    plt.show()


def simple_remap(bad_list):
    """
    Nimmt eine Liste mit Einträgen in der Form [[list1], [list2], ...]
    entgegen, und macht daraus eine Liste der Form [[elem1_list1, elem2_list2,
    ...], [elem1_list2, elem2_list2, ...]].
    """
    return np.reshape(bad_list, (len(bad_list), len(bad_list[0]))).T.tolist()


def mean(iter_list, index):
    """
    Berechnet das arithmetische Mittel von iter_list[0][index],
    iter_list[1][index], ...
    """
    return np.mean(simple_remap(iter_list)[index])
