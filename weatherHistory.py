import numpy as np
import pandas as pd
df=pd.read_csv('./data/weatherHistory.csv')
df.columns#检查特征
df.count#检查空白值
pd.set_option('display.max_columns', None)#行完整显示
df0.head(10)#显示前十行
'''
                  Formatted Date        Summary Precip Type  Temperature (C)  \
0  2006-04-01 00:00:00.000 +0200  Partly Cloudy        rain         9.472222   
1  2006-04-01 01:00:00.000 +0200  Partly Cloudy        rain         9.355556   
2  2006-04-01 02:00:00.000 +0200  Mostly Cloudy        rain         9.377778   
3  2006-04-01 03:00:00.000 +0200  Partly Cloudy        rain         8.288889   
4  2006-04-01 04:00:00.000 +0200  Mostly Cloudy        rain         8.755556   
5  2006-04-01 05:00:00.000 +0200  Partly Cloudy        rain         9.222222   
6  2006-04-01 06:00:00.000 +0200  Partly Cloudy        rain         7.733333   
7  2006-04-01 07:00:00.000 +0200  Partly Cloudy        rain         8.772222   
8  2006-04-01 08:00:00.000 +0200  Partly Cloudy        rain        10.822222   
9  2006-04-01 09:00:00.000 +0200  Partly Cloudy        rain        13.772222   
   Apparent Temperature (C)  Humidity  Wind Speed (km/h)  \
0                  7.388889      0.89            14.1197   
1                  7.227778      0.86            14.2646   
2                  9.377778      0.89             3.9284   
3                  5.944444      0.83            14.1036   
4                  6.977778      0.83            11.0446   
5                  7.111111      0.85            13.9587   
6                  5.522222      0.95            12.3648   
7                  6.527778      0.89            14.1519   
8                 10.822222      0.82            11.3183   
9                 13.772222      0.72            12.5258   
   Wind Bearing (degrees)  Visibility (km)  Pressure (millibars)  
0                   251.0          15.8263               1015.13  
1                   259.0          15.8263               1015.63  
2                   204.0          14.9569               1015.94  
3                   269.0          15.8263               1016.41  
4                   259.0          15.8263               1016.51  
5                   258.0          14.9569               1016.66  
6                   259.0           9.9820               1016.72  
7                   260.0           9.9820               1016.84  
8                   259.0           9.9820               1017.37  
9                   279.0           9.9820               1017.22  
'''
df0=df.drop(columns=['Daily Summary','Loud Cover'])#删除不必要的特征
df0.columns.value_counts()
'''
Visibility (km)             1
Apparent Temperature (C)    1
Temperature (C)             1
Precip Type                 1
Summary                     1
Humidity                    1
Formatted Date              1
Wind Speed (km/h)           1
Pressure (millibars)        1
Wind Bearing (degrees)      1
'''
df0['Precip Type'].value_counts()
'''
rain    85224
snow    10712
'''
df0['Summary'].value_counts()
'''
Partly Cloudy                          31733
Mostly Cloudy                          28094
Overcast                               16597
Clear                                  10890
Foggy                                   7148
Breezy and Overcast                      528
Breezy and Mostly Cloudy                 516
Breezy and Partly Cloudy                 386
Dry and Partly Cloudy                     86
Windy and Partly Cloudy                   67
Light Rain                                63
Breezy                                    54
Windy and Overcast                        45
Humid and Mostly Cloudy                   40
'''
