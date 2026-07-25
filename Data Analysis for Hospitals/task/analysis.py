import pandas as pd

pd.set_option('display.max_columns', 8)

"""
1/5: Uploading data
"""
dfGeneral = pd.read_csv('test/general.csv')
dfPrenatal = pd.read_csv('test/prenatal.csv')
dfSports = pd.read_csv('test/sports.csv')

# print(dfGeneral.head(20))
# print(dfPrenatal.head(20))
# print(dfSports.head(20))

"""
2/5: Merging dataframes, modifying columns`names, drop column
"""
columns = list(dfGeneral.columns.values) # creating 'columns' names list from General
dfPrenatal.columns = columns
dfSports.columns = columns

dfMerged = pd.concat([dfGeneral,dfPrenatal,dfSports],ignore_index=True)
# print(dfMerged.columns.values)
dfMerged.drop('Unnamed: 0', axis=1, inplace=True)
# print(dfMerged.head(20))
print(dfMerged.sample(n=20, random_state=30))