import Tkinter
import Tkinter as tk
from Tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
import tkMessageBox as msg
import matplotlib.pyplot as plt
import pickle
import Image
import os

from colors import *
def arginine(self):
    ch_min = [0, 0, 40]
    ch_max = [-20, 30, 70]

    cc_min = [0, 0, 40]
    cc_max = [40, -20, 70]

    co_min = [45, -40, 10]
    co_max = [60, -40, -50]

    nh_min = [-45, 40, 10]
    nh_max = [-50, 40, -50]

    cn_min = [0, 0, 40]
    cn_max = [-45, 40, 10]

    cc1_min = [0, 0, 40]
    cc1_max = [45, -40, 10]

    c3_min = [40, -20, 70]
    c3_max = [80, -45, 60]

    c3h1_min = [80, -45, 60]
    c3h1_max = [70, -20, 40]

    c3h2_min = [80, -45, 60]
    c3h2_max = [100, -60, 40]

    c3c4_min = [80, -45, 60]
    c3c4_max = [125, -70, 100]

    c4h1_min = [125, -70, 100]
    c4h1_max = [145, -45, 80]

    c4h2_min = [125, -70, 100]
    c4h2_max = [155, -20, 120]

    c4n1_min = [125, -70, 100]
    c4n1_max = [175, -85, 80]

    c5n1_min = [175, -85, 80]
    c5n1_max = [280, -120, 130]

    c5n2_min = [280, -120, 130]
    c5n2_max = [310, -150, 100]

    c5n2h1_min = [310, -150, 100]
    c5n2h1_max = [350, -190, 130]

    c5n2h2_min = [310, -150, 100]
    c5n2h2_max = [270, -200, 70]

    c5n3_min = [280, -120, 130]
    c5n3_max = [250, -180, 160]

    c5n3h1_min = [250, -180, 160]
    c5n3h1_max = [300, -240, 200]

    c5n3h2_min = [250, -180, 160]
    c5n3h2_max = [200, -230, 130]

    c4n1h1_min = [175, -85, 80]
    c4n1h1_max = [185, -110, 40]

    c2h1_min = [40, -20, 70]
    c2h1_max = [50, -50, 100]

    c2h2_min = [40, -20, 70]
    c2h2_max = [25, 10, 100]

    fig = Figure(figsize=(10,6), dpi=100,facecolor='black')
    canvas = FigureCanvasTkAgg(fig, self)
    canvas.draw()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_axis_bgcolor("black")	

    ch = ax.plot([ch_max[0], ch_min[0]], [ch_max[1], ch_min[1]], [ch_max[2], ch_min[2]], linewidth=5,
                 color=ch_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    cc = ax.plot([cc_max[0], cc_min[0]], [cc_max[1], cc_min[1]], [cc_max[2], cc_min[2]], linewidth=5,
                 color=cc_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    co = ax.plot([co_max[0], co_min[0]], [co_max[1], co_min[1]], [co_max[2], co_min[2]], linewidth=5,
                 color=co_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    nh = ax.plot([nh_max[0], nh_min[0]], [nh_max[1], nh_min[1]], [nh_max[2], nh_min[2]], linewidth=5,
                 color=nh_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    cn = ax.plot([cn_max[0], cn_min[0]], [cn_max[1], cn_min[1]], [cn_max[2], cn_min[2]], linewidth=5,
                 color=cn_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    ccl = ax.plot([cc1_max[0], cc1_min[0]], [cc1_max[1], cc1_min[1]], [cc1_max[2], cc1_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    c3 = ax.plot([c3_max[0], c3_min[0]], [c3_max[1], c3_min[1]], [c3_max[2], c3_min[2]], linewidth=5,
                 color=cc_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    c3h1 = ax.plot([c3h1_max[0], c3h1_min[0]], [c3h1_max[1], c3h1_min[1]], [c3h1_max[2], c3h1_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    c3h2 = ax.plot([c3h2_max[0], c3h2_min[0]], [c3h2_max[1], c3h2_min[1]], [c3h2_max[2], c3h2_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    c3c4 = ax.plot([c3c4_max[0], c3c4_min[0]], [c3c4_max[1], c3c4_min[1]], [c3c4_max[2], c3c4_min[2]], linewidth=5,
                   color=cc_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    c4h1 = ax.plot([c4h1_max[0], c4h1_min[0]], [c4h1_max[1], c4h1_min[1]], [c4h1_max[2], c4h1_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    c4h2 = ax.plot([c4h2_max[0], c4h2_min[0]], [c4h2_max[1], c4h2_min[1]], [c4h2_max[2], c4h2_min[2]],
                   linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    c4n1 = ax.plot([c4n1_max[0], c4n1_min[0]], [c4n1_max[1], c4n1_min[1]], [c4n1_max[2], c4n1_min[2]],
                  linewidth=5,
                  color=cn_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    c5n1 = ax.plot([c5n1_max[0], c5n1_min[0]], [c5n1_max[1], c5n1_min[1]], [c5n1_max[2], c5n1_min[2]], linewidth=5,
                   color=cn_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    c5n2 = ax.plot([c5n2_max[0], c5n2_min[0]], [c5n2_max[1], c5n2_min[1]], [c5n2_max[2], c5n2_min[2]], linewidth=5,
                   color=cn_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    c5n2h1 = ax.plot([c5n2h1_max[0], c5n2h1_min[0]], [c5n2h1_max[1], c5n2h1_min[1]], [c5n2h1_max[2], c5n2h1_min[2]],
                     linewidth=5,
                     color=nh_color,
                     marker='o', markerfacecolor='orange', markersize=12)
    c5n2h2 = ax.plot([c5n2h2_max[0], c5n2h2_min[0]], [c5n2h2_max[1], c5n2h2_min[1]], [c5n2h2_max[2], c5n2h2_min[2]],
                     linewidth=5,
                     color=nh_color,
                     marker='o', markerfacecolor='orange', markersize=12)
    c5n3 = ax.plot([c5n3_max[0], c5n3_min[0]], [c5n3_max[1], c5n3_min[1]], [c5n3_max[2], c5n3_min[2]],
                     linewidth=5,
                     color=cn_color,
                     marker='o', markerfacecolor='orange', markersize=12)
    c5n3h1 = ax.plot([c5n3h1_max[0], c5n3h1_min[0]], [c5n3h1_max[1], c5n3h1_min[1]], [c5n3h1_max[2], c5n3h1_min[2]], linewidth=5,
                   color=nh_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    c5n3h2 = ax.plot([c5n3h2_max[0], c5n3h2_min[0]], [c5n3h2_max[1], c5n3h2_min[1]], [c5n3h2_max[2], c5n3h2_min[2]],
                     linewidth=5,
                     color=nh_color,
                     marker='o', markerfacecolor='orange', markersize=12)
    c4n1h1 = ax.plot([c4n1h1_max[0], c4n1h1_min[0]], [c4n1h1_max[1], c4n1h1_min[1]], [c4n1h1_max[2], c4n1h1_min[2]], linewidth=5,
                   color=nh_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    c2h1 = ax.plot([c2h1_max[0], c2h1_min[0]], [c2h1_max[1], c2h1_min[1]], [c2h1_max[2], c2h1_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    c2h2 = ax.plot([c2h2_max[0], c2h2_min[0]], [c2h2_max[1], c2h2_min[1]], [c2h2_max[2], c2h2_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)

    tch = plt.Rectangle((0, 0), 1, 1, fc=ch_color)
    tch1 = plt.Rectangle((0, 0), 1, 1, fc=ch_color)
    tcn = plt.Rectangle((0, 0), 1, 1, fc=cn_color)
    tcc = plt.Rectangle((0, 0), 1, 1, fc=cc_color)
    tbco = plt.Rectangle((0, 0), 1, 1, fc=co_color)
    tbnh = plt.Rectangle((0, 0), 1, 1, fc=nh_color)


    ax.legend([tch,tcn,tcc,tbco,tbnh],['ch','cn','cc','co','nh'])
    ax.axis("off")  
    toolbarFrame = Frame(self)
    toolbarFrame.grid(row=6,column=7)
    toolbar = NavigationToolbar2TkAgg(canvas, toolbarFrame)
    canvas.get_tk_widget().grid(row=4,column=7) 
