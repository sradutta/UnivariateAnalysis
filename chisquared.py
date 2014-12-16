#import libraries
import scipy.stats as stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

#clear data and find the frequency
loansData = pd.read_csv('loansData.csv')
loansData.dropna(inplace=True)
freq=collections.Counter(loansData['Open.CREDIT.Lines'])
print freq

'''The unique number of open credit lines are 4. They are 31, 34, 36, 38. The most frequent number of open credit lines is 8.'''

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

'''The data is a little right-skewed'''


chi, p = stats.chisquare(freq.values())
print chi, p








