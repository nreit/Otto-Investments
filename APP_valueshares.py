print 'Values & Shares Calculation Using Yahoo Finance REST API'
#Knowledge to get all the raw data:
#https://ilmusaham.wordpress.com/tag/stock-yahoo-data/

import csv
import urllib2

ticker1 = raw_input('Enter a ticker: ')
percent1 = float(raw_input('Percentage: '))
baseurl = 'http://finance.yahoo.com/d/quotes.csv?s=' #part one of the Yahoo Finance URL
for_code = '&f='
price_code = 'l1'
fullurl = baseurl + ticker1 + for_code + price_code 
yahoo_finance_response = urllib2.urlopen(fullurl)
yahoo_finance_data = csv.reader(yahoo_finance_response)
for item in yahoo_finance_data: 
		for price in item: 
			stock_price1 = float(price)

investable = float(percent1 * 50000.0)
shares = int(investable / stock_price1)
print 'number of shares: '
print shares
value = shares * stock_price1
print 'value price: '
print value



ticker2 = raw_input('Enter a ticker: ')
percent2 = float(raw_input('Percentage: '))
baseurl = 'http://finance.yahoo.com/d/quotes.csv?s=' #part one of the Yahoo Finance URL
for_code = '&f='
price_code = 'l1'
fullurl = baseurl + ticker2 + for_code + price_code 
yahoo_finance_response = urllib2.urlopen(fullurl)
yahoo_finance_data = csv.reader(yahoo_finance_response)
for item in yahoo_finance_data: 
		for price in item: 
			stock_price2 = float(price)

investable = float(percent2 * 50000.0)
shares = int(investable / stock_price2)
print 'number of shares: '
print shares
value = shares * stock_price2
print 'value price: '
print value
