# -*- coding: utf-8 -*-
"""
Created on Tue May 16 23:10:33 2023

@author: DELL
"""

# -*- coding: utf-8 -*-


#https://www.kaggle.com/datasets/shwetankchaudhary/power-bi-sample-data?datasetId=2565391&sortBy=dateRun&tab=bookmarked

import matplotlib.pyplot as plt
import pandas as pd

# To change the font on the graph
plt.rcParams["font.family"] = "Arial"

# Reading the dataset from an external source
url = "https://drive.google.com/file/d/1nH74xls5nqOuGQepjuIaxQJBc-vBNq_R/view?usp=sharing"
#sales_df = pd.read_excel(r"C:\Users\navee\Downloads\Sample data.xlsx")
sales_df = pd.read_csv("https://drive.google.com/uc?export=download&id="+url.split('/')[-2])
print(sales_df.head())

# To display the list of column names in the dataset
column_names = list(sales_df)
print(column_names)

# Convert the Date column to datetime format
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

# Create a new column for the month
sales_df['Month'] = sales_df['Date'].dt.strftime('%b')
#print(sales_df['Month'])

#function to display the months in order on the X-axis
def order_months(months_list):
    """Orders a list of month names in chronological order."""
    # Define a dictionary to map month names to their corresponding numbers
    month_to_num = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }
    # Create a list of tuples with month names and their corresponding numbers
    month_num_list = [(month, month_to_num[month]) for month in months_list]
    # Sort the list of tuples by month number
    sorted_month_num_list = sorted(month_num_list, key=lambda x: x[1])
    # Extract the sorted list of month names
    sorted_months_list = [month_num[0] for month_num in sorted_month_num_list]
    return sorted_months_list



# Group the data by month and calculate the sum of sales
sales_by_month = sales_df.groupby(('Month'), sort = False)[' Sales'].sum()
print(sales_by_month)

# Order the months
ordered_months = order_months(sales_by_month.index)

# Reindex the data by the ordered months
sales_by_month = sales_by_month.reindex(ordered_months)


colors = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
# Plot the bar chart
sales_by_month.plot(kind='bar', 
                    color=colors, 
                    alpha=0.65, 
                    edgecolor='black')

# Set the chart title and axis labels
plt.title('Montly Sale')
plt.xticks(rotation=90, horizontalalignment="center")
plt.xlabel('Month')
plt.ylabel('Total Sales')

# Display the chart
plt.show()
