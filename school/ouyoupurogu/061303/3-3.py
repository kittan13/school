# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import time

def readCSV(csvfile, parse_dates = ["Date"], rollingmean = True):
    df = pd.read_csv(csvfile, parse_dates = parse_dates)
    if rollingmean:
        df["Tokyo 7days"] =df["Tokyo"].rolling (7).mean ()
    #print('>>> DataFrame <<<')
    #print(df.info())
    return{k:v.to_numpy() for k, v in df.items()}


if __name__== '__main__':
    filename = 'newly_confirmed_cases_daily.csv'
    positive = readCSV(filename, rollingmean=True)
    print('>>> 東京都の毎日の新規陽性者数と7日間移動平均 <<<')
    print('{:<10}{:<10}{:<20}'.format("日付", "東京都", "東京都7日間平均移動"))
    for d, p, q in zip(positive['Date'], positive['Tokyo'], positive['Tokyo 7days']):
        print(f'\r{np.datetime_as_string(d, unit = "D"):15}{p:8}{q:20.2f}', end ='')
        time.sleep(0.01)
    #print('\n', positive.keys())

