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

def serine(self):
    cn_min = [0, 0, 40]
    cn_max = [-45, 40, 10]

    bnh_min = [-45, 40, 10]
    bnh_max = [-50, 40, -50]

    cc1_min = [0, 0, 40]
    cc1_max = [45, -40, 10]

    bco_min = [45, -40, 10]
    bco_max = [60, -40, -50]

    ch1_min = [0, 0, 40]
    ch1_max = [-10, 10, 70]

    cc2_min = [0, 0, 40]
    cc2_max = [10, -10, 70]

    ch2_min = [10, -10, 70]
    ch2_max = [5, -5, 90]

    ch3_min = [10, -10, 70]
    ch3_max = [20, -20, 90]

    co2_min = [10, -10, 70]
    co2_max = [40, -40, 70]
    oh_min = [40, -40, 70]
    oh_max = [60, -50, 50]

    fig = Figure(figsize=(10,6), dpi=100,facecolor='black')
    canvas = FigureCanvasTkAgg(fig, self)
    canvas.draw()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_axis_bgcolor("black")	

    cn = ax.plot([cn_max[0], cn_min[0]], [cn_max[1], cn_min[1]], [cn_max[2], cn_min[2]], linewidth=5, color=cn_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    bnh = ax.plot([bnh_max[0], bnh_min[0]], [bnh_max[1], bnh_min[1]], [bnh_max[2], bnh_min[2]], linewidth=5,
                  color=nh_color, marker='o', markerfacecolor='orange', markersize=12)
    ccl = ax.plot([cc1_max[0], cc1_min[0]], [cc1_max[1], cc1_min[1]], [cc1_max[2], cc1_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    bco = ax.plot([bco_max[0], bco_min[0]], [bco_max[1], bco_min[1]], [bco_max[2], bco_min[2]], linewidth=5,
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
    co2 = ax.plot([co2_max[0], co2_min[0]], [co2_max[1], co2_min[1]], [co2_max[2], co2_min[2]], linewidth=5,
                  color=co_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    oh = ax.plot([oh_max[0], oh_min[0]], [oh_max[1], oh_min[1]], [oh_max[2], oh_min[2]], linewidth=5,
                  color=oh_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    tch = plt.Rectangle((0, 0), 1, 1, fc=ch_color)
    toh = plt.Rectangle((0, 0), 1, 1, fc=oh_color)
    tcn = plt.Rectangle((0, 0), 1, 1, fc=cn_color)
    tcc = plt.Rectangle((0, 0), 1, 1, fc=cc_color)
    tbco = plt.Rectangle((0, 0), 1, 1, fc=co_color)
    tbnh = plt.Rectangle((0, 0), 1, 1, fc=nh_color)


    ax.legend([tch,tcn,tcc,tbco,tbnh,toh],['ch','cn','cc','co','nh','oh'])

    ax.axis("off")  
    toolbarFrame = Frame(self)
    toolbarFrame.grid(row=6,column=7)
    toolbar = NavigationToolbar2TkAgg(canvas, toolbarFrame)
    canvas.get_tk_widget().grid(row=4,column=7) 

