#! /usr/bin/env python3

import os
import matplotlib.pyplot as plt
import datetime
import openpyxl
from openpyxl.styles import NamedStyle, Font, Alignment
from openpyxl.drawing.image import Image



def plot_sparklines(title, data_list):
    coordinates_list = data_list[0]
    company_name = data_list[1]
    highest_count = data_list[2]
    active = data_list[3]

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
    if highest_count[1] > y[-1]:
        plt.plot(highest_count[0], highest_count[1],
                 color='k', marker='o', markersize=4)
        ax.annotate('{}'.format(highest_count[1]),
                    xy=(highest_count[0], highest_count[1]),
                    xytext=(-2, 2), textcoords='offset points',
                    ha='right', va='bottom')
    if active[1] > 0:
        plt.plot(active[0], active[1],
                 color='r', marker='o', markersize=4)
        ax.annotate('{}'.format(active[1]),
                    xy=(active[0], active[1]),
                    xytext=(3, -3), textcoords='offset points',
                    ha='left', va='top')

    fig.text(0.3, 0.15, '{}: {}'.format(cid, company_name))
    plt.grid()
    plt.savefig('charts/{}_{}.png'.format(cid,company_name.replace('.', '').replace('/', '')),
                format='png')
    # plt.show()


##################
# Function Calls #
##################

now = datetime.datetime.now()
filename = ('sparklines_{}.xlsx').format(
                 datetime.datetime.strftime(now, '%Y-%m-%dT%H-%M-%S'))

data = []

plot_sparklines(title, data)
