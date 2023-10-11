# -*- coding: utf-8 -*-

import covid
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib.font_manager import FontProperties
goth = FontProperties(fname="C:/Windows/Fonts/msgothic.ttc")

# Configure options
opbar = {
    "align":"center",
    "width":1.0,
    "alpha":0.3,
    "color":"blue"
}

opplot = {
    "linewidth":1.2,
    "alpha":0.7
}

# Drawing function
def draw_comparison(prefectures, epoch0, ndays, xlim, xticks, ylim, yticks, 
         pngfile, log=False, rotation= 28, pad = -2):
    filename = "newly_confirmed_cases_daily.csv"
    daily = covid.readCSV(filename)
    fig= plt.figure(figsize=(12,8.5))
    ax = plt.axes([0.09, 0.11, 0.89, 0.83])
    if log :
        ax.set_yscale("log")

    for pref in prefectures:
        p = covid.prefecture[pref]
        population = covid.population[pref]
        daily[p] = daily[p] *(1000000 /population)
        ax.plot(daily['Date'],daily[p + ' 7days'], label = pref + ' (10万人あたりの日別陽性者数)', **opplot)


    ax.set_xlim(xlim)  # set x limit
    ax.set_xticks(xticks)  # set x ticks
    ax.set_ylim(ylim)  # set y limit
    ax.set_yticks(yticks)  # set y ticks
    
    ax.set_title('各都市における人口10万人あたりの日別陽性者数', fontproperties=goth, y=1.02)
    ax.text(0, 1.05, "Y210231 北村拓也", transform=ax.transAxes, fontproperties=goth, size=9)  
    ax.legend(prop=goth, loc="upper left", bbox_to_anchor=(0.0,1.0))
    
    plt.show()
    fig.savefig(pngfile,dpi=600)

# Set parameters and call function
if __name__ == "__main__":
    epoch0, ndays = dt.datetime(2022, 1, 10), 90*7
    xlim, xticks = [epoch0,epoch0+dt.timedelta(days=ndays)],[epoch0+dt.timedelta(days=i) for i in range(7, ndays, 8*7)]
    prefs = ['京都府', '大阪府', '東京都']
    log, ylim, yticks = True, [1000,20000], [10,100,1000,10000,100000]
    draw_comparison(prefs, epoch0, ndays, xlim, xticks, ylim, yticks, "ex04log.png", log=log)
