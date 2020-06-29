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

def tryptophan(self):

    ch_min = [0, 0, 40]
    ch_max = [-20, 10, 70]

    cn_min = [0, 0, 40]
    cn_max =[-45,40, 10]

    cc_min = [0, 0,40]
    cc_max = [ 45,  -40, 10]

    co_min =[45, -40, 10]
    co_max =[ 60, -40, -50]

    nh_min = [-45,  40, 10]
    nh_max = [ -50,  40, -50]

    cc1_min = [0,  0, 40]
    cc1_max =[10,  -10, 70]

    cch1_min =[10, -10, 70]
    cch1_max = [ -40, 10,  90]

    cch2_min = [10, -10, 70, 90]
    cch2_max =[ -15, -40, 90]

    c3_min =[10, -10,70]
    c3_max = [ 35, -45, 120]

    pc1_min = [35,-45, 90]
    pc1_max =[ 35, -45, 120]

    pc2_min = [35,-45,120]
    pc2_max =[ 15, -85, 150]

    pc2h_min =[15, -85, 150]
    pc2h_max = [15, -85, 170]

    pc3_min = [15, -85, 150]
    pc3_max =[45, -100, 120]

    pc3nh_min = [45, -100, 120]
    pc3nh_max = [60, -120, 140]

    pc4_min =[45, -100, 120]
    pc4_max = [45, -100, 90]

    hex_cc_join_min = [35,-45,90]
    hex_cc_join_max = [45, -100, 90]

    hex_cc_join_1_min =[35, -45, 90]
    hex_cc_join_1_max = [ 10, -20, 60]

    hex_cc_join_1h_min = [10,-20,60]
    hex_cc_join_1h_max =[ -20, -40, 70]

    hex_cc_join_2_min =[10,-20, 60]
    hex_cc_join_2_max =[ 25, -45, 30]

    hex_cc_join_2h_min = [25, -45, 30]
    hex_cc_join_2h_max = [-5, -65, 40]

    hex_cc_join_3_min = [25, -45, 30]
    hex_cc_join_3_max = [65, -85,  35]

    hex_cc_join_3h_min =[65,-85, 35]
    hex_cc_join_3h_max =[ 45, -105, 45]

    hex_cc_join_4_min =[65, -85,35]
    hex_cc_join_4_max =[85, -100, 65]

    hex_cc_join_4h_min =[85, -100,65]
    hex_cc_join_4h_max =[45, -125, 80]

    hex_cc_join_5_min = [85, -100, 65]
    hex_cc_join_5_max = [ 45, -100, 90]

    fig = Figure(figsize=(10,6), dpi=100,facecolor='black')
    canvas = FigureCanvasTkAgg(fig, self)
    canvas.draw()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_axis_bgcolor("black")		 
    
    ch = ax.plot([ch_max[0], ch_min[0]], [ch_max[1], ch_min[1]], [ch_max[2], ch_min[2]], color=ch_color,
                 linewidth=5,marker='o', markerfacecolor='orange', markersize=12)

    cn = ax.plot([cn_max[0], cn_min[0]], [cn_max[1], cn_min[1]], [cn_max[2], cn_min[2]],
                  color= cn_color,linewidth=5,marker='o', markerfacecolor='orange', markersize=12)

    cc = ax.plot([cc_max[0], cc_min[0]], [cc_max[1], cc_min[1]], [cc_max[2], cc_min[2]],
                color=cc_color,linewidth=5,marker='o', markerfacecolor='orange', markersize=12)
    co= ax.plot([co_max[0], co_min[0]], [co_max[1], co_min[1]], [co_max[2], co_min[2]],
                color=co_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    nh =ax.plot([ nh_max[0],  nh_min[0]], [ nh_max[1],  nh_min[1]], [ nh_max[2],  nh_min[2]],
                color=nh_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    cc1 = ax.plot([ cc1_max[0],  cc1_min[0]], [ cc1_max[1],  cc1_min[1]], [ cc1_max[2],  cc1_min[2]],
                color=cc_color, linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    cch1 =ax.plot([ cch1_max[0],  cch1_min[0]], [ cch1_max[1],  cch1_min[1]], [ cch1_max[2],  cch1_min[2]],color=ch_color,
          linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    cch2 = ax.plot([ cch2_max[0],  cch2_min[0]], [ cch2_max[1],  cch2_min[1]], [ cch2_max[2],  cch2_min[2]],color=ch_color,
            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    c3 = ax.plot([ c3_max[0],  c3_min[0]], [ c3_max[1],  c3_min[1]], [ c3_max[2],  c3_min[2]],color=cc_color,
            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)
    pc1 = ax.plot([pc1_max[0], pc1_min[0]], [pc1_max[1], pc1_min[1]], [pc1_max[2], pc1_min[2]],  color=pc_color,
            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    pc2 = ax.plot([ pc2_max[0],  pc2_min[0]], [ pc2_max[1],  pc2_min[1]], [ pc2_max[2],  pc2_min[2]], color=pc_color,
            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)
    pc2h =ax.plot([ pc2h_max[0],  pc2h_min[0]], [ pc2h_max[1],  pc2h_min[1]], [ pc2h_max[2],  pc2h_min[2]],color=ch_color,
            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)
    pc3 = ax.plot([ pc3_max[0],  pc3_min[0]], [ pc3_max[1],  pc3_min[1]], [ pc3_max[2],  pc3_min[2]],color=pc_color,
            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)
    pc3nh =  ax.plot([pc3nh_max[0], pc3nh_min[0]], [pc3nh_max[1], pc3nh_min[1]], [pc3nh_max[2], pc3nh_min[2]], color=nh_color,
            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    pc4 = ax.plot([pc4_max[0], pc4_min[0]], [pc4_max[1], pc4_min[1]], [pc4_max[2], pc4_min[2]],
            color=pc_color,
            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    hex_cc_join=   ax.plot([ hex_cc_join_max[0],  hex_cc_join_min[0]], [ hex_cc_join_max[1],  hex_cc_join_min[1]], [ hex_cc_join_max[2],  hex_cc_join_min[2]],
            color=hex_join_color,
            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    hex_cc_join_1 = ax.plot([  hex_cc_join_1_max[0],   hex_cc_join_1_min[0]], [  hex_cc_join_1_max[1],   hex_cc_join_1_min[1]],
            [  hex_cc_join_1_max[2],   hex_cc_join_1_min[2]],
            color=hex_join_color,
            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)
    hex_cc_join_1h = ax.plot([ hex_cc_join_1h_max[0], hex_cc_join_1h_min[0]], [hex_cc_join_1h_max[1], hex_cc_join_1h_min[1]],
              [hex_cc_join_1h_max[2], hex_cc_join_1h_min[2]],color=ch_color,
              linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    hex_cc_join_2 = ax.plot([hex_cc_join_2_max[0], hex_cc_join_2_min[0]], [hex_cc_join_2_max[1], hex_cc_join_2_min[1]],
              [hex_cc_join_2_max[2], hex_cc_join_2_min[2]],
              color=hex_join_color,
              linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    hex_cc_join_2h = ax.plot([hex_cc_join_2h_max[0], hex_cc_join_2h_min[0]], [hex_cc_join_2h_max[1], hex_cc_join_2h_min[1]],
                            [hex_cc_join_2h_max[2], hex_cc_join_2h_min[2]],color=ch_color,
                            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    hex_cc_join_3 = ax.plot([hex_cc_join_3_max[0], hex_cc_join_3_min[0]], [hex_cc_join_3_max[1], hex_cc_join_3_min[1]],
                            [hex_cc_join_3_max[2], hex_cc_join_3_min[2]],
                            color=hex_join_color,
                            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    hex_cc_join_3h = ax.plot([hex_cc_join_3h_max[0], hex_cc_join_3h_min[0]], [hex_cc_join_3h_max[1], hex_cc_join_3h_min[1]],
                            [hex_cc_join_3h_max[2], hex_cc_join_3h_min[2]],color=ch_color,
                            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    hex_cc_join_4 = ax.plot([hex_cc_join_4_max[0], hex_cc_join_4_min[0]], [hex_cc_join_4_max[1], hex_cc_join_4_min[1]],
                            [hex_cc_join_4_max[2], hex_cc_join_4_min[2]],
                            color=hex_join_color,
                            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)
    hex_cc_join_4h = ax.plot([hex_cc_join_4h_max[0], hex_cc_join_4h_min[0]], [hex_cc_join_4h_max[1], hex_cc_join_4h_min[1]],
                            [hex_cc_join_4h_max[2], hex_cc_join_4h_min[2]],color=ch_color,
                            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)

    hex_cc_join_5= ax.plot([hex_cc_join_5_max[0], hex_cc_join_5_min[0]], [hex_cc_join_5_max[1], hex_cc_join_5_min[1]],
                            [hex_cc_join_5_max[2], hex_cc_join_5_min[2]],
                           color=hex_join_color,
                            linewidth=5, marker='o', markerfacecolor='orange', markersize=12)
    tch = plt.Rectangle((0, 0), 1, 1, fc=ch_color)
    tpc = plt.Rectangle((0, 0), 1, 1, fc=pc_color)
    tcn = plt.Rectangle((0, 0), 1, 1, fc=cn_color)
    tcc = plt.Rectangle((0, 0), 1, 1, fc=cc_color)
    tbco = plt.Rectangle((0, 0), 1, 1, fc=co_color)
    tbnh = plt.Rectangle((0, 0), 1, 1, fc=nh_color)
    thex_join_color = plt.Rectangle((0, 0), 1, 1, fc=hex_join_color)


    ax.legend([tch,tcn,tcc,tbco,tbnh,thex_join_color,tpc],['ch','cn','cc','co','nh','hex_join_color','pc'])
    ax.axis("off")  
    toolbarFrame = Frame(self)
    toolbarFrame.grid(row=6,column=7)
    toolbar = NavigationToolbar2TkAgg(canvas, toolbarFrame)
    canvas.get_tk_widget().grid(row=4,column=7) 

