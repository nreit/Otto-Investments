print 'Reading All Stock Tickers'

import csv
import urllib2
import datetime
import math
import numpy as np

fullurl = 'http://data.okfn.org/data/core/s-and-p-500-companies/r/constituents.csv'
pull = urllib2.urlopen(fullurl)
ticker_data = csv.reader(pull)
tickers = [] 
for row in ticker_data:
	tickers.append(row[0])
tickers = tickers[1:]
print tickers

outfile = open("tickers.csv", "w")
for tick in tickers:
	outfile.write('"%s"\n' %tick)
outfile.close()