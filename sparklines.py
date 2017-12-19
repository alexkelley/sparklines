#! /usr/bin/env python3

import os
import matplotlib.pyplot as plt
import datetime
import openpyxl
from openpyxl.styles import NamedStyle, Font, Alignment
from openpyxl.drawing.image import Image


def plot_sparklines(title, coordinates_list, highest, lowest, current):

    font = {'family': 'serif',
            'weight': 'normal',
            'size': 8}
    plt.rc('font', **font)

    x = []
    y = []
    for point in coordinates_list:
        x.append(point[0])
        y.append(point[1])

    fig, ax = plt.subplots(1, 1, figsize=(4, 1))
    plt.plot(x, y, color='#545454')
    plt.plot(x[0], y[0], color='g', marker='o', markersize=4)
    plt.plot(x[-1], y[-1], color='b', marker='o', markersize=4)
    plt.margins(0.05, 0.1)
    for k, v in ax.spines.items():
        v.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.annotate('{}'.format(y[0]), xy=(x[0], y[0]),
                xytext=(-2, 2), textcoords='offset points',
                ha='right', va='bottom')
    ax.annotate('{}'.format(y[-1]), xy=(x[-1], y[-1]),
                xytext=(3, -3), textcoords='offset points',
                ha='left', va='bottom')
    # if highest[1] > y[-1]:
    #     plt.plot(highest[0], highest[1],
    #              color='k', marker='o', markersize=4)
    #     ax.annotate('{}'.format(highest[1]),
    #                 xy=(highest[0], highest[1]),
    #                 xytext=(-2, 2), textcoords='offset points',
    #                 ha='right', va='bottom')
    # if current[1] > 0:
    #     plt.plot(current[0], current[1],
    #              color='r', marker='o', markersize=4)
    #     ax.annotate('{}'.format(current[1]),
    #                 xy=(current[0], current[1]),
    #                 xytext=(3, -3), textcoords='offset points',
    #                 ha='left', va='top')

    fig.text(0.3, 0.15, '{}'.format(title))
    plt.grid()
    #plt.savefig('charts/{}.png'.format(title), format='png')
    plt.show()


##################
# Function Calls #
##################

now = datetime.datetime.now()
filename = ('sparklines_{}.xlsx').format(
                 datetime.datetime.strftime(now, '%Y-%m-%dT%H-%M-%S'))

title = 'Fun with Sparklines'
coordinates_list = [
    (datetime.datetime(2016, 12, 1, 0, 0), 7),
    (datetime.datetime(2017, 1, 1, 0, 0), 6),
    (datetime.datetime(2017, 2, 1, 0, 0), 5),
    (datetime.datetime(2017, 3, 1, 0, 0), 6),
    (datetime.datetime(2017, 4, 1, 0, 0), 4),
    (datetime.datetime(2017, 5, 1, 0, 0), 2),
    (datetime.datetime(2017, 6, 1, 0, 0), 3),
    (datetime.datetime(2017, 7, 1, 0, 0), 1),
    (datetime.datetime(2017, 8, 1, 0, 0), 5),
    (datetime.datetime(2017, 9, 1, 0, 0), 8),
    (datetime.datetime(2017, 10, 1, 0, 0), 9),
    (datetime.datetime(2017, 11, 1, 0, 0), 3)
]
highest = 9
lowest =  1
current = 3

plot_sparklines(title, coordinates_list, highest, lowest, current)
