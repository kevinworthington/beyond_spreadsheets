

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 00:31:17 2022

@author: sirui qi

This python is divided into cells by the "#%%", and each cell corresponds to one part of an exercise in the Intermediate Python workshop.

Please run this cell first. This cell will help you import all needed packages in following cells.

Use the "run the current cell and go to the next cell" button on upper toolbar, or use the shortcut "shift + enter".

"""

new_df = surveys_df[pd.isnull(surveys_df['sex'])]['sex']
new_df
new_df[:]='x'
new_df

surveys_df[(surveys_df.sex.isin(['F', 'M'])) & (surveys_df.weight > 0)][['sex','weight']]
new_df = surveys_df[(surveys_df.sex.isin(['F', 'M'])) & (surveys_df.weight > 0)][['sex','weight']]
new_df.mean()
#ax = new_df.plot.bar(x='sex', y='weight', stacked=True)
#ax

df_mean=new_df.groupby(['sex']).agg({'weight':'mean'})
plt.bar(df_mean.index, df_mean['weight'])
plt.show()
#%%
##load two dataframes and concatenate

surveys_df = pd.read_csv("data/surveys.csv")
print(surveys_df)
species_df = pd.read_csv("data/species.csv", keep_default_na=False, na_values=[""]) #load another dataframe using pandas and assign missing values to be NAN data type
print('\nspecies_df:')
print(species_df)

survey_sub_first10 = surveys_df.head(10) # Read in first 10 lines of surveys table
survey_sub_last10 = surveys_df.tail(10) # Grab the last 10 rows
survey_sub_last10 = survey_sub_last10.reset_index(drop=True) # drop=True option avoids adding new index column with old index values
vertical_stack = pd.concat([survey_sub_first10, survey_sub_last10], axis=0)
print("\nvertical_stack:")
print(vertical_stack)
horizontal_stack = pd.concat([survey_sub_first10, survey_sub_last10], axis=1)
print("\nhorizontal_stack:")
print(horizontal_stack)

#%%
##join two dataframes in different ways

surveys_df = pd.read_csv("data/surveys.csv")
survey_sub = surveys_df.head(10)
species_sub = pd.read_csv('data/speciesSubset.csv', keep_default_na=False, na_values=[""]) #load another dataframe using pandas and assign missing values to be NAN data type

merged_inner = pd.merge(left=survey_sub, right=species_sub, left_on='species_id', right_on='species_id')
print('the shape of merged_inner:', merged_inner.shape)
print('\ninner join:')
print(merged_inner)

merged_left = pd.merge(left=survey_sub, right=species_sub, how='left', left_on='species_id', right_on='species_id')
print('the shape of merged_left:', merged_left.shape)
print('\nleft join:')
print(merged_left)