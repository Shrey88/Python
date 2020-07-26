""" *
    *   as we continue to work with dataframe in pandas we need more methods to organise, compare and sort our data
    * """
import pandas as pd


df = pd.read_csv('.\\Exercise Files\\Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code','Income']


""" *
    *   so let's start filtering data base on property
    *   so what if we want to filter the rows and column based on the single value in the column
    *
    *   say we want to filter data where people living only on Riverside.
    *
    *   the condition returns the a tuple containing the index value and boolean value(True/False)
    *   the index value is passed to the loc function to print the data that has returned True
    * """
print(df.loc[df['City']=='Riverside'])
print('=' * 20)
print()


""" *
    *   suppose you want to match the person's name who stays at Riverside.
    * """
print(df.loc[ (df['City']=='Riverside') & (df['First']=='John') ] )
print('=' * 20)
print()


""" *
    *   setting up new column Tax percentage
    * """
df['Tax %'] = df['Income'].apply(lambda x: .15 if 10000 < x < 40000 else .20 if 40000 < x < 80000 else .25)
print(df)
print('=' * 20)
print()


""" *
    *   we want to compute the tax they owe to pay based on the income and tax%
    * """
df['Taxes_Owed'] = df['Income'] * df['Tax %']
print(df)
print('=' * 20)
print()


""" *
    *   to drop columns
    * """
drop_columns = ['Area Code', 'First', 'Address']
df.drop(columns=drop_columns, inplace=True)
print(df)
print('=' * 20)
print()


""" *
    *   create a new column and fill in some false values
    *   the second parameter : we have mentioned the column for which we want to change here it is Test_Col
    * """
df['Test_Col'] = False  # <-- setting all the rows of this column to False

df.loc[df['Income'] < 60000, 'Test_Col'] = True
print(df)
print('=' * 20)
print()


""" *
    *   Groupby
    *
    *   we need to specify on which column you want to groupby and we are also using the math function to get the mean
    *   value
    * """

print(df.groupby(['Test_Col']).mean())
print('=' * 20)
print()


""" *
    *   Sort Function
    *
    *   sort function can order the data based on the column you specify
    *   sort_values is a function of dataframe and here you won't get the intellisense since you are using the math 
    *   function and applying the sort_values on the dataframe objects returned by the mean function
    *   you can set the order of ascending as True or False.
    * """
print(df.groupby(['Test_Col']).mean().sort_values('Income'))
print('=' * 20)
print()