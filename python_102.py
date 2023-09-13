

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 00:31:17 2022

@author: sirui qi

This python is divided into cells by the "#%%", and each cell corresponds to one part of an exercise in the Intermediate Python workshop.

Please run this cell first. This cell will help you import all needed packages in following cells.

Use the "run the current cell and go to the next cell" button on upper toolbar, or use the shortcut "shift + enter".

"""
import pandas as pd # Import the Panda package and name it as pd for convenience
import os

#%%
## check the data types of different data, and check the data types of different computation results

print('the type of 10:', type(10))
print('the type of 10.0:', type(10.0))
print("the type of '10':", type('10.0'))

print("\n")

print('the type of 10+10:', type(10+10))
print('the type of 10+10.0:', type(10+10.0))
print("the type of 10*10.0:", type(10*10.0))

try:
    print("the type of 10+'10.0':", type(10+'10.0'))
except Exception as e:
    print("the type of 10+'10.0':", e)
    
print("the type of '10.0'+'10':", type('10.0'+'10'))
print("the result of '10.0'+'10':", '10.0'+'10')

#%%
## read the survey dataset from data directory using the pandas function, read_csv, and check the data types of columns in pandas dataframe
## then practice changing the data types for different columns


surveys_df = pd.read_csv("data/surveys.csv") #load the dataframe using pandas 
print('type of surveys_df:', type(surveys_df), '\n')  
print('type of each column in surveys_df:')
print(surveys_df.dtypes)

print('type of sex:', surveys_df['sex'].dtype)

# this will work for changing the data type of record_id
print('type of record_id:', surveys_df['record_id'].dtype) 
surveys_df['record_id'] = surveys_df['record_id'].astype('float64')
print('type of record_id:', surveys_df['record_id'].dtype)

# this will not work for changing the data type of plot_id. think about what is the reason
print('type of plot_id:', surveys_df['plot_id'].dtype)
surveys_df.plot_id.astype("float")
print('type of plot_id:', surveys_df['plot_id'].dtype)

#%%
##basic operations on dataframes and exporting a dataframe to a new file

surveys_df = pd.read_csv("data/surveys.csv") #reload the dataframe using pandas
print(surveys_df)
df_na = surveys_df.dropna() #remove rows with missing values in dataframe
print(df_na)
df_na.to_csv('data/surveys_complete.csv', index=False)  #save the new dataframe to a csv file
print(os.listdir('data'))

#%%
##queries
surveys_df
surveys_df[(surveys_df.year == 1990) & (surveys_df.weight <= 8)]
surveys_df[surveys_df.weight >= 0]
surveys_df[surveys_df.weight.isnull()]
surveys_df[surveys_df['species_id'].isin(['NL', 'DM'])]
surveys_df[surveys_df.sex.isnull()]
surveys_df[surveys_df.sex.isin(['F', 'M'])]
surveys_df[(surveys_df.sex != 'F') & (surveys_df.sex != 'M')]
surveys_df[pd.isnull(surveys_df).any(axis=1)]

#%%
from matplotlib import pyplot as plt
empty_weights = surveys_df[pd.isnull(surveys_df['weight'])]['weight']
empty_weights

