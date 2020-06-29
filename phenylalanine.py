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

def phenylalanine(self):
    ch_min = [0, 0, 40]
    ch_max = [-20, 10, 70]

    cn_min = [0, 0, 40]
    cn_max = [-45, 40, 10]

    cc_min = [0, 0, 40]
    cc_max = [45, -40, 10]

    co_min = [45, -40, 10]
    co_max = [60, -40, -50]

    nh_min = [-45, 40, 10]
    nh_max = [-50, 40, -50]

    cc1_min = [0, 0, 40]
    cc1_max = [10, -10, 70]

    cch1_min = [10, -10, 70]
    cch1_max = [20, -15, 50]

    cch2_min = [10, -10, 70]
    cch2_max = [5, -30, 50]

    cch3_min = [10, -10, 70]
    cch3_max = [35, -45, 90]

    pc1_min = [35, -45, 90]
    pc1_max = [35, -45, 120]

    pc1h_min = [35, -45, 120]
    pc1h_max = [25, -25, 140]

    pc2_min = [35, -45, 120]
    pc2_max = [15, -85, 150]

    pc2h_min = [15, -85, 150]
    pc2h_max = [15, -85, 170]

    pc3_min = [15, -85, 150]
    pc3_max = [45, -100, 120]

    pc3h_min = [45, -100, 120]
    pc3h_max = [25, -120, 130]

    pc4_min = [45, -100, 120]
    pc4_max = [45, -100, 90]

    pc4h_min = [45, -100, 90]
    pc4h_max = [25, -120, 80]

    pc5_min = [45, -100, 90]
    pc5_max = [45, -70, 50]

    pc5h_min = [45, -70, 50]
    pc5h_max = [45, -70, 30]

    pc6_min = [45, -70, 50]
    pc6_max = [35, -45, 90]
 
    fig = Figure(figsize=(10,6), dpi=100,facecolor='black')
    canvas = FigureCanvasTkAgg(fig, self)
    canvas.draw()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_axis_bgcolor("black")	

    ch = ax.plot([ch_max[0], ch_min[0]], [ch_max[1], ch_min[1]], [ch_max[2], ch_min[2]], linewidth=5,
                 color=ch_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    cn = ax.plot([cn_max[0], cn_min[0]], [cn_max[1], cn_min[1]], [cn_max[2], cn_min[2]], linewidth=5,
                 color=cn_color,
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
    ccl = ax.plot([cc1_max[0], cc1_min[0]], [cc1_max[1], cc1_min[1]], [cc1_max[2], cc1_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    cc1 = ax.plot([cc1_max[0], cc1_min[0]], [cc1_max[1], cc1_min[1]], [cc1_max[2], cc1_min[2]], linewidth=5,
                 color=cc_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    cch1 = ax.plot([cch1_max[0], cch1_min[0]], [cch1_max[1], cch1_min[1]], [cch1_max[2], cch1_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    cch2 = ax.plot([cch2_max[0], cch2_min[0]], [cch2_max[1], cch2_min[1]], [cch2_max[2], cch2_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    cch3 = ax.plot([cch3_max[0], cch3_min[0]], [cch3_max[1], cch3_min[1]], [cch3_max[2], cch3_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    pc1 = ax.plot([pc1_max[0], pc1_min[0]], [pc1_max[1], pc1_min[1]], [pc1_max[2], pc1_min[2]], linewidth=5,
                   color=pc_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    pc1h = ax.plot([pc1h_max[0], pc1h_min[0]], [pc1h_max[1], pc1h_min[1]], [pc1h_max[2], pc1h_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    pc2 = ax.plot([pc2_max[0], pc2_min[0]], [pc2_max[1], pc2_min[1]], [pc2_max[2], pc2_min[2]], linewidth=5,
                  color=pc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    pc2h = ax.plot([pc2h_max[0], pc2h_min[0]], [pc2h_max[1], pc2h_min[1]], [pc2h_max[2], pc2h_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    pc3 = ax.plot([pc3_max[0], pc3_min[0]], [pc3_max[1], pc3_min[1]], [pc3_max[2], pc3_min[2]], linewidth=5,
                  color=pc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    pc3h = ax.plot([pc3h_max[0], pc3h_min[0]], [pc3h_max[1], pc3h_min[1]], [pc3h_max[2], pc3h_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    pc4 = ax.plot([pc4_max[0], pc4_min[0]], [pc4_max[1], pc4_min[1]], [pc4_max[2], pc4_min[2]], linewidth=5,
                  color=pc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    pc4h = ax.plot([pc4h_max[0], pc4h_min[0]], [pc4h_max[1], pc4h_min[1]], [pc4h_max[2], pc4h_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    pc5 = ax.plot([pc5_max[0], pc5_min[0]], [pc5_max[1], pc5_min[1]], [pc5_max[2], pc5_min[2]], linewidth=5,
                  color=pc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    pc5h = ax.plot([pc5h_max[0], pc5h_min[0]], [pc5h_max[1], pc5h_min[1]], [pc5h_max[2], pc5h_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    pc6 = ax.plot([pc6_max[0], pc6_min[0]], [pc6_max[1], pc6_min[1]], [pc6_max[2], pc6_min[2]], linewidth=5,
                  color=pc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    tch = plt.Rectangle((0, 0), 1, 1, fc=ch_color)
    tpc = plt.Rectangle((0, 0), 1, 1, fc=pc_color)
    tcn = plt.Rectangle((0, 0), 1, 1, fc=cn_color)
    tcc = plt.Rectangle((0, 0), 1, 1, fc=cc_color)
    tbco = plt.Rectangle((0, 0), 1, 1, fc=co_color)
    tbnh = plt.Rectangle((0, 0), 1, 1, fc=nh_color)


    ax.legend([tch,tcn,tcc,tbco,tbnh,tpc],['ch','cn','cc','co','nh','pc'])

    ax.axis("off")  
    toolbarFrame = Frame(self)
    toolbarFrame.grid(row=6,column=7)
    toolbar = NavigationToolbar2TkAgg(canvas, toolbarFrame)
    canvas.get_tk_widget().grid(row=4,column=7) 

