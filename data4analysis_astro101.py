from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib import const
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# date = Datetime('1991/01/26', '23:30', '+08:00')
# pos = GeoPos('30n42', '111e17')
# chart = Chart(date, pos)
# sun = chart.get(const.SUN)
# print(sun)

start_time = pd.to_datetime('1949/10/01')
end_time = pd.to_datetime('2030/01/01')
days = (end_time - start_time).days
pos = GeoPos('30n42', '111e17') # Yichang
from pandas.tseries.offsets import Day

time_collection = []
saturn_collection = []
for timeslice in range(days):
    if timeslice % 7 ==0:
        current_day = start_time+Day(timeslice)
        date_string = current_day.date().strftime('%Y/%m/%d')
        date = Datetime(date_string, '00:00', '+08:00')
        chart = Chart(date, pos)
        if const.CAPRICORN ==chart.objects.content['Saturn'].sign     \
            or const.AQUARIUS ==chart.objects.content['Saturn'].sign    \
            or const.LIBRA==chart.objects.content['Saturn'].sign:
            saturn_status = 5
        else:
            saturn_status = 0
        time_collection.append(date_string)
        saturn_collection.append(saturn_status)
        print (date_string, chart.objects.content['Saturn'].sign)
saturn_collection = np.array(saturn_collection)
x_label = np.arange(len(saturn_collection)) # X label use time need test
print('eof')

