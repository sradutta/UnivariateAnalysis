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
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.savefig("amtfundbyinv_boxplot.jpg")

#generate a histogram
loansData.hist(column="Amount.Funded.By.Investors")
plt.savefig("amtfundbyinv_histogram.jpg")

#generate a qq-plot
plt.figure()
graph=stats.probplot(loansData["Amount.Funded.By.Investors"], dist="norm", plot=plt)
plt.savefig("amtfundbyinv_qqplot.jpg")
