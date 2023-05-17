# -*- coding: utf-8 -*-
"""
Created on Tue May 16 23:12:29 2023

@author: DELL
"""

# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import pandas as pd

#importing the data from an external source
url = "https://drive.google.com/file/d/1qoVpHcuryH7sDB-vG3KnnNfUfZ8RbCNn/view?usp=sharing"
#dataframe = pd.read_csv(r'C:\Users\navee\Downloads\People using at least basic sanitation services (% of population).csv')
dataframe = pd.read_csv("https://drive.google.com/uc?export=download&id="+url.split('/')[-2])

#dropping unncessary columns to refine the data
dataframe = dataframe.drop(columns=['Series Name', 'Series Code', 'Country Code', '2021 [YR2021]'])
dataframe = dataframe.dropna()

#renaming columns for better access
dataframe = dataframe.rename(columns={'Country Name': 'Country'})
print(dataframe)

#function to print the first five tuples in a dataset
print(dataframe.head())

dataframe = dataframe.drop([3, 6, 8, 9, 12, 13, 14, 15, 16, 18])

# line plot
year = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

plt.figure(figsize=(8, 5))
#iloc function to display the values from 2012 to 2020
plt.plot(year, dataframe.iloc[1, 1:10], label='Austraila')
plt.plot(year, dataframe.iloc[2, 1:10], label='Bangladesh')
plt.plot(year, dataframe.iloc[3, 1:10], label='Brazil')
plt.plot(year, dataframe.iloc[4, 1:10], label='Canada')
plt.plot(year, dataframe.iloc[5, 1:10], label='China')
plt.plot(year, dataframe.iloc[6, 1:10], label='Afghanistan')
plt.xlabel('Year')
plt.ylabel('% of pop')
plt.title('Usage of  basic sanitation services from 2012 to 2020')
plt.legend()
plt.show()