#-*- coding: utf-8-*-

import aGSIA
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import math

def ex08 (mesh, zname, pngfile):
    alt, idx = aGSIA.readDEM (mesh)
    lon0 = (int(mesh[2:4])+int(mesh[5])/8)+100; lon1 = lon0+1/8
    lat0 = (int(mesh[0:2])+int(mesh[4])/8)/1.5; lat1 = lat0+1/12
    extent = [lon0, lon1, lat0, lat1]
    aspect = 1/math.cos (math.radians (lat0+1/24))
    optext = {'xycoords':'data', 'textcoords':'offset points', 'fontproperties':FontProperties (fname="C:/Windows/Fonts/msgothic.ttc")}
    fig=plt.figure (figsize=(6,4))
    ax = plt.axes ([0.02, 0.07, 0.9, 0.9])
    ax.annotate (zname, xy=(lon1,lat1),xytext=(7,-14),size=14, **optext)
    im=ax.imshow(alt, aspect=aspect, extent=extent) 
   #im=ax.imshow(idx, aspect=aspect, extent=extent, cmap='RdBu')
    plt.colorbar (im, cax=plt.axes([0.9,0.1,0.03,0.75]))
    plt.show()
    fig.savefig(pngfile, dpi=600)

if __name__ =='__main__':
    mesh, zname = '523537', '瀬田    Y210235久保智大'
    ex08 (mesh, zname, f'dem{mesh}.png')