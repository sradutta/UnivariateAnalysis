import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

#read the data from the directory
loansData = pd.read_csv('/Users/kuttush/Desktop/Spongebob/Thinkful/DataScience/Prob_And_Stats/loansData.csv')
print loansData

#remove the rows with null values.Return object with labels on given axis 
#omitted where alternately any or all of the data are missing
loansData.dropna(inplace=True)
print loansData

#generate the boxploat and show it
loansData.boxplot(column='Amount.Requested')
plt.savefig("boxplot.jpg")

#generate a histogram
loansData.hist(column="Amount.Requested")
plt.savefig("histogram.jpg")

#generate a qq-plot
plt.figure()
graph=stats.probplot(loansData["Amount.Requested"], dist="norm", plot=plt)
plt.savefig("qqplot.jpg")




'''Observations: Both the histograms of "amount.requested and amount.funded.by.investors" are right-skewed. The median for amount.requested is approximately 269.5. The median for amount.funded.by.investors is approximately 227.5. Since boththe graphs are right-skewed, thus the means are going to be greater than 269.5 and 227.5 respectively. The graph of the amount.funded.by.investors looked approximately normal.'''


'''Observations for Boxplot: The minimum value for amount.requested is larger than that of the amount.funded.by.investors (its minimum value being zero). However, the maximum value of amount.funded is greater than that of the amount.funded.y.investors. For both the graphs, the maximum values seem outliers. However, the second-quartile or median occurs at 10,000 for both the graphs. Thus, about 50% of the data has values less than 10,000 and about 50% has values greater than 10,000.'''


'''Observations for QQ-Plot: Neither of the distributions are normally-distributed since there are cluster of points that have deviated away from the line.''' 
