

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
import numpy as np
import os
import plotnine as p9

import zipfile
import wget
import csv
import json

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


import plotnine as p9

#%%
### Making Plots With plotnine

## Plotting with plotnine



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

#%%
## check the existence of a file and unzip it

url = 'http://bit.ly/python-feb2'
zip_file_name = wget.download(url) #wget will create duplicates when downloading the existed file
print('download file name:',zip_file_name)
directory_name = 'my_data'
if os.path.exists(zip_file_name):
    print(zip_file_name+' exist!')
    print('unzipping files')
    zip_ref = zipfile.ZipFile(zip_file_name, 'r')
    zip_ref.extractall(directory_name)
    zip_ref.close()
    # with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
    #     zip_ref.extractall(directory_name) #this command will overwrite existed files
    print('files extracted to '+directory_name)


#%%
## with statement practice

for i in range(5):
    file1 = open('write_the_file1.txt', 'a')
    file1.write('hello world !\n')
    
    file2 = open('write_the_file2.txt', 'a')
    file2.write('hello world !\n')
    file2.close()
    
    with open ('write_the_file3.txt', 'a') as file3:
            file3.write('hello world !\n')
            
with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
    zip_ref.extractall(directory_name)


#%%
## directory processing

print ('The current working directory is ' + os.getcwd())
path = 'tmp/year'
if not os.path.exists(path):
    print(path + ' is being created')
    os.makedirs(path)
else:
    print(path + ' already exists')

os.chdir(path)
print ('The current working directory is ' + os.getcwd())

os.chdir('../..')
print ('The current working directory is ' + os.getcwd())


#%%
## load csv file using csv

with open('my_data/species.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    print(reader)
    print(type(reader))
    line = next(reader)
    print(line)
    print(type(line))
    
    for row in reader:
        print(', '.join(row))

with open('my_data/species.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    rows = list(reader)
    print(rows)
    print(rows[0])
    
with open('my_data/species.csv', 'a') as csvfile:
    writer = writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['ZM', 'Zenaida', 'macroura', 'Bird'])


#%%
## load csv file using numpy and pandas

arr = np.loadtxt("my_data/species.csv", delimiter=",", dtype=str)
print(type(arr))
print(arr[1])
print(arr[0][1])

df = pd.read_csv("my_data/species.csv")
print(df.info())
print(df.loc[0,'species_id'])


#%%
## json practice

with open('my_data/species.json') as json_data:
    data = json.load(json_data)
    print(type(data))
    print(type(data[0]))
    print(data[0])
    print()
    print(type(json.dumps(data[0], indent=None)))
    print(json.dumps(data[0], indent=None))
    print()
    print(json.dumps(data[0], indent=1))
    
with open('my_data/species.json') as json_data:
    data = json.load(json_data)
    new_species = {"species_id": "AA", "genus": "Amphispiza", "species": "bilineata", "taxa": "Bird"}
    print(json.dumps(data[-1], indent=None))
    data.append(new_species)
    print(json.dumps(data[-1], indent=None))
    
with open('my_data/temp.json', 'w') as json_data:
    new_species_1 = {"species_id": "AA", "genus": "Amphispiza", "species": "bilineata", "taxa": "Bird"}
    new_species_2 = {"species_id": "BB", "genus": "Amphispiza", "species": "bilineata", "taxa": "Bird"}
    new_species_3 = {"species_id": "CC", "genus": "Amphispiza", "species": "bilineata", "taxa": "Bird"}
    json_object = json.dumps([new_species_1, new_species_2, new_species_3], indent=4)
    json_data.write(json_object)
    
with open('my_data/temp.json', 'r+') as json_data:
    data = json.load(json_data)
    new_species = {"species_id": "DD", "genus": "Amphispiza", "species": "bilineata", "taxa": "Bird"}
    data[1]['species_id'] = 'DD'
    json_data.seek(0)  # rewind
    json.dump(data, json_data)
    json_data.truncate()
    
    
#%%
## identationError
nums = [11, 30, 44, 54]

for num in nums:
    square = num ** 2
     print(square)

#%%
## messing up the brackets
# a = list[]
a = list()

x = [1,2,3]
y = (1,2,3)
# print(x(1))
print(x[1])

# print(y(1))
print(y[1])

#%%
def sum(a,b):
    c = a + b
    return c

sum(1,2)
print(c)
    

#%%
### Making Plots With plotnine

def sum(a,b):
    c = a + b
    print(d)
    return c

sum(1,2)


#%%
## Other plots with plotnine

def division(x,y):
    z= x/y
    print(z)
division(5,1)
# division(5,0)

def new_division(x,y):
    try:
        z = x/y
        print(z)
    except ZeroDivisionError:
        print('divide by zero')
    
    
new_division(5,1)
new_division(5,0)



#%%
##Split plots

list1 = [1,2,3,4,5,6,7,8,9,0]
iter1 = iter(list1)
while True:
    try:
        print(next(iter1))
    except StopIteration:
        break

iter1 = iter(list1)
print(next(iter1))
#%%
##Further Customizations
#%%
##Further Customizations

url = 'http://bit.ly/python-oct13' 
zip_file_name = wget.download(url)
print('download file name:',zip_file_name)
directory_name = 'my_data' 
if os.path.exists(zip_file_name):
    print(zip_file_name+' exist!')
    print('unzipping files')
    zip_ref = zipfile.ZipFile(zip_file_name, 'r')
    zip_ref.extractall(directory_name)
    zip_ref.close()
    print('files extracted to '+directory_name)

#%%

for i in range(5):
    file1 = open('write_the_file1.txt', 'a')
    file1.write('hello world !\n')
    
    file2 = open('write_the_file2.txt', 'a')
    file2.write('hello world !\n')
    file2.close()
    
    with open ('write_the_file3.txt', 'a') as file3:
        file3.write('hello world !\n')

#%%

zip_ref = zipfile.ZipFile(zip_file_name, 'r')
zip_ref.extractall(directory_name)
zip_ref.close()

with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
    zip_ref.extractall(directory_name)

#%%
print ('The current working directory is ' + os.getcwd())

path = 'tmp/year'
if not os.path.exists(path):
    print(path + ' is being created')
    os.makedirs(path)
else:
    print(path + ' already exists')
    
#%%
os.chdir(path)
print ('The current working directory is ' + os.getcwd())
os.chdir('../..')
print ('The current working directory is ' + os.getcwd())

