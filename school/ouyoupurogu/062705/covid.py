# -*- coding: utf-8 -*-
import matplotlib.dates as mdates
import datetime as dt
import pandas as pd

prefecture = {
    '全国':  'ALL',         '北海道':'Hokkaido',    '青森県':'Aomori',
    '岩手県':'Iwate',       '宮城県':'Miyagi',      '秋田県':'Akita',
    '山形県':'Yamagata',    '福島県':'Fukushima',   '茨城県':'Ibaraki',
    '栃木県':'Tochigi',     '群馬県':'Gunma',       '埼玉県':'Saitama',
    '千葉県':'Chiba',       '東京都':'Tokyo',     '神奈川県':'Kanagawa',
    '新潟県':'Niigata',     '富山県':'Toyama',      '石川県':'Ishikawa',
    '福井県':'Fukui',       '山梨県':'Yamanashi',   '長野県':'Nagano',
    '岐阜県':'Gifu',        '静岡県':'Shizuoka',    '愛知県':'Aichi',
    '三重県':'Mie',         '滋賀県':'Shiga',       '京都府':'Kyoto',
    '大阪府':'Osaka',       '兵庫県':'Hyogo',       '奈良県':'Nara',
  '和歌山県':'Wakayama',    '鳥取県':'Tottori',     '島根県':'Shimane',
    '岡山県':'Okayama',     '広島県':'Hiroshima',   '山口県':'Yamaguchi',
    '徳島県':'Tokushima',   '香川県':'Kagawa',      '愛媛県':'Ehime',
    '高知県':'Kochi',       '福岡県':'Fukuoka',     '佐賀県':'Saga',
    '長崎県':'Nagasaki',    '熊本県':'Kumamoto',    '大分県':'Oita',
    '宮崎県':'Miyazaki',  '鹿児島県':'Kagoshima',   '沖縄県':'Okinawa'}

population = {
# 2022-10-01現在推計人口
# https://www.stat.go.jp/data/jinsui/2022np/index.htm
  '全国':  124947000,
  '東京都': 14038000, '神奈川県': 9232000, '大阪府': 8782000, '愛知県': 7495000,
  '埼玉県': 7337000, '千葉県': 6266000, '兵庫県': 5402000, '北海道': 5140000,
  '福岡県': 5116000, '静岡県': 3582000, '茨城県': 2840000, '広島県': 2760000,
  '京都府': 2550000, '宮城県': 2280000, '新潟県': 2153000, '長野県': 2020000,
  '岐阜県': 1946000, '群馬県': 1913000, '栃木県': 1909000, '岡山県': 1862000,
  '福島県': 1790000, '三重県': 1742000, '熊本県': 1718000, '鹿児島県': 1563000,
  '沖縄県': 1468000, '滋賀県': 1409000, '山口県': 1313000, '奈良県': 1306000,
  '愛媛県': 1306000, '長崎県': 1283000, '青森県': 1204000, '岩手県': 1181000,
  '石川県': 1118000, '大分県': 1107000, '宮崎県': 1052000, '山形県': 1041000,
  '富山県': 1017000, '香川県':  934000, '秋田県':  930000, '和歌山県':903000,
  '山梨県':  802000, '佐賀県':  801000, '福井県':  753000, '徳島県':  704000,
  '高知県':  676000, '島根県':  658000, '鳥取県':  544000}

def readCSV (csvfile, parse_dates=['Date'], encoding='utf-8', rollingmean=True):
  df = pd.read_csv (csvfile, parse_dates=parse_dates, encoding=encoding)
  df.rename (columns={'合計': '全国'}, inplace=True)
  df.sort_values (df.columns[0], inplace=True)
  if rollingmean:
    for p in df.columns[1:]: df[p+' 7days'] = df[p].rolling (7).mean ()
  return {k: v.to_numpy () for k, v in df.items ()}

def readCSV2 (csvfile):
  df1 = pd.read_csv (csvfile, header=None, nrows=2)
  df1.rename (columns={0: df1.iat[1, 0]}, inplace=True)
  for j in df1.columns[1:]:
    if type (df1.iat[0, j]) is str: prefix = df1.iat[0, j]
    df1.rename (columns={j: prefix+'_'+df1.iat[1, j]}, inplace=True)
  df = pd.read_csv (csvfile, header=None, skiprows=2, na_values='*')
  df.sort_values (df.columns[0], inplace=True)
  for i, d in enumerate (df[0]):
    df.iat[i, 0] = pd.to_datetime (d.split ('~'), format='%Y/%m/%d')
  for j, c in enumerate (df1.columns): df.rename (columns={j: c}, inplace=True)
  return {k: v.to_numpy () for k, v in df.items ()}

def readXLSXfp ():
  xlsxfile  = '001108957.xlsx'
  d = []
  for header in [3, 64]:
    df = pd.read_excel (xlsxfile, skiprows=[0], header=header, nrows=39,
      index_col=[0, 1])
    df.rename (columns={'合計': '全国'}, inplace=True)
    d.append ({**{'Week': list (df.index)},
      **{k: v.to_numpy () for k, v in df.items ()}})
  return d

def drawFrame (title, optitle, ax, xlim, xticks, ylim, yticks,
  rotation=28, pad=-2):
  ax.annotate (title, xy=(xlim[0], ylim[1]), xytext=(10, 4), **optitle)
  ax.tick_params (axis='y', which='both', direction='in', right=True)
  ax.set_xlim (xlim); ax.set_xticks (xticks)
  ax.set_ylim (ylim); ax.set_yticks (yticks)
  ax.minorticks_on ()
  ax.xaxis.set_tick_params (rotation=rotation, labelsize=9, pad=pad)
  ax.xaxis.set_major_formatter (mdates.DateFormatter ('%m/%d'))
  for y in range (xlim[0].year, xlim[1].year+1): ax.annotate (f'{y}年',
    xy=(dt.date (y, 1, 10), ylim[0]), xytext=(0, -29), **{**optitle, 'size':9})

