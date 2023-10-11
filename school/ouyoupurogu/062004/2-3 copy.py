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

def ex04(pref, pref2, pref3, epoch0, ndays, xlim, xticks, ylim, yticks, 
         pngfile, log=False, rotation= 28, pad = -2):
    filename = "newly_confirmed_cases_daily.csv"
    daily = covid.readCSV(filename)
    fig= plt.figure(figsize=(6,4))
    ax = plt.axes([0.09, 0.11, 0.89, 0.83])
    if log :
        ax.set_yscale("log")
    p = covid.prefecture[pref]
    p2 = covid.prefecture[pref2]
    p3 = covid.prefecture[pref3]
    population = covid.population[pref]
    population2 = covid.population[pref2]
    population3 = covid.population[pref3]
    daily[p] = daily[p] *(100000 /population)
    daily[p2] = daily[p2] *(100000 /population2)
    daily[p3] = daily[p3] *(100000 /population3)
    
    covid.drawFrame(pref + ', ' + pref2 + ', ' + pref3 + ' 10万人あたりの日別陽性者数',
                    optitle, ax, xlim, xticks, ylim, yticks,rotation=rotation, pad=pad)
    
    ax.plot(daily['Date'],daily[p + ' 7days'], label = pref + '', color='blue')
    ax.plot(daily['Date'],daily[p2 + ' 7days'], label = pref2 + '', color='green')
    ax.plot(daily['Date'],daily[p3 + ' 7days'], label = pref3 + '', color='red')
    ax.legend(prop=goth, loc="upper left", bbox_to_anchor=(0.0,1.0))
    plt.show()
    fig.savefig(pngfile,dpi=600)


if __name__ == "__main__":
    epoch0, ndays = dt.datetime(2022, 1, 10), 82*7
    xlim, xticks = [epoch0,epoch0+dt.timedelta(days=ndays)],[epoch0+dt.timedelta(days=i) for i in range(7, ndays, 4*7)]
    pref, pref2, pref3, log, ylim, yticks = '京都府', '滋賀県', '岡山県', True, [10,12000], [10,100,1000]
    ex04(pref, pref2, pref3, epoch0, ndays, xlim, xticks, ylim, yticks, "ex04log.png", log=log)


