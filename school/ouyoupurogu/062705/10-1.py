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

def ex06(pref_list, odays, fac, epoch0, ndays, xlim, xticks, ylim, yticks, pngfile, log=False, rotation=28, pad=-2):
    filename = "newly_confirmed_cases_daily.csv"
    daily = covid.readCSV(filename)
    weekly1, weekly2 = covid.readXLSXfp()
    fig = plt.figure(figsize=(6, 5))
    ax = plt.axes([0.09, 0.11, 0.89, 0.83])
    xlim, xticks = [epoch0, epoch0 + dt.timedelta(days=ndays)], [epoch0 + dt.timedelta(days=i) for i in range(7, ndays, 4 * 7)]
    ax.set_yscale("log")

    for pref in pref_list:
        p = covid.prefecture[pref]
        weekly_pref = weekly2[pref]

        # Modify the label based on the comparison factor 'fac'
        label = f"{pref}定点あたりの報告数 × {fac}"

        # Plot the data for the prefecture
        ax.bar([str(d[0]) for d in weekly1["Week"]], np.ravel(list(weekly_pref))*fac, label=label, alpha=0.5)

        # Convert daily data to DataFrame
        daily_df = pd.DataFrame(daily)

        # Calculate and plot 7-day moving average
        daily_df[p + "7days"] = daily_df[p].rolling(window=7, min_periods=1).mean()
        
        # Calculate the date 'odays' days before the end date
        end_date = daily_df["Date"].iloc[-1]
        start_date = end_date - pd.Timedelta(days=odays)
        
        ax.plot(daily_df[(daily_df["Date"] >= start_date) & (daily_df["Date"] <= end_date)]["Date"], 
                daily_df[(daily_df["Date"] >= start_date) & (daily_df["Date"] <= end_date)][p + "7days"], 
                label=f"陽性者数7日間移動平均 (-{odays}日)", linewidth=1.5)

    ax.bar([str(d[0]) for d in weekly1["Week"]], np.ravel(list(weekly_pref))*fac, label=f"{pref}定点あたりの報告数 × {fac}", **{**opbar, "width": 7.0})
    ax.bar(fpmi["Week"], fac * np.array(fpmi[pref]), **{**opbar, "width": 7.0, "color": "orange"})
    daily[p + "7days"] = pd.Series(daily[p]).rolling(window=7, min_periods=1).mean()  # 7日間移動平均を計算
    #ax.plot(daily["Date"] - np.timedelta64(odays, "D"), daily[p + "7days"], label=f"陽性者数7日間移動平均 (-{odays}日)", **opplot)
    ax.legend(prop=goth, loc="upper right", bbox_to_anchor=(1.0, 1.0))
    plt.show()
    fig.savefig(pngfile, dpi=600)

if __name__ == "__main__":
    epoch0, ndays = dt.datetime(2022, 1, 10), 82 * 7
    xlim, xticks = [epoch0, epoch0 + dt.timedelta(days=ndays)], [epoch0 + dt.timedelta(days=i) for i in range(7, ndays, 4 * 7)]
    pref_list, odays, fac, ylim, yticks = ["大阪府", "京都府", "東京都"], 3, 350, [0.2, 200], [1, 10, 100, 1000, 10000, 100000]
    ex06(pref_list, odays, fac, epoch0, ndays, xlim, xticks, ylim, yticks, "ex05.png", log=True)
