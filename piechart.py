# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:07:59 2023

@author: DELL
"""

# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

url = 'https://drive.google.com/file/d/12akRDB02Ph5vAbcKSlJySZqGHl0OdZGM/view?usp=sharing'

#data = pd.read_csv(r'C:\Users\navee\Downloads\Olympic Medals.csv')
data = pd.read_csv("https://drive.google.com/uc?export=download&id="+url.split('/')[-2])

#Dropping unnecssary columns
data = data.drop(columns=['Image URL'])

country_data = data["Country Name"]
#medal_data = data['1988'] 
medal_data =data['2000']

print(medal_data)
#prints the first five tuples of the dataset
print(data.head())

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0.1)

#function for conversting hexadecimal values of colors to RGB
def hex_to_RGB(hex_str):
    """ #FFFFFF -> [255,255,255]"""
    #Pass 16 to the integer function for change of base
    return [int(hex_str[i:i+2], 16) for i in range(1,6,2)]

#function to get a color gradient for the pie chart
def get_color_gradient(c1, c2, n):
    """
    Given two hex colors, returns a color gradient
    with n colors.
    """
    assert n > 1
    color1_rgb = np.array(hex_to_RGB(c1))/255
    color2_rgb = np.array(hex_to_RGB(c2))/255
    mix_pcts = [x/(n-1) for x in range(n)]
    rgb_colors = [((1-mix)*color1_rgb + (mix*color2_rgb)) for mix in mix_pcts]
    return ["#" + "".join([format(int(round(val*255)), "02x") for val in item]) for item in rgb_colors]

plt.figure(figsize=(30, 15))
color1 = "#0F3BFF"
color2 = "#2AE6F7"
#explode = (0.1, 0, 0, 0.1, 0.1)  
plt.pie(medal_data, 
        labels=country_data, 
        explode = explode, 
        colors = get_color_gradient(color1, color2, len(country_data)), 
        autopct='%1.1f%%', 
        shadow=True, 
        startangle=180,
        wedgeprops = {
            "edgecolor" : "white",
            'linewidth': 1,
            'antialiased': True})
#plt.pie(data['1988'], labels=data['Country Name'], autopct='%1.1f%%', shadow=True)

plt.title('Medal Achievements for different countries in the year 2000')
plt.show()
