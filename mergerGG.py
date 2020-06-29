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



def mergerGG(self):
    cn_min =[-45,40,10]
    cn_max = [ -90, 80, 40]

    ch_min =[0, 0, 40]
    ch_max = [-10, 10, 70]

    ch1_min = [0, 0,40]
    ch1_max =[10,-10, 70]

    cc_min = [0, 0,40]
    cc_max =[ -45, 40, 10]

    cn1_min =[0, 0, 40]
    cn1_max =[45, -40, 10]

    nh_min = [45,-40, 10]
    nh_max =[60, -40,-50]

    co_min = [-45, 40,10]
    co_max = [-50, 40, -50]

    # 2nd amino acid
    cnbond_min = [-45,40,10]
    cnbond_max = [-90, 80, 40]

    nh1_min = [-90, 80, 40]
    nh1_max = [ -90, 80, 60]

    nc_min = [-90,80, 40]
    nc_max =[-100, 130, 10]

    nch1_min = [-100, 130,10]
    nch1_max = [-120, 150, -30]

    nch2_min = [-100,130,10]
    nch2_max =[-80, 150, -20]

    ncc_min =[-100,130, 10]
    ncc_max =[-60, 190, 30]

    nco_min = [-60, 190, 30]
    nco_max = [-60, 190, 70]
    ##########################################################################

    fig = Figure(figsize=(10,6), dpi=100,facecolor='black')
    canvas = FigureCanvasTkAgg(fig, self)
    canvas.draw()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_axis_bgcolor("black")	

    ch = ax.plot([ch_max[0], ch_min[0]], [ch_max[1], ch_min[1]], [ch_max[2], ch_min[2]], color=ch_color,
                 linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    cn = ax.plot([cn_max[0], cn_min[0]], [cn_max[1], cn_min[1]], [cn_max[2], cn_min[2]],
                 color=cn_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    cc = ax.plot([cc_max[0], cc_min[0]], [cc_max[1], cc_min[1]], [cc_max[2], cc_min[2]],
                 color=cc_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    ch1 = ax.plot([ch1_max[0], ch1_min[0]], [ch1_max[1], ch1_min[1]], [ch1_max[2], ch1_min[2]],
                 color=ch_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)
    co = ax.plot([co_max[0], co_min[0]], [co_max[1], co_min[1]], [co_max[2], co_min[2]],
                 color=co_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    nh = ax.plot([nh_max[0], nh_min[0]], [nh_max[1], nh_min[1]], [nh_max[2], nh_min[2]],
                 color=nh_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    cn1 = ax.plot([cn1_max[0], cn1_min[0]], [cn1_max[1], cn1_min[1]], [cn1_max[2], cn1_min[2]],
                 color=cn_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    cnbond = ax.plot([cnbond_max[0], cnbond_min[0]], [cnbond_max[1], cnbond_min[1]], [cnbond_max[2], cnbond_min[2]],
                  color=(1,0.9,0.9), linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    nh1 = ax.plot([nh1_max[0], nh1_min[0]], [nh1_max[1], nh1_min[1]], [nh1_max[2], nh1_min[2]],
                  color=nh_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    nc = ax.plot([nc_max[0], nc_min[0]], [nc_max[1], nc_min[1]], [nc_max[2], nc_min[2]],
                  color=cn_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    nch1 = ax.plot([nch1_max[0], nch1_min[0]], [nch1_max[1], nch1_min[1]], [nch1_max[2], nch1_min[2]],
                  color=ch_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    nch2 = ax.plot([nch2_max[0], nch2_min[0]], [nch2_max[1], nch2_min[1]], [nch2_max[2], nch2_min[2]],
                  color=ch_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    ncc = ax.plot([ncc_max[0], ncc_min[0]], [ncc_max[1], ncc_min[1]], [ncc_max[2], ncc_min[2]],
                   color=cc_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    nco = ax.plot([nco_max[0], nco_min[0]], [nco_max[1], nco_min[1]], [nco_max[2], nco_min[2]],
                   color=co_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)
    tch = plt.Rectangle((0, 0), 1, 1, fc=ch_color)
    tcnbond = plt.Rectangle((0, 0), 1, 1, fc=(1,0.9,0.9))
    tcn = plt.Rectangle((0, 0), 1, 1, fc=cn_color)
    tcc = plt.Rectangle((0, 0), 1, 1, fc=cc_color)
    tbco = plt.Rectangle((0, 0), 1, 1, fc=co_color)
    tbnh = plt.Rectangle((0, 0), 1, 1, fc=nh_color)


    ax.legend([tch,tcn,tcc,tbco,tbnh,tcnbond],['ch','cn','cc','co','nh','cnbond'])

    ax.axis("off")  
    toolbarFrame = Frame(self)
    toolbarFrame.grid(row=6,column=7)
    toolbar = NavigationToolbar2TkAgg(canvas, toolbarFrame)
    canvas.get_tk_widget().grid(row=4,column=7) 

