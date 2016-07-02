print 'Market Value Calculation Using Yahoo Finance REST API'
#Knowledge to get all the raw data:
#https://ilmusaham.wordpress.com/tag/stock-yahoo-data/

import csv
import urllib2

ticker = raw_input('Enter a ticker: ')
shares = float(raw_input('How many shares do you own? '))


############################################################################################
#URL construction
baseurl = 'http://finance.yahoo.com/d/quotes.csv?s=' #part one of the Yahoo Finance URL
for_code = '&f='
price_code = 'l1'

#get price
fullurl = baseurl + ticker + for_code + price_code 
yahoo_finance_response = urllib2.urlopen(fullurl)
yahoo_finance_data = csv.reader(yahoo_finance_response)
for item in yahoo_finance_data: 
		for price in item: 
			stock_price = float(price)

market_value = shares*stock_price

print 'Market Value: '
print market_value
