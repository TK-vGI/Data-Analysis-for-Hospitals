import pandas as pd

pd.set_option('display.max_columns', 8)

"""
1/5: Uploading data
"""
dfGeneral = pd.read_csv('test/general.csv')
dfPrenatal = pd.read_csv('test/prenatal.csv')
dfSports = pd.read_csv('test/sports.csv')

print(dfGeneral.head(20))
print(dfPrenatal.head(20))
print(dfSports.head(20))