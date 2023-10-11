import pandas as pd
import numpy as np
import time

def readCSV(csvfile, parse_dates=["Date"], rollingmean=True):
    df = pd.read_csv(csvfile, parse_dates=parse_dates)
    if rollingmean:
        df["Tokyo 7days"] = df["Tokyo"].rolling(7).mean()
    print('>>> DataFrame <<<')
    print(df.info())
    return {k: v.to_numpy() for k, v in df.items()}

def print_tokyo_cases(csvfile):
    data = readCSV(csvfile, rollingmean=True)
    print(">>> 東京都の毎日の新規陽性者数と7日間移動平均 <<<")
    print("{:<10} {:<10} {:<10}".format("日付", "東京都", "東京都 7日間移動平均"))

    for d, p, q in zip(data['Date'], data['Tokyo'], data['Tokyo 7days']):
        print("{:<10} {:<10} {:<10.2f}".format(d, p, q))
        time.sleep(0.01)

if __name__ == '__main__':
    filename = 'newly_confirmed_cases_daily.csv'
    print_tokyo_cases(filename)
