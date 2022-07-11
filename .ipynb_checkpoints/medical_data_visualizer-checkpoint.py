import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# calculating the bmi
df['bmi'] = df.weight / ((df.height / 100) **2)

# calculating overweight value 
def overweight_function(x):
    if x > 25:
        return 1
    else: return 0

# Add 'overweight' column
df['overweight'] = df.bmi.apply(lambda x :overweight_function(x))

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def norm_data(x):
    if x == 1:
        return 0
    else: return 1
df.cholesterol = df.cholesterol.apply(lambda x :norm_data(x))
df.gluc = df.gluc.apply(lambda x :norm_data(x))

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat =  df[['id', 'cardio', 'cholesterol','gluc', 'smoke', 'alco', 'active', 'overweight']].melt(id_vars=['id', 'cardio'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat = None

    # Draw the catplot with 'sns.catplot()'
    cat_order = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    
    fig = sns.catplot(x='variable',hue = 'value',
               data=df_cat, kind="count", col='cardio', order = cat_order, aspect = 1)
    fig.set_ylabels('total')
    


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
