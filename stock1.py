import tushare
import pandas as pd
info = tushare.get_hist_data('600848')
yesterday_info = info.loc['2018-01-24']
print('eof')
