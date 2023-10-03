

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 00:31:17 2022

@author: sirui qi

This python is divided into cells by the "#%%", and each cell corresponds to one part of an exercise in the Intermediate Python workshop.

Please run this cell first. This cell will help you import all needed packages in following cells.

Use the "run the current cell and go to the next cell" button on upper toolbar, or use the shortcut "shift + enter".

"""

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
## Scatterplot example using matplotlib
import matplotlib.pyplot as plt
import pandas as pd


surveys_complete = pd.read_csv('data/surveys.csv')
surveys_complete = surveys_complete.dropna()


x = surveys_complete.weight
y = surveys_complete.hindfoot_length
surveys_plot_plt = plt.scatter(x, y, s =10, c='black')
plt.show()


## Plot element customization using matplotlib
import numpy as np
labels, index = np.unique(surveys_complete.species_id, return_inverse=True)
# Now we apply the indices to the data points
surveys_plot_plt = plt.scatter(x, y, s =10, c=index)
# legend
plt.legend(surveys_plot_plt.legend_elements(num=None)[0], labels, ncol=6, loc='upper left', bbox_to_anchor=(-0.05, 1.15))
#other aspects such as x-label title, applying log scale to x-axis
plt.xlabel("Weight (g)")
plt.xscale("log")
plt.show()


## Boxplots with matplotlib
data = []
labels = []
for element in np.unique(surveys_complete.species_id):
    data.append(surveys_complete.loc[surveys_complete['species_id'] == element, 'weight'].to_numpy())
    labels.append(element)

plt.boxplot(data,
            labels=labels)  # additional arguments can be provided to control whisker and box width, marker size, shape, color, opacity etc.
plt.xlabel("Species ID")
plt.ylabel("weight distribution")

plt.show()


## Combining matplotlib elements with plotnine
myplot = (p9.ggplot(data=surveys_complete,
         mapping=p9.aes(x='hindfoot_length', y='weight')) +
         p9.geom_point())


plt_myplot = myplot.draw() #plotnine object converted to matplotlib object
p9_ax = plt_myplot.axes[0] #This generates the “ax” parameters

## p9_ax object can now be customized using matplotlib

p9_ax.set_xlabel("Hindfoot length")
p9_ax.tick_params(labelsize=16, pad=8)
p9_ax.set_title('Scatter plot of weight versus hindfoot length', fontsize=15)
plt.show()
