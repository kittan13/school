import covid
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib.font_manager import FontProperties

goth = FontProperties(fname="/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc")

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
    "color": "blue" # Typo fixed
}

opplot = {
    "linewidth": 1.2,
    "alpha": 0.7,
    "color": "blue"
}

def ex04(pref, epoch0, ndays, xlim, xticks, ylim, yticks, pngfile, log=False, rotation=28, pad=-2):
    filename = "newly_confirmed_cases_daily.csv"
    daily = covid.readCSV(filename)
    fig = plt.figure(figsize=(6,4))
    ax = plt.axes([0.09, 0.11, 0.89, 0.83])
    if log:
        ax.set_yscale("log")
    p = covid.prefecture[pref]  # Translated prefecture name to english
    ax.bar(daily["date"], daily[p], **opbar) # Used translated name
    ax.plot(daily["date"], daily[p], **opplot) # Used translated name
    xticks = [epoch0+dt.timedelta(days=i) for i in range(7, ndays, 4*7)] # Used timedelta instead of datetime
    covid.drawFrame(pref + " 日別陽性者数", optitle, ax, xlim, xticks, ylim, yticks, rotation=rotation, pad=pad)
    fig.savefig(pngfile)
