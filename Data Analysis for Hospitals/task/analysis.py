import pandas as pd

pd.set_option('display.max_columns', 8)

"""
1/5: Uploading data
    1. read data from csv file to dataframe from General (G), Prenatal (P), Sports (S)
    2. print first 20 rows for each G, P, S respectively
"""
dfGeneral = pd.read_csv('test/general.csv')
dfPrenatal = pd.read_csv('test/prenatal.csv')
dfSports = pd.read_csv('test/sports.csv')

# print(dfGeneral.head(20))
# print(dfPrenatal.head(20))
# print(dfSports.head(20))

"""
2/5: Merging dataframes, modifying columns`names, drop column
    1. unify columns in Prenatal, Sports with General table
    2. merge in order G+P+S 
    3. drop 'Unnamed: 0' column
    4. print random 20 rows of merged dataframe
"""
columns = list(dfGeneral.columns.values) # creating 'columns' names list from General
dfPrenatal.columns = columns
dfSports.columns = columns

dfMerged = pd.concat([dfGeneral,dfPrenatal,dfSports],ignore_index=True)
# print(dfMerged.columns.values)
dfMerged.drop('Unnamed: 0', axis=1, inplace=True)
# print(dfMerged.head(20))
# print(dfMerged.sample(n=20, random_state=30))

"""
3/5: Removing NaN values
    1. delete empty rows
    2. unify gender values to f/m, replace NaN to f in the Prenatal hospital
    3. replace NaN with 0s for rest of the columns
    4. print final dataframe shape
    5. print random 20 rows
"""
# dfMerged.isnull().sum() # helps with identifying NaN rows, columns in table

dfMerged.dropna(axis=0, how='all', inplace=True) # 1

dfMerged["gender"] = (dfMerged["gender"]
                      .str.lower()
                      .str.strip()
                      .replace({'male': 'm','man': 'm','female': 'f','woman': 'f'})
                      ) # 2

dfMerged['gender'] = dfMerged.apply(lambda row: 'f' if row['hospital'] == 'prenatal' else row['gender'], axis=1) # 3

cols = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
dfMerged[cols] = dfMerged[cols].fillna(0) # 4

print('Data shape:', dfMerged.shape) # 5

print(dfMerged.sample(n=20, random_state=30))