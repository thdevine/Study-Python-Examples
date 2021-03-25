import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
#%% section 1     #os.chdir('C:\\Users\\tdevine\\Desktop\\2018_M2\\metrics2\\ass2\\data’) #Changes the current directory
os.chdir('C:\\Users\\tdevine\\Desktop\\CMU-2018-2019-2020\\metrics2\\ass2\\data') #Changes the current directory

# # Below gives you the ‘data.csv’ file.
# PCEND = pd.read_csv('PCEND.csv')     # Personal Consumption Expenditures: Nondurable Goods (billions of dollars) from FED
# PPCEND = pd.read_csv('PPCEND.csv')   # Personal consumption expenditures: Nondurable goods (chain-type price index), DNDGRG3M086SBEA from FED
# CNP16OV = pd.read_csv('CNP16OV.csv') # Civilian Noninstitutional Population (thousands of persons) from FED
# GS1 = pd.read_csv('GS1.csv')         # annualized 1-Year Treasury Constant Maturity Rate from FED
# SP500 = pd.read_csv('SP500.csv')     # S&P 500 index at closing price of the first day of the month
# PPCES = pd.read_csv('PPCES.csv')     # Personal Consumption Expenditures : Services (Chain-type price index)
# PCES = pd.read_csv('PCES.csv')       # Personal Consumption Expenditures : Services
# SP500['DATE']=SP500['Date']
# del SP500['Date']
# frames = [PCEND, PPCEND, CNP16OV, GS1, SP500, PPCES, PCES]
# df = reduce(lambda  left,right: pd.merge(left,right,on=['DATE'],how='outer'), frames)
# df=df.dropna()
# date_thres = pd.to_datetime('2017-12-01')
# df['DATE']=pd.to_datetime(df['DATE'])
# df=df[df['DATE']<=date_thres]

# data = pd.read_csv('data.csv')

#%% section 2
# To open the data (alternative method):
dat = ("C:\\Users\\tdevine\\Desktop\\CMU-2018-2019-2020\\metrics2\\ass2\\data\data.csv")
filename = open(dat, 'r')
data = pd.read_csv(filename)

#%% section 3

# Code for creating a lagged time series
# df['Data_lagged'] = df.groupby(['Group'])['Data'].shift(1)
# df['lagprice'] = df['price'].shift(1)

#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.shift.html

# Create new columns for lagged PPCEND and lagged PPCES 
data['lag_PPCEND'] = data['PPCEND'].shift(12)
data['lag_PPCES'] = data['PPCES'].shift(12)
data['lag_SP500'] = data['SP500'].shift(12)

# Create deflated columns
data['rCpc']= np.divide(1e9*data.PCEND, np.multiply(data.PPCEND/100, data.CNP16OV*1000))
data['rCps'] = np.divide(1e9*data.PCES, np.multiply(data.PPCES/100,data.CNP16OV*1000))#service
data['rCt'] = data.rCpc + data.rCps #total 
data['a_inflation'] =  np.divide(data.PPCEND,data.lag_PPCEND) - 1
data['Rb'] = np.power(1 +np.divide(data.GS1,100) - data.a_inflation,1/12 )  #total monthly return to bonds (deflated)
data['Rm'] = np.multiply(np.divide(data.SP500,data.lag_SP500),np.divide(data.lag_PPCEND,data.PPCEND))  #total monthly return to stocks (deflated)
data['lag_rCpc'] = data['rCpc'].shift(12)
data['Rc'] = np.divide(data.rCpc,data.lag_rCpc)  #total monthly return to per-capita consumption (deflated)

#%% section 4
# Plot
data['rrCpc'] = 0
for i in range(1,data.shape[0]):
    data.loc[i,'rrCpc'] = data.rCpc[i] / data.rCpc[i-1]
data.rrCpc[0] = data.loc[1,'rrCpc']
plt.plot(data.rrCpc)
plt.show()

data['rrCt'] = 0
for i in range(1,data.shape[0]):
    data.loc[i,'rrCt'] = data.rCt[i] / data.rCt[i-1]
data.rrCt[0] = data.loc[1,'rrCt']
plt.plot(data.rrCt)
plt.show()


data['rRm'] = 0
for i in range(1,data.shape[0]):
    data.loc[i,'rRm'] = data.Rm[i] / data.Rm[i-1]
data.rRm[0] = 	data.loc[1,'rRm']

plt.plot(data.rRm)
plt.show()

#https://machinelearningmastery.com/time-series-data-stationary-python/

from statsmodels.tsa.stattools import adfuller

# Unit root test for rrCpc
result1 = adfuller(data.rrCpc)
print('ADF Statistic: %f' % result1[0])
print('p-value: %f' % result1[1])
print('Critical Values:')
for key, value in result1[4].items():
 	print('\t%s: %.3f' % (key, value))
   
# Unit root test for rCt
result2 = adfuller(data.rCt)
print('ADF Statistic: %f' % result2[0])
print('p-value: %f' % result2[1])
print('Critical Values:')
for key, value in result2[4].items():
 	print('\t%s: %.3f' % (key, value))

# Unit root test for rRm
  #Here I drop the first 12 rows because they are full of NaN
result3 = adfuller(data.loc[13:,'rRm'])
print('ADF Statistic: %f' % result3[0])
print('p-value: %f' % result3[1])
print('Critical Values:')
for key, value in result3[4].items():
 	print('\t%s: %.3f' % (key, value))






# unit root testing in r using ur.df() package
#https://stats.stackexchange.com/questions/129842/best-practice-for-adf-kpss-unit-root-testing-sequence



