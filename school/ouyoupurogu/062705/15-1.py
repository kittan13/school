import covid
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt
from matplotlib.font_manager import FontProperties
import pytz  # Add this import to handle time zones

goth = FontProperties(fname="C:/Windows/Fonts/msgothic.ttc")

optitle = {
    "xycoords": "data",
    "textcoords": "offset points",
    "fontproperties": goth,
    "size": 12
}

opplot = {
    "linewidth": 1.2,
    "alpha": 0.7,
    "color": "blue"
}


fpmi = {
    "Week": [dt.date(2023,5, 8), dt.date(2023, 5, 15), dt.date(2023, 5, 22), dt.date(2023, 5, 29), dt.date(2023, 6, 5), dt.date(2023, 6, 12), dt.date(2023, 6, 19), dt.date(2023, 6, 26)],
    "東京都": [2.40, 3.53, 3.96, 5.29],
    "滋賀県": [1.82, 2.07, 1.77, 2.47],
    "鳥取県": [2.69, 3.24, 2.86, 4.24],
    "全国": [2.63, 3.55, 3.63, 4.55],
    "大阪府":[1.79, 2.37, 2.75, 3.33, 4.33, 4.55, 5.16, 5.93]
}

def ex06(pref, odays, fac, epoch0, ndays, xlim, xticks, ylim, yticks, pngfile, log=False, rotation=28, pad=-2):
    filename = "newly_confirmed_cases_daily.csv"
    daily = covid.readCSV(filename)
    weekly1, weekly2 = covid.readXLSXfp()
    fig = plt.figure(figsize=(6, 5))
    ax = plt.axes([0.09, 0.11, 0.89, 0.83])
    xlim, xticks = [epoch0, epoch0 + dt.timedelta(days=ndays)], [epoch0 + dt.timedelta(days=i) for i in range(7, ndays, 4 * 7)]
    if log:
        ax.set_yscale("log")
    p = covid.prefecture[pref]
    covid.drawFrame("", optitle, ax, xlim, xticks, ylim, yticks, rotation=rotation, pad=pad)
    ax.set_title("大阪府 定点あたりの報告数の日別陽性者数への変換", fontproperties=goth, size=12, pad=4)
    ax.text(0, 1.05, "Y210231 北村拓也", transform=ax.transAxes, fontproperties=goth, size=9)

    weekly_pref = weekly2[pref]  # 特定の都道府県のデータを抽出
    
    # Convert dates to pandas Timestamp objects and specify time zone (Japan Standard Time)
    dates = [pd.Timestamp(date, tz=pytz.timezone("Asia/Tokyo")) for date in fpmi["Week"]]
    
    ax.plot(dates, fac * np.array(fpmi[pref]), label=f"{pref}FPMI × {fac}", **{**opplot, "color": "orange"})
    ax.legend(prop=goth, loc="upper right", bbox_to_anchor=(1.0, 1.0))
    plt.show()
    fig.savefig(pngfile, dpi=600)

if __name__ == "__main__":
    epoch0, ndays = dt.datetime(2022, 1, 10), 82 * 7
    xlim, xticks = [epoch0, epoch0 + dt.timedelta(days=ndays)], [epoch0 + dt.timedelta(days=i) for i in range(7, ndays, 4 * 7)]
    pref, odays, fac, ylim, yticks = "大阪府", 3, 350, [0.2, 200], [1, 10, 100, 1000, 10000, 100000]
    ex06(pref, odays, fac, epoch0, ndays, xlim, xticks, ylim, yticks, "ex05.png", log=True)