import covid
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt
from matplotlib.font_manager import FontProperties

goth = FontProperties(fname="C:/Windows/Fonts/msgothic.ttc")

optitle = {
    "xycoords": "data",
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

def ex06(pref, odays, fac, epoch0, ndays, xlim, xticks, ylim, yticks, pngfile, log=False, rotation=28, pad=-2):
    filename = "newly_confirmed_cases_daily.csv"
    daily = covid.readCSV(filename)
    weekly1, weekly2 = covid.readXLSXfp()
    fig = plt.figure(figsize=(6, 4))
    ax = plt.axes([0.09, 0.11, 0.89, 0.83])
    xlim, xticks = [epoch0, epoch0 + dt.timedelta(days=ndays)], [epoch0 + dt.timedelta(days=i) for i in range(7, ndays, 4 * 7)]
    if log:
        ax.set_yscale("log")
    p = covid.prefecture[pref]
    covid.drawFrame(pref + "", optitle, ax, xlim, xticks, ylim, yticks, rotation=rotation, pad=pad)
    ax.set_title(pref + "定点あたりの報告数の日別陽性者数への変換", fontproperties=goth, size=12, pad=6)
    ax.text(0, 1.05, "Y210231 北村拓也", transform=ax.transAxes, fontproperties=goth, size=9)  
    ax.bar([d[0] for d in weekly2["Week"]], weekly2[pref]*fac, label=f"定点あたりの報告数 × {fac}", **{**opbar, "width": 7.0})
    ax.bar(fpmi["Week"], fac * np.array(fpmi[pref]), **{**opbar, "width": 7.0, "color": "orange"})
    daily[p + "7days"] = pd.Series(daily[p]).rolling(window=7, min_periods=1).mean()  # 7日間移動平均を計算
    ax.plot(daily["Date"] - np.timedelta64(odays, "D"), daily[p + "7days"], label=f"陽性者数7日間移動平均 (-{odays}日)", **opplot)
    ax.legend(prop=goth, loc="upper right", bbox_to_anchor=(1.0, 1.0))
    plt.show()
    fig.savefig(pngfile, dpi=600)

if __name__ == "__main__":
    epoch0, ndays = dt.datetime(2022, 1, 10), 82 * 7
    xlim, xticks = [epoch0, epoch0 + dt.timedelta(days=ndays)], [epoch0 + dt.timedelta(days=i) for i in range(7, ndays, 4 * 7)]
    pref, odays, fac, ylim, yticks = "鳥取県", 3, 70, [8, 8000], [1, 10, 100, 1000]
    ex06(pref, odays, fac, epoch0, ndays, xlim, xticks, ylim, yticks, "ex05.png", log=True)
