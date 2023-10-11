# -*- coding: utf-8 -*-
import aGSI, aColor
from matplotlib.font_manager import FontProperties 
import matplotlib.pyplot as plt
import math

ctable =[( 0, [0.00, 0.0, 0.70]), # altitude, [Hue, Saturation, Value]
         (70, [0.76, 0.7,0.80]),
         (80, [0.73, 0.7,0.80]),
         (83, [0.70, 0.7,0.80]),
         (85, [0.65, 0.7,0.80]),
         (86, [0.60, 0.7,0.80]),
         (87, [0.55, 0.7,0.80]),
         (88, [0.50, 0.7,0.80]),
         (89, [0.45, 0.7,0.80]),
         (90, [0.40, 0.7,0.801]),
         (95, [0.30, 0.7,0.80]),
         (100, [0.20, 0.7,0.81]), 
         (110, [0.15, 0.7,0.82]), 
         (120, [0.13, 0.8,0.83]), 
         (140, [0.12, 0.9,0.84]),
         (170, [0.11, 1.0,0.85]), 
         (200, [0.10, 1.0,0.87]), 
         (300, [0.10, 1.0,0.89]), 
         (400, [0.10, 1.0,0.91]), 
         (500, [0.10, 1.0,0.93]), 
         (3000, [0.10, 1.0,0.95])]

def ex09 (mesh, date, zname,pngfile):
    alt, idx = aGSI. readDEM (mesh)
    wa = aGSI.readArea(f' FG-GML-{mesh}-WA-{date}') #基盤地図情報水域 lon0 = (int (mesh [2:4])+int (mesh [5]) /8) +100; lon1 = lon0+1/8
    lon0 = (int (mesh [2:4])+int (mesh [5])/8) /100; lon1 = lon0+1/12
    lat0 = (int (mesh [0:2])+int (mesh [4])/8) /1.5; lat1 = lat0+1/12
    extent = [lon0, lon1, lat0, lat1]
    aspect = 1/math.cos (math.radians (lat0+1/24))
    optext = {'xycoords': 'data', 'textcoords': 'offset points', 'fontproperties':
        FontProperties (fname="C:/Windows/Fonts/msgothic.ttc")}
    fig = plt.figure (figsize= (6, 4))
    ax = plt.axes ([0.02, 0.07, 0.9, 0.9])
    ax.annotate(zname, xy=(lon1, lat1), xytext=(7, -14), size=14, **optext)
    norm, cmap = aColor.makeCmap(ctable)
# カラ ーマップの作成
    im = plt.imshow (alt, norm=norm, cmap=cmap, aspect=aspect, extent=extent) # i t mi 
    im2 = aColor.shading (im.make_image (plt, unsampled=True) [0], alt, idx) # RaI
    ax.imshow (im2, aspect=aspect, extent=extent)
    aGSI. drawArea (ax, wa, None, None, linewidth=0, alpha=1,facecolor='#8080c0')
    plt.colorbar (im, cax=plt.axes ([0.9, 0.1, 0.03, 0.75])) 
    plt.show()
    fig.savefig (pngfile, dpi=600)

if __name__ == '__main__':
    mesh, date, zname = '523537', '20220401', '瀬田 Y210231北村拓也'
    ex09(mesh, date, zname, f'dem{mesh}C.png' )