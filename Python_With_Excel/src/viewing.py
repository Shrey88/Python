""" *
    *   while working with pandas manipulating data frame is key to get what you want out of your data.
    *
    * """
import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('.\\Exercise Files\\Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code','Income']


""" *
    *   although we have setup our own columns, imagine if you had to deal with a spreadsheet with so many columns that 
    *   it was hard to fully read the data through your terminal. You need to know which columns contain what so that you
    *   can access the date you need to proceed.
    *   In order to do this we need to use the same function we used to assign the columns.
    *"""
print(df.columns)
print('=' * 20)
print()


""" *
    *   let's say you want to view only one column. Panda's is a multi row and multi column data structure, but it's 
    *   functionality makes it easy for us to do this in one line with no iteration required.
    * """
print(df['First'])
print('=' * 20)
print()


""" *
    *   if you want to access multiple column's data, we'd just pass it in as a list
    *   we are using double brackets here because we are presenting the index of the data frame as a list of columns
    * """
print(df[['State', 'Area Code']])
print('=' * 20)
print()


""" *
    *   if we had large set of data, we could only want to view certain values in a column, we can achieve this by 
    *   slicing
    *   we want first columns with first 3 rows
    * """
print(df['First'][0:3])
print('=' * 20)
print()


""" *
    *   rows are indexed automatically by pandas we use them to locate specifically with integer location function
    *   if we pass in the first index and print that to terminal then we should see that the row printed corresponds to 
    *   the index given at the ilocation.
    *
    *   ilocation function is a very useful tool when iterating through a data frame as you can increment the row
    *   repeatedly.
    * """
print(df.iloc[1])
print('=' * 20)
print()


""" *
    *   although pandas has some functionality for more efficient ways of gathering data rather than iteration, we can 
    *   also use the ilocation function with two numbers or variables and they correspond to a row-column value or 
    *   coordinate system 
    *   
    *   we recognised that indices are numbered starting at zero and our headers are strings.
    *   when using location function headers also correspond to integer values for their length starting at zero
    *
    *   so if we wanted to print Repici
    * """
print(df.iloc[2,1])
print('=' * 20)
print()


""" *
    *   we can combine any of these access and viewing functions for saving, so if you want to grab certain rows or 
    *   columns, or even a specific location of an Excel file, you can pick them out of your data frame, store them and 
    *   save them
    * """
wanted_values = df[['First', 'Last', 'State']]
stored = wanted_values.to_excel(".\\Exercise Files\\Stored_Location.xlsx", index=None)