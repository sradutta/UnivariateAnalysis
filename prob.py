'''The results of rolling a six-sided die 30 times is as follows: 1, 4, 6, 1, 5, 3, 2, 5, 4, 6, 1, 2, 4, 3, 5, 6, 3, 2, 1, 1, 5, 6, 2, 4, 4, 3, 1, 6, 2, 4. Write a python code that will calculate the frequencies and generate the boxplot, histogram and qq-plot.'''

#import libraries
import collections
import matplotlib.pyplot as plt
import scipy.stats as stats

#data
testlist=[1, 4, 6, 1, 5, 3, 2, 5, 4, 6, 1, 2, 4, 3, 5, 6, 3, 2, 1, 1, 5, 6, 2, 4, 4, 3, 1, 6, 2, 4]

#count the total number of items in the collection
c = collections.Counter(testlist)

#calculate the number of instances in the list
count_sum = sum(c.values())

#print the frequency in a file
with open('unit2lesson2frequency', 'w') as outputFile:
    outputFile.write('dice-result, frequency\n')
    for k, v in c.iteritems():
        outputFile.write(str(k) + ',' + str(float(v)/count_sum) + '\n')
outputFile.close()

#create boxplot
plt.boxplot(testlist)
plt.savefig('frequency_boxplot.jpg')

#create histogram
plt.hist(testlist,histtype='bar')
plt.savefig('frequency_histogram.jpg')

#create qqplot
graph=stats.probplot(testlist, dist='norm', plot=plt)
plt.savefig('frequency_qqplot.jpg')
