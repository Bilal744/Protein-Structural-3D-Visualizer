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
def alanine(self):
    ch_min = [0, 0, 40]
    ch_max = [-10, 10, 70]

    ch1_min = [0, 0, 40]
    ch1_max = [10, -10, 70]

    ch2_min = [10, -10, 70]
    ch2_max = [25, -25, 80]

    ch3_min = [10, -10, 70]
    ch3_max = [5, -30, 50]

    ch4_min = [10, -10, 70]
    ch4_max = [15, -25, 60]

    cn_min = [0, 0, 40]
    cn_max = [-45, 40, 10]

    cc1_min = [0, 0, 40]
    cc1_max = [45, -40, 10]

    co_min = [45, -40, 10]
    co_max = [60, -40, -50]

    nh_min = [-45, 40, 10]
    nh_max = [-50, 40, -50]
    
    fig = Figure(figsize=(10,6), dpi=100,facecolor='black')
    canvas = FigureCanvasTkAgg(fig, self)
    canvas.draw()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_axis_bgcolor("black")

    ch = ax.plot([ch_max[0], ch_min[0]], [ch_max[1], ch_min[1]], [ch_max[2], ch_min[2]], linewidth=5,color=ch_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    cc1 = ax.plot([ch1_max[0], ch1_min[0]], [ch1_max[1], ch1_min[1]], [ch1_max[2], ch1_min[2]], linewidth=5,color=cc_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    ch2 = ax.plot([ch2_max[0], ch2_min[0]], [ch2_max[1], ch2_min[1]], [ch2_max[2], ch2_min[2]], linewidth=5,color=ch_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    ch3 = ax.plot([ch3_max[0], ch3_min[0]], [ch3_max[1], ch3_min[1]], [ch3_max[2], ch3_min[2]], linewidth=5,color=ch_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    ch4 = ax.plot([ch4_max[0], ch4_min[0]], [ch4_max[1], ch4_min[1]], [ch4_max[2], ch4_min[2]], linewidth=5,color=ch_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    cn = ax.plot([cn_max[0], cn_min[0]], [cn_max[1], cn_min[1]], [cn_max[2], cn_min[2]], linewidth=5, color=cn_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    cc = ax.plot([cc1_max[0], cc1_min[0]], [cc1_max[1], cc1_min[1]], [cc1_max[2], cc1_min[2]], linewidth=5, color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    co = ax.plot([co_max[0], co_min[0]], [co_max[1], co_min[1]], [co_max[2], co_min[2]], linewidth=5, color=co_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    nh = ax.plot([nh_max[0], nh_min[0]], [nh_max[1], nh_min[1]], [nh_max[2], nh_min[2]], linewidth=5,
                 color=nh_color, marker='o', markerfacecolor='orange', markersize=12)

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

