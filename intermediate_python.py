

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
import plotnine as p9
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

#%%
##for loop practice

animals = ['lion', 'tiger', 'crocodile', 'vulture', 'hippo'] # create a str list
print(animals)
print() #empty print function will print blank line, which will make the whole output more readable
for creature in animals: 
    print(creature)
    
print()
for creature in animals: 
    print('The loop variable is now: ' + creature)
print()
surveys_df = pd.read_csv('data/surveys.csv')
surveys_2002 = surveys_df[surveys_df.year == 2002] #filter out the 2002 year data and save it into a new dataframe named surveys_2002
surveys_2002.to_csv('data/surveys_2002.csv') #save new datafame to csv file
surveys_df['year'].unique() #print the year infomation of the original surveys dataframe, and this will help us understand how much year information in the dataframe
for year in surveys_df['year'].unique():
    filename='data/surveys_' + str(year) + '.csv' #for each year, create a different file name
    print(filename)
    surveys_year = surveys_df[surveys_df.year == year] #filter out one year and pass it to a new dataframe
    surveys_year.to_csv(filename)
print()
print(os.listdir('data'))

#%%
## basic function creation practice
def this_is_the_function_name(input_argument1, input_argument2): #this line will include function name and inputs

    # The body of the function is indented
    # This function prints the two arguments to screen
    print('The function arguments are:', input_argument1, input_argument2, '(this is done inside the function!)')

    # And returns their product
    return input_argument1 * input_argument2

this_is_the_function_name(2, 5)

#%%
def one_year_csv_writer(this_year, all_data):
    """
    Writes a csv file for data from a given year.

    this_year -- year for which data is extracted
    all_data -- DataFrame with multi-year data
    """

    # Select data for the year
    surveys_year = all_data[all_data.year == this_year]

    # Write the new DataFrame to a csv file
    filename = 'data/function_surveys_' + str(this_year) + '.csv'
    surveys_year.to_csv(filename)

surveys_df = pd.read_csv('data/surveys.csv')
one_year_csv_writer(2002, surveys_df) #pass the year and dataframe to the 'one_year_csv_writer' function
print(os.listdir('data'))

#%%
def yearly_data_csv_writer(start_year, end_year, all_data):
    """
    Writes separate CSV files for each year of data.

    start_year -- the first year of data we want
    end_year -- the last year of data we want
    all_data -- DataFrame with multi-year data
    """

    # "end_year" is the last year of data we want to pull, so we loop to end_year+1
    for year in range(start_year, end_year+1):
        one_year_csv_writer(year, all_data)

yearly_data_csv_writer(1977, 2002, surveys_df) #pass the year range and dataframe to the 'yearly_data_csv_writer' function
print(os.listdir('data'))



#%%
### Making Plots With plotnine

## Plotting with plotnine

import plotnine as p9


surveys_complete = pd.read_csv('data/surveys.csv')
surveys_complete = surveys_complete.dropna()


surveys_plot = p9.ggplot(data=surveys_complete, mapping=p9.aes(x='weight', y='hindfoot_length'))
surveys_plot +  p9.geom_point() # creates the plot


## Chaining elements with plotnine
surveys_plot = p9.ggplot(data=surveys_complete, mapping=p9.aes(x='weight', y='hindfoot_length', color='species_id'))
(surveys_plot 
+ p9.geom_point() 
+ p9.xlab("Weight (g)") 
+ p9.scale_x_log10()
+ p9.theme_bw()
+ p9.theme(text=p9.element_text(size=16)))


#%%
## Other plots with plotnine

# Boxplot
surveys_plot = p9.ggplot(data=surveys_complete, mapping=p9.aes(x='species_id', y='weight'))
surveys_plot + p9.geom_boxplot()

# Time series
yearly_counts = surveys_complete.groupby(['year', 'species_id'])['species_id'].count()
yearly_counts = yearly_counts.reset_index(name='counts')
surveys_plot = p9.ggplot(data=yearly_counts, mapping=p9.aes(x='year', y='counts',  color='species_id'))
surveys_plot + p9.geom_line()


#%%
##Split plots

# facet_wrap
surveys_plot = p9.ggplot(data=surveys_complete, mapping=p9.aes(x='weight', y='hindfoot_length', color='species_id'))
surveys_plot + p9.geom_point(alpha=0.1)
surveys_plot + p9.geom_point(alpha=0.1) + p9.facet_wrap("plot_id")


# facet_grid
# only select the years of interest
survey_2000 = surveys_complete[surveys_complete["year"].isin([2000, 2001])]


(p9.ggplot(data=survey_2000,
           mapping=p9.aes(x='weight',
                          y='hindfoot_length',
                          color='species_id'))
    + p9.geom_point(alpha=0.1)
    + p9.facet_grid("year ~ sex")
)



#%%
##Further Customizations

# Change text angle
surveys_plot = p9.ggplot(data=surveys_complete, mapping=p9.aes(x='factor(year)'))
surveys_plot + p9.geom_bar()
surveys_plot + p9.geom_bar() + p9.theme_bw()  + p9.theme(axis_text_x = p9.element_text(angle=90))



# custom theme and categorical variable with 'factor' function
my_custom_theme = p9.theme(axis_text_x = p9.element_text(color="grey", size=10, angle=90, hjust=.5), axis_text_y = p9.element_text(color="grey", size=10))
surveys_plot = p9.ggplot(data=surveys_complete, mapping=p9.aes(x='factor(year)'))
surveys_plot + p9.geom_bar() + my_custom_theme

# Saving
my_plot = (p9.ggplot(data=surveys_complete,
           mapping=p9.aes(x='weight', y='hindfoot_length', color='species_id'))
    + p9.geom_point()
    
)
my_plot.save("my_bar_graph.png", width=10, height=10, dpi=300) 

