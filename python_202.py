

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
import zipfile
import wget
import csv
import json


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


