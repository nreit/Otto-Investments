print 'Return Calculation Using Yahoo Finance REST API'
#Knowledge to get all the raw data:
#https://ilmusaham.wordpress.com/tag/stock-yahoo-data/

import csv
import urllib2
import datetime
import math


ticker = raw_input('Enter the ticker you want to find projected ROR for:')

############################################################################################
#URL construction
baseurl = 'http://finance.yahoo.com/d/quotes.csv?s=' #part one of the Yahoo Finance URL
for_code = '&f='
price_code = 'l1'
target_code = 't8'
dividend_code = 'd'

#get price
fullurl = baseurl + ticker + for_code + price_code 
yahoo_finance_response = urllib2.urlopen(fullurl)
yahoo_finance_data = csv.reader(yahoo_finance_response)
for item in yahoo_finance_data: 
		for price in item: 
			stock_price = float(price)

#get price target
fullurl = baseurl + ticker + for_code + target_code
yahoo_finance_response = urllib2.urlopen(fullurl)
yahoo_finance_data = csv.reader(yahoo_finance_response)
for item in yahoo_finance_data: 
	for price in item: 
		price_target = float(price)

#get dividend (if applicable)
fullurl = baseurl + ticker + for_code + dividend_code
yahoo_finance_response = urllib2.urlopen(fullurl)
yahoo_finance_data = csv.reader(yahoo_finance_response)
for item in yahoo_finance_data: 
	try:
		for dividend in item:
			dividend = float(dividend)
	except:
		dividend = float(0)

################################################################################################
growth = 100*((price_target + dividend - stock_price)/stock_price)
print '\n'
print 'The projected growth for ' + str(ticker) + ' is ' + str(growth) + '%'
print '\n'

