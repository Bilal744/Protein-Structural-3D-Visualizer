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

def glutamine(self):
    ch_min = [0, 0, 40]
    ch_max = [-20, 30, 70]

    cn_min = [0, 0, 40]
    cn_max = [-45, 40, 10]

    cc1_min = [0, 0, 40]
    cc1_max = [45, -40, 10]

    co_min = [45, -40, 10]
    co_max = [60, -40, -50]

    nh_min = [-45, 40, 10]
    nh_max = [-50, 40, -50]

    cc_min = [0, 0, 40]
    cc_max = [40, -20, 70]

    ccc_min = [40, -20, 70]
    ccc_max = [80, -45, 60]

    ccch1_min = [80, -45, 60]
    ccch1_max = [70, -20, 40]

    ccch2_min = [80, -45, 60]
    ccch2_max = [110, -40, 70]

    cccc_min = [80, -45, 60]
    cccc_max = [125, -70, 100]

    ccccn1_min = [125, -70, 100]
    ccccn1_max = [175, -85, 80]

    ccccnh1_min = [175, -85, 80]
    ccccnh1_max = [145, -130, 40]

    ccccnh2_min = [175, -85, 80]
    ccccnh2_max = [185, -110, 40]

    cccco_min = [125, -70, 100]
    cccco_max = [145, -45, 80]

    cch2_min = [40, -20, 70]
    cch2_max = [50, -50, 100]

    cch3_min = [40, -20, 70]
    cch3_max = [25, 10, 100]

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
    ccl = ax.plot([cc1_max[0], cc1_min[0]], [cc1_max[1], cc1_min[1]], [cc1_max[2], cc1_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    co = ax.plot([co_max[0], co_min[0]], [co_max[1], co_min[1]], [co_max[2], co_min[2]], linewidth=5,
                  color=co_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    nh = ax.plot([nh_max[0], nh_min[0]], [nh_max[1], nh_min[1]], [nh_max[2], nh_min[2]], linewidth=5,
                 color=nh_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    cc = ax.plot([cc_max[0], cc_min[0]], [cc_max[1], cc_min[1]], [cc_max[2], cc_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)

    cch2 = ax.plot([cch2_max[0], cch2_min[0]], [cch2_max[1], cch2_min[1]], [cch2_max[2], cch2_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)
    cch3 = ax.plot([cch3_max[0], cch3_min[0]], [cch3_max[1], cch3_min[1]], [cch3_max[2], cch3_min[2]], linewidth=5,
                   color=ch_color,
                   marker='o', markerfacecolor='orange', markersize=12)

    ccc = ax.plot([ccc_max[0], ccc_min[0]], [ccc_max[1], ccc_min[1]], [ccc_max[2], ccc_min[2]], linewidth=5,
                  color=cc_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ccch1= ax.plot([ccch1_max[0], ccch1_min[0]], [ccch1_max[1], ccch1_min[1]], [ccch1_max[2], ccch1_min[2]], linewidth=5,
                 color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)
    ccch2 = ax.plot([ccch2_max[0], ccch2_min[0]], [ccch2_max[1], ccch2_min[1]], [ccch2_max[2], ccch2_min[2]], linewidth=5,
                  color=ch_color,
                  marker='o', markerfacecolor='orange', markersize=12)






    cccc = ax.plot([cccc_max[0], cccc_min[0]], [cccc_max[1], cccc_min[1]], [cccc_max[2], cccc_min[2]], linewidth=5,
                 color=cc_color,
                marker='o', markerfacecolor='orange', markersize=12)

    ccccn1 = ax.plot([ccccn1_max[0], ccccn1_min[0]], [ccccn1_max[1], ccccn1_min[1]], [ccccn1_max[2], ccccn1_min[2]], linewidth=5,
                 color=cn_color,
                 marker='o', markerfacecolor='orange', markersize=12)
    ccccnh1 = ax.plot([ccccnh1_max[0], ccccnh1_min[0]], [ccccnh1_max[1], ccccnh1_min[1]], [ccccnh1_max[2], ccccnh1_min[2]],
                     linewidth=5,
                     color=nh_color,
                     marker='o', markerfacecolor='orange', markersize=12)
    ccccnh2 = ax.plot([ccccnh2_max[0], ccccnh2_min[0]], [ccccnh2_max[1], ccccnh2_min[1]], [ccccnh2_max[2], ccccnh2_min[2]],
                     linewidth=5,
                     color=nh_color,
                     marker='o', markerfacecolor='orange', markersize=12)
    cccco = ax.plot([cccco_max[0], cccco_min[0]], [cccco_max[1], cccco_min[1]], [cccco_max[2], cccco_min[2]], linewidth=5,
                  color=co_color,
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

