#coding: utf-8   #ユニコード

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

coding: utf-8   #ユニコード

def ex02(pngfile):
    optext = {"xycoords":"data", "textcoords":"offset points", "fontproperties":FontProperties(fname="c:\Windows\Fonts")}
    fig = plt.figure(figsize=(6,4))
    ax = plt.axes([0.05, 0.05, 0.9, 0.9])
    ax.set_xlim(0,9)
    ax.set_ylim(0,6)
    title = "吾輩は猫である"
    autohr = "夏目　漱石"
    jtext = (
        "吾輩は猫である。名前はまだない。"
    )

    ax.annotate(title, xy = (4.5, 5), ha = "center", size = 32 , alpha = 0.7, **optext)
    ax.annotate(autohr, xy=(4.5,5), xytext=(60,-30), size = 20, **optext)
    ax.annotate(jtext, xy=(1,3.3), va ="top", size = 13, linespacing = 1.6, **optext)
    plt.show()
    fig.savefig(pngfile,dpi = 600)

if __name__ == "__main__":
    plt.style.use("bmh")
    ex02("iamacat.png")