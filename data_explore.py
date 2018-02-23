#coding:utf-8
import pandas as pd
file = open('severeinjury.csv','rb')
import codecs
with codecs.open('severeinjury.csv', "r",encoding='utf-8', errors='ignore') as fdata:
    datafile = pd.read_csv(fdata)
# test mars
# list all mars properties, whether in Scopio or in Aries, or in Capricorn. Else in Their opposing constellation
# list all major starts that has a aspect with mars, with exception of moon, to test corellation with body part

# run a Saturn Jupyter graph for overall uckiness of generations
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib import const

latitude,longitude = datafile['Latitude'],datafile['Longitude']
birthtime =  datafile['EventDate']
birthtime = pd.to_datetime(birthtime)

pos = GeoPos('30n42', '111e17')
for tmp in birthtime: # Pandas wrapped numpy datetime64 to timestamp object, which is far better to use
    date_old = tmp.date()
    date_string = date_old.strftime('%Y/%d/%m')
    date = Datetime(date_string, '00:00', '+08:00')
    chart = Chart(date, pos)
    chart.objects.content['Saturn'].sign

chart = Chart(birthtime, pos)




# aa = pd.read_csv(file,error_bad_lines=False)
# df = pd.read_csv(file,sep=',', header = None, skiprows=1000, chunksize=1000)
# aa = pd.read_csv('severeinjury.csv',encoding='cp936')
print('eof')