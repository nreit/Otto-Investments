print 'Percentile Calculation Using Yahoo Finance REST API'
#Knowledge to get all the raw data:
#https://ilmusaham.wordpress.com/tag/stock-yahoo-data/

import csv
import urllib2
import datetime
import math


ticker = raw_input('Enter the ticker you want to find projected ROR for:')

############################################################################################
#URL construction
baseurl = 'http://finance.yahoo.com/d/quotes.csv?s='
for_code = '&f='
price_code = 'l1'
high_code = 'k'
low_code = 'j'

#price
fullurl = baseurl + ticker + for_code + price_code 
yahoo_finance_response = urllib2.urlopen(fullurl)
yahoo_finance_data = csv.reader(yahoo_finance_response)
for item in yahoo_finance_data: 
	for price in item: 
		stock_price = float(price)

#52 week high
fullurl = baseurl + ticker + for_code + high_code 
yahoo_finance_response = urllib2.urlopen(fullurl)
yahoo_finance_data = csv.reader(yahoo_finance_response)
for item in yahoo_finance_data:
	for price in item: 
		year_high = float(price)

#52 week low 
fullurl = baseurl + ticker + for_code + low_code 
yahoo_finance_response = urllib2.urlopen(fullurl)
yahoo_finance_data = csv.reader(yahoo_finance_response)
for item in yahoo_finance_data: 
	for price in item: 
		year_low = float(price)

#percentile for the year
yearly_price_range = year_high - year_low
how_far_off_from_yearly_low = stock_price - year_low
current_price_percentile = int(100*(how_far_off_from_yearly_low/yearly_price_range))


print '\n'
print str(ticker) + ' is currently trading at $' + str(stock_price) + ". It's yearly high is $" + str(year_high) + ", and it's yearly low is $" + str(year_low)
print '\n'
print 'Within the past 52-weeks, ' + str(ticker) + ' is trading in the ' + str(current_price_percentile) + 'th percentile.'
print '\n'

