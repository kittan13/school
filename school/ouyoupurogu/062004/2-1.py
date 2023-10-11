# -*- coding: utf-8 -*-

import covid
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib.font_manager import FontProperties
goth = FontProperties(fname="C:/Windows/Fonts/msgothic.ttc")

optitle = {
    "xycoords":"data",
    "textcoords":"offset points",
    "fontproperties":goth,
    "size":12
}

opbar = {
    "align":"center",
    "width":1.0,
    "alpha":0.3,
    "color":"blue"
}

opplot = {
    "linewidth":1.2,
    "alpha":0.7,
    "color":"blue"
}

def ex04(pref, epoch0, ndays, xlim, xticks, ylim, yticks, 
         pngfile, log=False, rotation= 28, pad = -2):
    filename = "newly_confirmed_cases_daily.csv"
    daily = covid.readCSV(filename)
    fig= plt.figure(figsize=(6,4))
    ax = plt.axes([0.09, 0.11, 0.89, 0.83])
    if log :
        ax.set_yscale("log")
    p = covid.prefecture[pref]
    
    # 10万人あたりの日別陽性者数の計算
    population = covid.population[pref]
    daily_per_100k = daily[p] * (100000 / population)

    covid.drawFrame(pref + '  10万人あたりの日別陽性者数',
                    optitle, ax, xlim, xticks, ylim, yticks,rotation=rotation, pad=pad)
    ax.plot(daily['Date'], daily_per_100k, label = '10万人あたりの日別陽性者数', **opplot)

    #ax.plot(daily['Date'],daily[p + ' 7days'], label = '7日間移動平均', **opplot)
    ax.legend(prop=goth, loc="upper left", bbox_to_anchor=(0.0,1.0))
    plt.show()
    fig.savefig(pngfile,dpi=600)

if __name__ == "__main__":
    epoch0, ndays = dt.datetime(2022, 1, 10), 82*7
    xlim, xticks = [epoch0,epoch0+dt.timedelta(days=ndays)],[epoch0+dt.timedelta(days=i) for i in range(7, ndays, 4*7)]
    #pref, log , ylim, yticks = '京都府', False, [0,7000], range(0, 7000, 500)
    #ex04(pref, epoch0, ndays, xlim, xticks, ylim, yticks, "ex04.png", log=log)
    pref, log, ylim, yticks = '滋賀県', True, [0,1000], [1, 10, 100, 1000]
    ex04(pref, epoch0, ndays, xlim, xticks, ylim, yticks, "ex04log.png", log=log)
