import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')

#print (df.head)

print ('\n')

df['PCT'] = (df['Adj. High'] - df['Adj. Low'] / df['Adj. Low']) * 100.0

df = df [['Adj. Open','Adj. High','Adj. Low', 'PCT']]

print (df.head)
