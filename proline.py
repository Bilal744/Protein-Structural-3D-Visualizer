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


def proline(self):
    co_min = [45,-40,10]
    co_max = [60,-40,-50]

    cc_min = [0, 0, 40]
    cc_max = [45,  -40,  10]

    cch_min = [0, 0, 40]
    cch_max = [ 20, -20,  -10]

    cc2_min = [0, 0, 40,]
    cc2_max = [-85, -40, 10]

    cc2h1_min = [-85, -40, 10]
    cc2h1_max = [-45,-20, -20]




    cc2h2_min = [-85,-40,10]
    cc2h2_max = [-105, -60, -20]

    ccn_min =[0,  0, 40]
    ccn_max = [-40, 60, 80]

    c2nc_min = [-40, 60, 80]
    c2nc_max =[-90, 40, 100]

    c2nch1_min = [-90,40,100]
    c2nch1_max = [-60, 60, 120]

    c2nch2_min = [-90, 40, 100]
    c2nch2_max = [-120, 20, 120]

    c3_min = [-85, -40, 10]
    c3_max = [-120,20, 50]

    c3h1_min = [-120,  20,  50]
    c3h1_max = [-150, 50,20]

    c3h2_min = [-120, 20,50]
    c3h2_max = [-160, 50, 80]

    c4_min = [-120,20,50]
    c4_max = [ -90, 40, 100]

    fig = Figure(figsize=(10,6), dpi=100,facecolor='black')
    canvas = FigureCanvasTkAgg(fig, self)
    canvas.draw()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_axis_bgcolor("black")		 
    
    co = ax.plot([co_max[0], co_min[0]], [co_max[1], co_min[1]], [co_max[2], co_min[2]],
                 linewidth=5, color=co_color, marker='o', markerfacecolor='orange', markersize=12)
    cc = ax.plot([cc_max[0], cc_min[0]], [cc_max[1], cc_min[1]], [cc_max[2], cc_min[2]],
                 linewidth=5, color=cc_color, marker='o', markerfacecolor='orange', markersize=12)

    cch = ax.plot([cch_max[0], cch_min[0]], [cch_max[1], cch_min[1]], [cch_max[2], cch_min[2]],
                  linewidth=5, color=ch_color, marker='o', markerfacecolor='orange', markersize=12)

    cc2 = ax.plot([cc2_max[0], cc2_min[0]], [cc2_max[1], cc2_min[1]], [cc2_max[2], cc2_min[2]],
                  linewidth=5, color=cc_color, marker='o', markerfacecolor='orange', markersize=12)

    cc2h1 = ax.plot([cc2h1_max[0], cc2h1_min[0]], [cc2h1_max[1], cc2h1_min[1]], [cc2h1_max[2], cc2h1_min[2]],
                    linewidth=5, color=ch_color, marker='o', markerfacecolor='orange', markersize=12)

    cc2h2 = ax.plot([cc2h2_max[0], cc2h2_min[0]], [cc2h2_max[1], cc2h2_min[1]], [cc2h2_max[2], cc2h2_min[2]],
                    linewidth=5, color=ch_color, marker='o', markerfacecolor='orange', markersize=12)

    ccn = ax.plot([ccn_max[0], ccn_min[0]], [ccn_max[1], ccn_min[1]], [ccn_max[2], ccn_min[2]],
                  linewidth=5, color=cn_color, marker='o', markerfacecolor='orange', markersize=12)

    c2nc = ax.plot([c2nc_max[0], c2nc_min[0]], [c2nc_max[1], c2nc_min[1]], [c2nc_max[2], c2nc_min[2]],
                   linewidth=5, color=cn_color, marker='o', markerfacecolor='orange', markersize=12)

    c2nch1 = ax.plot([c2nch1_max[0], c2nch1_min[0]], [c2nch1_max[1], c2nch1_min[1]], [c2nch1_max[2], c2nch1_min[2]],
                     linewidth=5, color=ch_color, marker='o', markerfacecolor='orange', markersize=12)

    c2nch2 = ax.plot([c2nch2_max[0], c2nch2_min[0]], [c2nch2_max[1], c2nch2_min[1]], [c2nch2_max[2], c2nch2_min[2]],
                     linewidth=5, color=ch_color, marker='o', markerfacecolor='orange', markersize=12)

    c3 = ax.plot([c3_max[0], c3_min[0]], [c3_max[1], c3_min[1]], [c3_max[2], c3_min[2]],
                 linewidth=5, color=cc_color, marker='o', markerfacecolor='orange', markersize=12)
    c3h1 = ax.plot([c3h1_max[0], c3h1_min[0]], [c3h1_max[1], c3h1_min[1]], [c3h1_max[2], c3h1_min[2]],
                   linewidth=5, color=ch_color, marker='o', markerfacecolor='orange', markersize=12)
    c3h2 = ax.plot([c3h2_max[0], c3h2_min[0]], [c3h2_max[1], c3h2_min[1]], [c3h2_max[2], c3h2_min[2]],
                   linewidth=5, color=ch_color, marker='o', markerfacecolor='orange', markersize=12)

    c4 = ax.plot([c4_max[0], c4_min[0]], [c4_max[1], c4_min[1]], [c4_max[2], c4_min[2]],
                 linewidth=5, color=cc_color, marker='o', markerfacecolor='orange', markersize=12)
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

