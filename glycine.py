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


def glycine(self):
    ch_max = [-10, 10, 70]
    ch_min = [0, 0, 40]

    ch1_min = [0, 0, 40]
    ch1_max = [10, -10, 70]

    cn_min = [0, 0, 40]
    cn_max = [-45, 40, 10]

    cc_min = [0, 0, 40]
    cc_max = [45, -40, 10]

    bco_min = [45, -40, 10]
    bco_max = [60, -40, -40]

    bnh_min = [-45, 40, 10]
    bnh_max = [-50, 40, -50]

    fig = Figure(figsize=(10,6), dpi=100,facecolor='black')
    canvas = FigureCanvasTkAgg(fig, self)
    canvas.draw()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_axis_bgcolor("black")		 
    
    ch=ax.plot([ch_max[0],ch_min[0]],[ch_max[1],ch_min[1]],[ch_max[2],ch_min[2]],linewidth=5,color=ch_color,marker='o', markerfacecolor='orange', markersize=12)
    ch1 = ax.plot([ch1_max[0],ch1_min[0]],[ch1_max[1],ch1_min[1]],[ch1_max[2],ch1_min[2]],linewidth=5,color=ch_color,marker='o', markerfacecolor='orange', markersize=12)
    cn = ax.plot([cn_max[0],cn_min[0]],[cn_max[1],cn_min[1]],[cn_max[2],cn_min[2]],linewidth=5,color=cn_color,marker='o', markerfacecolor='orange', markersize=12)
    cc = ax.plot ([cc_max[0],cc_min[0]],[cc_max[1],cc_min[1]],[cc_max[2],cc_min[2]],linewidth=5,color=cc_color,marker='o', markerfacecolor='orange', markersize=12)
    bco = ax.plot([bco_max[0],bco_min[0]],[bco_max[1],bco_min[1]],[bco_max[2],bco_min[2]],linewidth=5,color=co_color,marker='o', markerfacecolor='orange', markersize=12)
    bnh =ax.plot([bnh_max[0],bnh_min[0]],[bnh_max[1],bnh_min[1]],[bnh_max[2],bnh_min[2]],linewidth=5,color=nh_color,marker='o', markerfacecolor='orange', markersize=12)
    
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

