# -*- coding: utf-8 -*-

import covid
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from matplotlib.font_manager import FontProperties

goth = FontProperties(fname="C:/Windows/Fonts/msgothic.ttc")

optitle = {
    "textcoords": "offset points",
    "fontproperties": goth,
    "size": 12
}

opbar = {
    "align": "center",
    "width": 1.0,
    "alpha": 0.3,
    "color": "blue"
}

opplot = {
    "linewidth": 1.2,
    "alpha": 0.7,
    "color": "blue"
}


fpmi = {
    "Week": [dt.date(2023, 5, 8), dt.date(2023, 5, 15), dt.date(2023, 5, 22), dt.date(2023, 5, 29)],
    "東京都": [2.40, 3.53, 3.96, 5.29],
    "滋賀県": [1.82, 2.07, 1.77, 2.47],
    "鳥取県": [2.69, 3.24, 2.86, 4.24],
    "全国": [2.63, 3.55, 3.63, 4.55]
}

def ex05(pref, epoch0, ndays, xlim, xticks, ylim, yticks, pngfile, fac=1, log=False, rotation=28, pad=-2):
    weekly1, weekly2 = covid.readXLSXfp()
    daily = covid.readCSV("newly_confirmed_cases_daily.csv")
    fig = plt.figure(figsize=(6, 5))
    ax = plt.axes([0.1, 0.12, 0.88, 0.78])
    xlim, xticks = [epoch0, epoch0 + dt.timedelta(days=ndays)], [epoch0 + dt.timedelta(days=i) for i in range(7, ndays, 4 * 7)]
    if log:
        ax.set_yscale("log")
    p = covid.prefecture[pref]
    covid.drawFrame("Y21231", optitle, ax, xlim, xticks, ylim, yticks, rotation=rotation, pad=pad)
    ax.set_title(pref + "定点医療機関 定点あたりの報告数", fontproperties=goth, size=12, pad=20)
    ax.bar([d[0] for d in weekly2["Week"]], weekly2[pref] * fac, label="定点あたりの報告数", **{**opbar, "width": 7.0})
    ax.bar(fpmi["Week"], np.array(fpmi[pref]) * fac, **{**opbar, "width": 7.0, "color": "orange"})
    ax.plot(daily["Date"], daily[p + " 7days"], label="7日間移動平均", **opplot)
    ax.legend(prop=goth, loc="upper right", bbox_to_anchor=(1.0, 1.0))
    plt.show()
    fig.savefig(pngfile, dpi=600)

if __name__ == "__main__":
    epoch0, ndays = dt.datetime(2022, 1, 10), 82 * 7
    xlim, xticks = [epoch0, epoch0 + dt.timedelta(days=ndays)], [epoch0 + dt.timedelta(days=i) for i in range(7, ndays, 4 * 7)]
    pref, ylim, yticks = "滋賀県", [0.2, 200], [1, 10, 100, 1000, 10000]
    ex05(pref, epoch0, ndays, xlim, xticks, ylim, yticks, "ex05.png", fac=70, log=True)
