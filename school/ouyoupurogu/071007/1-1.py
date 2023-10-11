#-*- coding: utf-8 -*-

import aGSI

if __name__ == "__main__":
    mesh = '523537'
    alt, idx = aGSI.readDEM (mesh, debug=2)
    print ("標高値", type (alt), alt.shape); print (alt)
    print("標高モデル",type (idx), idx.shape); print (idx)