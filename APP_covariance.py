print 'Covariance Calculation Using Yahoo Finance REST API'
#Knowledge to get all the raw data:
#https://ilmusaham.wordpress.com/tag/stock-yahoo-data/

import csv
import urllib2
import datetime
import math
import numpy as np

#This is the code for the data/time that the covariance will be caluclated over:
now = datetime.datetime.now()
month = str(int(now.month)-1) 
day = str(now.day) 
currentYear = str(now.year) 
lastYear = str(int(now.year)-1) 



ticker1 = raw_input('Enter the ticker one:')
url_pt1 = 'http://real-chart.finance.yahoo.com/table.csv?s=' 
url_pt3 = '&d='
url_pt5 = '&e='
url_pt7 = '&f='
url_pt9 = '&g=d&a='
url_pt11 = '&b='
url_pt13 = '&c='
url_pt15 = '&ignore=.csv'
#fullurl = url_pt1 + ticker1 + url_pt3 + month + url_pt5 + day + url_pt7 + currentYear + url_pt9 + month + url_pt11 + day + url_pt13 + lastYear + url_pt15 
fullurl = 'http://real-chart.finance.yahoo.com/table.csv?s=' + str(ticker1) + '&d=2&e=1&f=2016&g=d&a=2&b=1&c=2015&ignore.csv'
yahoo_finance_response = urllib2.urlopen(fullurl)
yahoo_finance_data = csv.reader(yahoo_finance_response)
ticker1_list_of_closing_prices = [] 
for row in yahoo_finance_data:
	ticker1_list_of_closing_prices.append(row[4])
ticker1_final_list_of_closing_prices = ticker1_list_of_closing_prices[1:]
ticker1_final_list_of_closing_prices = [float(x) for x in ticker1_final_list_of_closing_prices]
ticker1_average_price = np.mean(ticker1_final_list_of_closing_prices)
ticker1_average_price = float(ticker1_average_price)
ticker1_each_day_variance = map(lambda x: x - ticker1_average_price, ticker1_final_list_of_closing_prices)
ticker1_variance = [x**2 for x in ticker1_each_day_variance]
ticker1_variance = sum(ticker1_variance)/len(ticker1_variance)
ticker1_stdev = math.sqrt(ticker1_variance)
print ticker1_variance
print '\n'

ticker2 = raw_input('Enter the ticker two:')
url_pt1 = 'http://real-chart.finance.yahoo.com/table.csv?s=' 
url_pt3 = '&d='
url_pt5 = '&e='
url_pt7 = '&f='
url_pt9 = '&g=d&a='
url_pt11 = '&b='
url_pt13 = '&c='
url_pt15 = '&ignore=.csv'
#fullurl = url_pt1 + ticker2 + url_pt3 + month + url_pt5 + day + url_pt7 + currentYear + url_pt9 + month + url_pt11 + day + url_pt13 + lastYear + url_pt15 
fullurl = 'http://real-chart.finance.yahoo.com/table.csv?s=' + str(ticker2) + '&d=2&e=1&f=2016&g=d&a=2&b=1&c=2015&ignore.csv'
yahoo_finance_response = urllib2.urlopen(fullurl)
yahoo_finance_data = csv.reader(yahoo_finance_response)
ticker2_list_of_closing_prices = [] 
for row in yahoo_finance_data:
	ticker2_list_of_closing_prices.append(row[4])
ticker2_final_list_of_closing_prices = ticker2_list_of_closing_prices[1:]
ticker2_final_list_of_closing_prices = [float(x) for x in ticker2_final_list_of_closing_prices]
ticker2_average_price = np.mean(ticker2_final_list_of_closing_prices)
ticker2_average_price = float(ticker2_average_price)
ticker2_variance = [x**2 for x in ticker2_final_list_of_closing_prices]
ticker2_variance = ((sum(ticker2_variance))/ (len(ticker2_variance))) - (ticker2_average_price**2)
ticker2_stdev = math.sqrt(ticker2_variance)
print ticker2_variance
print '\n'

xy = [a*b for a,b in zip(ticker1_final_list_of_closing_prices, ticker2_final_list_of_closing_prices)]
summation_xy = (sum(xy))/(len(xy))
covariance = summation_xy - (ticker1_average_price * ticker2_average_price)
print covariance

correlation = (covariance/(ticker1_stdev*ticker2_stdev))
print correlation

