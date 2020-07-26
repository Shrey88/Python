import pandas as pd
from openpyxl.workbook import workbook  # <-- this module is used to load the excel workbook or save the workbook in excel format

""" *
    *   initializing the dataframes to read the different types of files
    *   we are going to read 3 different types of file xslx, csv, txt
    * """

df_excel = pd.read_excel('.\\Exercise Files\\regions.xlsx')

# there is not much difference between the csv and txt file except for some little formatting differences
df_csv = pd.read_csv('.\\Exercise Files\\Names.csv')
df_txt = pd.read_csv('.\\Exercise Files\\data.txt')

""" *
    *   lets look how pandas format our data
    *
    *   panda uses indexes for rows and headers for columns
    *   
    *   in our case indices are integers and headers are string.
    * """
print(df_excel)  # formatting is much better in excel
print()

""" *
    *   we can see that indices are still intact, but first row of data is acting as a header
    *   in order to prevent this, we need to specify the header flag as None
    *
    *   we can even set the names for the header 
    * """
print(df_csv)
df_csv = pd.read_csv('.\\Exercise Files\\Names.csv', header=None)
print()
print(df_csv)  # <-- headers will be just the integer values
print()
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Salary']
df_csv.to_excel('.\\Exercise Files\\modified.xlsx')  # <-- saving the data to excel, it will have indices and headers
print()

""" *   indices are present, but the data is acting as singular column this is because our word document is 
    *   formatted in such a way that tabs separate each column
    *
    *   so to format this, we can specify the delimiter as tabs
    * """
print(df_txt)
df_text = pd.read_csv('.\\Exercise Files\\data.txt', delimiter='\t')
print()
print(df_text)
