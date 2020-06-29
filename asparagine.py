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

def asparagine(self):
    cn_min = [0, 0, 40]
    cn_max = [-45, 40, 10]

    cc1_min = [0, 0, 40]
    cc1_max = [45, -40, 10]

    co_min = [45, -40, 10]
    co_max = [60, -40, -50]

    nh_min = [-45, 40, 10]
    nh_max = [-50, 40, -50]

    ch_min = [0, 0, 40]
    ch_max = [-10, 10, 70]

    ch1_min = [0, 0, 40]
    ch1_max = [10, -10, 70]

    ccc_min = [10, -10, 70]
    ccc_max = [25, -25, 80]

    cccn_min = [25, -25, 80]
    cccn_max = [35, -35, 100]

    cccnh1_min = [35, -35, 100]
    cccnh1_max = [50, -50, 70]

    cccnh2_min = [35, -35, 100]
    cccnh2_max = [50, -35, 130]

    ccco_min = [25, -25, 80]
    ccco_max = [10, 10, 100]

    cch2_min = [10, -10, 70]
    cch2_max = [5, -30, 50]

    cch3_min = [10, -10, 70]
    cch3_max = [15, -25, 60]

    fig = Figure(figsize=(10,6), dpi=100,facecolor='black')
    canvas = FigureCanvasTkAgg(fig, self)
    canvas.draw()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_axis_bgcolor("black")	

    cn = ax.plot([cn_max[0], cn_min[0]], [cn_max[1], cn_min[1]], [cn_max[2], cn_min[2]], linewidth=5,
                 color=cn_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    ccl = ax.plot([cc1_max[0], cc1_min[0]], [cc1_max[1], cc1_min[1]], [cc1_max[2], cc1_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    co = ax.plot([co_max[0], co_min[0]], [co_max[1], co_min[1]], [co_max[2], co_min[2]], linewidth=5,
                  color=co_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    nh = ax.plot([nh_max[0], nh_min[0]], [nh_max[1], nh_min[1]], [nh_max[2], nh_min[2]], linewidth=5,
                 color=nh_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    ch = ax.plot([ch_max[0], ch_min[0]], [ch_max[1], ch_min[1]], [ch_max[2], ch_min[2]], linewidth=5,
                  color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ch1 = ax.plot([ch1_max[0], ch1_min[0]], [ch1_max[1], ch1_min[1]], [ch1_max[2], ch1_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ccc = ax.plot([ccc_max[0], ccc_min[0]], [ccc_max[1], ccc_min[1]], [ccc_max[2], ccc_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    cccn= ax.plot([cccn_max[0], cccn_min[0]], [cccn_max[1], cccn_min[1]], [cccn_max[2], cccn_min[2]], linewidth=5,
                  color=cn_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    cccnh1 = ax.plot([cccnh1_max[0], cccnh1_min[0]], [cccnh1_max[1], cccnh1_min[1]], [cccnh1_max[2], cccnh1_min[2]], linewidth=5,
                  color=nh_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    cccnh2 = ax.plot([cccnh2_max[0], cccnh2_min[0]], [cccnh2_max[1], cccnh2_min[1]], [cccnh2_max[2], cccnh2_min[2]], linewidth=5,
                  color=nh_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ccco = ax.plot([ccco_max[0], ccco_min[0]], [ccco_max[1], ccco_min[1]], [ccco_max[2], ccco_min[2]], linewidth=5,
                  color=co_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    cch2 = ax.plot([cch2_max[0], cch2_min[0]], [cch2_max[1], cch2_min[1]], [cch2_max[2], cch2_min[2]], linewidth=5,
                  color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    cch3 = ax.plot([cch3_max[0], cch3_min[0]], [cch3_max[1], cch3_min[1]], [cch3_max[2], cch3_min[2]], linewidth=5,
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
