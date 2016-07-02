print 'Volatility Calculation Using Yahoo Finance REST API'
#Knowledge to get all the raw data:
#https://ilmusaham.wordpress.com/tag/stock-yahoo-data/

import csv
import urllib2
import datetime
import math
import numpy as np

ticker = raw_input('Enter the ticker you want to find volatility for:')
url_pt1 = 'http://real-chart.finance.yahoo.com/table.csv?s=' 
url_pt3 = '&d='
url_pt5 = '&e='
url_pt7 = '&f='
url_pt9 = '&g=d&a='
url_pt11 = '&b='
url_pt13 = '&c='
url_pt15 = '&ignore=.csv'
now = datetime.datetime.now()
month = str(int(now.month)-1) 
day = str(now.day) 
currentYear = str(now.year) 
lastYear = str(int(now.year)-1) 
fullurl = url_pt1 + ticker + url_pt3 + month + url_pt5 + day + url_pt7 + currentYear + url_pt9 + month + url_pt11 + day + url_pt13 + lastYear + url_pt15 
yahoo_finance_response = urllib2.urlopen(fullurl)
yahoo_finance_data = csv.reader(yahoo_finance_response)
list_of_closing_prices = [] 
for row in yahoo_finance_data:
	list_of_closing_prices.append(row[4])
print list_of_closing_prices
final_list_of_closing_prices = list_of_closing_prices[1:] 
#average_closing_price = float((reduce(lambda x, y: float(x)+float(y), final_list_of_closing_prices)) / float(len(final_list_of_closing_prices))) 
final_list_of_closing_prices = [float(x) for x in final_list_of_closing_prices]
average_closing_price = np.mean(final_list_of_closing_prices)
print average_closing_price
list_of_each_day_deviation = []
for price in final_list_of_closing_prices: 
	list_of_each_day_deviation.append((float(price)) - average_closing_price)
list_of_each_day_deviationSquared = [] 
for deviation in list_of_each_day_deviation: 
	list_of_each_day_deviationSquared.append((float(deviation))**2)
average_deviation_per_day_squared = float((reduce(lambda x, y: float(x)+float(y), list_of_each_day_deviationSquared)) / float(len(list_of_each_day_deviationSquared))) 
print 'average_deviation_per_day_squared'
print average_deviation_per_day_squared

average_deviation_per_day = math.sqrt(average_deviation_per_day_squared)
print 'deviation'
print average_deviation_per_day
print type(average_deviation_per_day_squared)
volatility_percentage = 100.0*(float(average_deviation_per_day) / average_closing_price)
print '\n'
print 'The volatility percentage for ' + str(ticker) + ' is ' + str(volatility_percentage) + ' %'
print '\n'