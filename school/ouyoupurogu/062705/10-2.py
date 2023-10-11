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
    "Week": [dt.date(2023,5, 8), dt.date(2023, 5, 15), dt.date(2023, 5, 22), dt.date(2023, 5, 29), dt.date(2023, 6, 5), dt.date(2023, 6, 12), dt.date(2023, 6, 19), dt.date(2023, 6, 26)],
    "東京都": [2.40, 3.54, 3.96, 5.29, 5.99, 5.85, 6.22, 6.85],
    "滋賀県": [1.82, 2.07, 1.77, 2.47],
    "京都府":[2.03, 2.96, 2.60, 3.51, 4.13, 4.67, 4.92, 6.02],
    "全国": [2.63, 3.55, 3.63, 4.55],
    "大阪府":[1.79, 2.37, 2.75, 3.33, 4.33, 4.55, 5.16, 5.93]
}

def compare_prefectures(pref_list, odays, fac, epoch0, ndays, xlim, xticks, ylim, yticks, pngfile, log=False, rotation=28, pad=-2):
    filename = "newly_confirmed_cases_daily.csv"
    daily = covid.readCSV(filename)
    weekly1, weekly2 = covid.readXLSXfp()

    fig, ax = plt.subplots(figsize=(10, 6))
    if log:
        ax.set_yscale("log")

    for pref in pref_list:
        p = covid.prefecture[pref]
        weekly_pref = weekly2[pref]

        # Modify the label based on the comparison factor 'fac'
        label = f"{pref}定点あたりの報告数 × {fac}"

        # Plot the data for the prefecture
        ax.bar([str(d[0]) for d in weekly1["Week"]], np.ravel(list(weekly_pref))*fac, label=label, alpha=0.5)

        # Calculate and plot 7-day moving average
        daily[p + "7days"] = pd.Series(daily[p]).rolling(window=7, min_periods=1).mean()
        ax.plot(daily["Date"] - dt.timedelta(days=odays), daily[p + "7days"], label=f"陽性者数7日間移動平均 (-{odays}日)", linewidth=1.5)

    ax.set_xlim(xlim)
    ax.set_xticks(xticks)
    ax.set_ylim(ylim)
    ax.set_yticks(yticks)
    ax.set_xlabel("Date")
    ax.set_ylabel("Cases")
    ax.legend(prop=goth, loc="upper left", bbox_to_anchor=(1, 1))

    plt.title("大阪府・京都府・東京都 定点あたりの報告数の比較", fontproperties=goth, size=14)
    plt.xticks(rotation=rotation)
    plt.grid(True, which="both", axis="both", linestyle="--", alpha=0.7)
    plt.tight_layout()

    plt.savefig(pngfile, dpi=300)
    plt.show()

if __name__ == "__main__":
    epoch0, ndays = dt.datetime(2022, 1, 10), 82 * 7
    xlim = [epoch0, epoch0 + dt.timedelta(days=ndays)]
    xticks = [epoch0 + dt.timedelta(days=i) for i in range(7, ndays, 4 * 7)]

    # Add your preferred values for 'fac' for each prefecture
    pref_list = ["大阪府", "京都府", "東京都"]
    fac_values = [350, 500, 800]  # Modify these values as per your preference

    for i, pref in enumerate(pref_list):
        fac = fac_values[i]
        compare_prefectures([pref], odays=3, fac=fac, epoch0=epoch0, ndays=ndays, xlim=xlim, xticks=xticks, ylim=[1, 10000], yticks=[1, 10, 100, 1000, 10000], pngfile=f"ex06_{pref}.png", log=True)
