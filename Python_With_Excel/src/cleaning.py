""" *
    *   Cleaning or Organising Data
    * """
import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv('.\\Exercise Files\\Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code','Income']


""" *
    *   the first step is to clean our data by getting rid of unnecessary columns
    *   
    *   inplace : it confirms that we are applying the changes to the data frames's current instance so that we don't 
    *   have to assign the result to itself may be like df = df.drop()
    * """
df.drop(columns='Address', inplace=True)


""" *
    *   let's setup indexed for our area code
    *   
    *   using an area code in a format like this allows us to use these unique identifiers a
    * """
df = df.set_index('Area Code')
print(df)
print('=' * 20)
print()
print(df.loc[8074])  # <-- this is the area code on which we setup an index
print('=' * 20)
print()
print(df.iloc[0])  # <-- this is normal way of accessing the information
print('=' * 20)
print()


""" *
    *   let's look at everyone's first name, this is using a slice method
    *   so it's giving us all the records with the First Name column in selection.
    * """
print(df.loc[8074:,'First'])
print('=' * 20)
print()


""" *
    *   if you remember, when we searched for all Johns who lived in Riverside, we only got one of the two.
    *   so we need to somehow read everyone's first name and use a string function to split it by spaces.
    *
    *   writing this 
    *       df.First.str.split()
    *   is similar to 
    *       df['First'].str.split()
    *   
    *   here we are splitting the string from First column
    * """
print(df['First'].str.split(expand=True))
print('=' * 20)
print()


""" *
    *   so now to fetch the first column of the string split 
    * """
# df.First = df['First'].str.split(expand=True)[0]  # <-- we can do something like this
df.First = df['First'].str.split(expand=True)  # <-- pandas will automatically set the 0th column values
print(df)
print('=' * 20)
print()


""" *
    *   replacing the NaN value with our own string
    * """
df = df.replace(np.nan, 'N/A', regex=True)
print(df)
print('=' * 20)
print()