# -*- coding: utf-8 -*-
import aGSI
from matplotlib.font_manager import FontProperties 
import matplotlib. pyplot as plt 
import math


goth = FontProperties(fname="C:/Windows/Fonts/msgothic.ttc")

def ex08 (mesh, zname, pngfile):
    alt, idx = aGSI. readDEM (mesh)
    mesh_parts = mesh.split('-')
    mesh_part1 = mesh_parts[0]
    mesh_part2 = mesh_parts[1]
    lon0 = (int(mesh_part1[2:4])+int(mesh_part2[0])/8) + 100
    lon1 = lon0+1/8
    lat0 = (int(mesh_part1[0:2])+int(mesh_part2[1])/8)/1.5
    lati = lat0+1/12
    ...

#経度範囲
# 緯度範囲
    extent = [lon0, lon1, lat0, lati]
    aspect = 1/math. cos (math. radians (lat0+1/24))
#縦横比
    optext = {'xycoords': 'data', 'textcoords' :'offset points',"fontproperties":FontProperties (fname="C:/Windows/Fonts/msgothic.ttc")}
    fig = plt.figure (figsize= (6, 4))
    ax = plt.axes ([0.02, 0.07, 0.9, 0.9])
    ax. annotate (zname, xy=(lon1, lati), xytext=(7, -14), size=14, **optext)
    plt.title("Y210267 長瀬将起", fontproperties=goth)  # タイトルの設定
    im = ax.imshow (alt, aspect=aspect, extent=extent)
# 標高値[m］
# im = ax.imshow (idx, aspect=aspect, extent extent, cmap='RaBu') # #==r
    plt.colorbar (im, cax=plt.axes ([0.9, 0.1, 0.03, 0.75]))
# 凡例彩色
    plt.show ()
    fig.savefig (pngfile, dpi=600)

if __name__== "__main__":
    mesh, zname = "523537","瀬田"
    ex08 (mesh, zname, f'dem{mesh} .png')
# 図郭「瀬田」のメッシュ番号