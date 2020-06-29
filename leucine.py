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

def leucine(self):
    cn_min = [0, 0, 40]
    cn_max = [-45, 40, 10]

    nh_min = [-45, 40, 10]
    nh_max = [-50, 40, -50]

    cc1_min = [0, 0, 40]
    cc1_max = [45, -40, 10]

    co_min = [45, -40, 10]
    co_max = [60, -40, -50]

    ch1_min = [0, 0, 40]
    ch1_max = [-10, 10, 70]

    cc2_min = [0, 0, 40]
    cc2_max = [10, -10, 70]

    ch2_min = [10, -10, 70]
    ch2_max = [5, -5, 100]

    ch3_min = [10, -10, 70]
    ch3_max = [20, -20, 100]

    cc3_min = [10, -10, 70]
    cc3_max = [45, -45, 70]

    ch4_min = [45, -45, 70]
    ch4_max = [45, -45, 98]

    cc4_min = [45, -45, 70]
    cc4_max = [75, -75, 90]

    ch5_max = [100, -65, 120]
    ch5_min = [75, -75, 90]

    ch6_min = [75, -75, 90]
    ch6_max = [90, -90, 95]

    ch7_min = [75, -75, 90]
    ch7_max = [85, -85, 75]

    cc5_min = [45, -45, 70]
    cc5_max = [65, -65, 40]

    ch8_min = [65, -65, 40]
    ch8_max = [55, -55, 10]

    ch9_min = [65, -65, 40]
    ch9_max = [85, -85, 20]

    ch10_min = [65, -65, 40]
    ch10_max = [95, -90, 40]

    fig = Figure(figsize=(10,6), dpi=100,facecolor='black')
    canvas = FigureCanvasTkAgg(fig, self)
    canvas.draw()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_axis_bgcolor("black")		 
    
    cn = ax.plot([cn_max[0], cn_min[0]], [cn_max[1], cn_min[1]], [cn_max[2], cn_min[2]], linewidth=5,
                  color=cn_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    nh = ax.plot([nh_max[0], nh_min[0]], [nh_max[1],nh_min[1]], [nh_max[2], nh_min[2]], linewidth=5,
                  color=nh_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ccl = ax.plot([cc1_max[0], cc1_min[0]], [cc1_max[1], cc1_min[1]], [cc1_max[2], cc1_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    co = ax.plot([co_max[0], co_min[0]], [co_max[1], co_min[1]], [co_max[2], co_min[2]], linewidth=5,
                  color=co_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ch1 = ax.plot([ch1_max[0], ch1_min[0]], [ch1_max[1], ch1_min[1]], [ch1_max[2], ch1_min[2]], linewidth=5,
                  color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    cc2 = ax.plot([cc2_max[0], cc2_min[0]], [cc2_max[1], cc2_min[1]], [cc2_max[2], cc2_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ch2 = ax.plot([ch2_max[0], ch2_min[0]], [ch2_max[1], ch2_min[1]], [ch2_max[2], ch2_min[2]], linewidth=5,
                  color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ch3 = ax.plot([ch3_max[0], ch3_min[0]], [ch3_max[1], ch3_min[1]], [ch3_max[2], ch3_min[2]], linewidth=5,
                  color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    cc3 = ax.plot([cc3_max[0], cc3_min[0]], [cc3_max[1], cc3_min[1]], [cc3_max[2], cc3_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ch4 = ax.plot([ch4_max[0], ch4_min[0]], [ch4_max[1], ch4_min[1]], [ch4_max[2], ch4_min[2]], linewidth=5,
                  color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    cc4 = ax.plot([cc4_max[0], cc4_min[0]], [cc4_max[1], cc4_min[1]], [cc4_max[2], cc4_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ch5 = ax.plot([ch5_max[0], ch5_min[0]], [ch5_max[1], ch5_min[1]], [ch5_max[2], ch5_min[2]], linewidth=5,
                  color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ch6 = ax.plot([ch6_max[0], ch6_min[0]], [ch6_max[1], ch6_min[1]], [ch6_max[2], ch6_min[2]], linewidth=5,
                  color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ch7 = ax.plot([ch7_max[0], ch7_min[0]], [ch7_max[1], ch7_min[1]], [ch7_max[2], ch7_min[2]], linewidth=5,
                  color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    cc5 = ax.plot([cc5_max[0], cc5_min[0]], [cc5_max[1], cc5_min[1]], [cc5_max[2], cc5_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ch8 = ax.plot([ch8_max[0], ch8_min[0]], [ch8_max[1], ch8_min[1]], [ch8_max[2], ch8_min[2]], linewidth=5,
                  color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ch9 = ax.plot([ch9_max[0], ch9_min[0]], [ch9_max[1], ch9_min[1]], [ch9_max[2], ch9_min[2]], linewidth=5,
                  color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ch10 = ax.plot([ch10_max[0], ch10_min[0]], [ch10_max[1], ch10_min[1]], [ch10_max[2], ch10_min[2]], linewidth=5,
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

