# -*- coding: utf-8 -*-

import covid
import matplotlib.pyplot as plt 
import datetime as dt
import numpy as np
from matplotlib.font_manager import FontProperties
goth=FontProperties (fname='C:/Windows/Fonts/msgothic.ttc')

optitle={'xycoords':'data','textcoords':'offset points','fontproperties':goth,'size':10}
opbar={'align':'center','width':1.0,'alpha':0.5,'color':'blue'}
opplot={'linewidth':1.5,'alpha':0.7,'color':'blue'}
fpmi = {
    'Week': [dt.date (2023, 5, 8), dt.date (2023, 5,15), dt.date (2023, 5,22), 
             dt.date (2023, 5,29), dt.date(2023, 6, 5), dt.date(2023,6,12), dt.date(2023,6,19), ],
    #'東京都' : [2.40, 3.53 , 3.96 , 5.29 , 3.56 ,3.44, 2.87,1.44],
    '奈良県':[2.55, 3.33, 3.29, 4.51, 4.64, 5.40, 5.58]}
    #'鳥取県':[2.69, 3.24, 2.86, 4.24,3.56 ,3.44, 2.87,5.66], 
        #'全国': [2.63, 3.55, 3.63, 4.557,3.56 ,3.44, 2.87,1.26]
def ex06 (pref, odays, fac, epochO, ndays, xlim, xticks, ylim, yticks, pngfile, log=False, rotation=28, pad=-2):
    filename = 'newly_confirmed_cases_daily.csv'
    daily = covid.readCSV(filename)
    weekly1,weekly2 = covid.readXLSXfp ()
    fig = plt.figure (figsize= (6,4))
    ax = plt.axes ([0.09,0.11,0.89,0.83])
    xlim, xticks = [epochO, epochO+dt.timedelta (days=ndays)], \
        [epochO+dt. timedelta (days=i) for i in range (7, ndays, 4*7)] 
    if log: ax.set_yscale ('log')
    p= covid.prefecture [pref]
    covid.drawFrame (pref + '　　定点当たり方向数の日別陽性者数への換算　　Y210251 大保心',
                     optitle, ax, xlim, xticks, ylim, yticks, rotation=rotation, pad=pad) 
    ax.bar ([d[0] for d in weekly2['Week']], fac*weekly2[pref],
            label=f'定点あたり報告数'r'$\times$'f' {fac}',**{**opbar,'width':7.0}) 
    ax.bar (fpmi ['Week'], fac*np.array (fpmi[pref]),
            **{**opbar, 'width':7.0, 'color': 'orange'})
    ax.plot (daily['Date']-np.timedelta64 (odays, 'D'),daily[p+' 7days'],
             label='陽性者数7日間移動平均('r'$-$'f'{odays}日)', **opplot)
    ax. legend (prop=goth, loc='upper right', bbox_to_anchor=(1.0, 1.0)) 
    plt.show ()
    fig.savefig (pngfile, dpi=600)

if __name__== '__main__':
    epochO, ndays= dt.datetime (2022, 1, 10), 82*7
    xlim, xticks = [epochO, epochO+dt.timedelta (days=ndays)], \
        [epochO+dt.timedelta (days=i) for i in range (7, ndays, 4*7)] 
    pref, odays, fac, ylim, yticks = '奈良県', 6,110,[8, 8000], [10, 100, 1000]
    ex06 (pref, odays, fac, epochO, ndays, xlim, xticks, ylim, yticks, 
          'ex06.png', log=True)