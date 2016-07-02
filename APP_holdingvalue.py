print 'Value of Purchase Calculation Using Yahoo Finance REST API'
#Knowledge to get all the raw data:
#https://ilmusaham.wordpress.com/tag/stock-yahoo-data/

import csv
import urllib2


ticker = raw_input('Enter the ticker you want to find projected ROR for:')

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

dollar_to_invest = float(raw_input('How much money do you have to invest? '))

shares = int(dollar_to_invest / stock_price)

print 'Number of shares to buy:'
print shares

value = (float(shares))*stock_price

print 'Value of buy:'
print value
