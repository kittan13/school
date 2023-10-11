# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import time

def readCSV(csvfile, parse_dates = ["Date"], rollingmean = True):
    df = pd.read_csv(csvfile, parse_dates = parse_dates)
    if rollingmean:
        for p in df.columns[1:]:df[p+' 7days'] = df[p].rolling (7).mean ()
    #print('>>> DataFrame <<<')
    #print(df.info())
    return{k:v.to_numpy() for k, v in df.items()}

if __name__== '__main__':
    filename = 'newly_confirmed_cases_daily.csv'
    positive = readCSV(filename, rollingmean=False)
    print('>>> Dict <<<')
    print('        日付  京都府  全国')
    for d, p, q in zip(positive['Date'], positive['Hokkaido'], positive['ALL']):
        print(f'\r{np.datetime_as_string(d, unit = "D")}{p:6}{q:6}', end ='')
        time.sleep(0.01)
    #print('\n', positive.keys())
