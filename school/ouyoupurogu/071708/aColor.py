# -*- coding: utf-8 -*-
import matplotlib.colors as mcolors

def makeCmap(ctable):
  n = len (ctable)-3
  norm = mcolors.BoundaryNorm ([t[0] for t in ctable[1:]], n+1)
  palette = [t[1] for t in ctable]
  clist = []
  for i, p in enumerate (palette[1:n+2]):
    clist.append ((i/n, mcolors.hsv_to_rgb (p)))
  cmap = mcolors.LinearSegmentedColormap.from_list ('mymap', clist, n+1)
  cmap.set_under (mcolors.hsv_to_rgb (palette[0]))
  cmap.set_over (mcolors.hsv_to_rgb (palette[n+2]))
  return norm, cmap


import scipy.ndimage as ndi
import numpy as np
import math

def Laplacian (arr, idx):
  w = np.array ([[0.25, 0.75, 0.25], [0.75, -4, 0.75], [0.25, 0.75, 0.25]])
  shade = ndi.convolve (arr, w, mode='nearest')
  if idx.min != 0:
    w10 = 0.25*np.array ([[0.25, 0, 0.75, 0, 0.25], [0, 0, 0, 0, 0],
      [0.75, 0, -4, 0, 0.75], [0, 0, 0, 0, 0], [0.25, 0, 0.75, 0, 0.25]])
    shade10 = ndi.convolve (arr, w10, mode='nearest')
    idx10 = np.where (idx == 0)
    shade[idx10] = shade10[idx10]
  return shade

def shading (rgbaimage, alt, idx,
  sp2 = 0.07, kp2 = 0.40, sm2 = 0.70, km2 = 0.20,
  sp1 = 2.00, kp1 = 0.00, sm1 = 0.03, km1 = 0.1):
  hsvimage = mcolors.rgb_to_hsv (rgbaimage[:,:,:3]/255)         # HSV画像へ変換
  shade = Laplacian (alt, idx)                                  # 二回差分の計算
  hsvimage[:,:,2] += [[-kp2*(sp2+math.log10 (+s+1-sp2)) if s > +sp2 else
                       -kp2*s if s >= 0 else
                       +km2*(sm2+math.log10 (-s+1-sm2)) if s < -sm2 else
                       +km2*s for s in t] for t in shade]       # 明度
  hsvimage[:,:,1] += [[+kp1*(sp1+math.log10 (+s+1-sp1)) if s > +sp1 else
                       +kp1*s if s >= 0 else
                       -km1*(sm1+math.log10 (-s+1-sm1)) if s < -sm1 else
                       -km1*s for s in t] for t in shade]       # 彩度
  return mcolors.hsv_to_rgb (np.clip (hsvimage, 0, 1))          # RGB画像に戻す