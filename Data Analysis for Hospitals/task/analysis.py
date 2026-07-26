import pandas as pd
import matplotlib.pyplot as plt

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
columns = list(dfGeneral.columns.values)  # creating 'columns' names list from General
dfPrenatal.columns = columns
dfSports.columns = columns

dfMerged = pd.concat([dfGeneral, dfPrenatal, dfSports], ignore_index=True)
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

dfMerged.dropna(axis=0, how='all', inplace=True)  # 1

dfMerged["gender"] = (dfMerged["gender"]
                      .str.lower()
                      .str.strip()
                      .replace({'male': 'm', 'man': 'm', 'female': 'f', 'woman': 'f'})
                      )  # 2

dfMerged['gender'] = dfMerged.apply(lambda row: 'f' if row['hospital'] == 'prenatal' else row['gender'], axis=1)  # 3

cols = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
dfMerged[cols] = dfMerged[cols].fillna(0)  # 4

# print('Data shape:', dfMerged.shape) # 5

# print(dfMerged.sample(n=20, random_state=30))

"""
4/5: Statistics, Selecting, pivot_table() and aggregating
    1.,2.,3,4. searching in merged dataframe
    5. create pivot table from merged dataframe and aggregate()
"""
answer_1 = dfMerged['hospital'].value_counts().idxmax()

answer_2 = dfMerged.loc[(dfMerged['hospital'] == 'general') & (dfMerged['diagnosis'] == 'stomach')].shape[0] / \
           dfMerged.loc[dfMerged['hospital'] == 'general'].shape[0]
answer_2 = round(answer_2, 3)

answer_3 = dfMerged.loc[(dfMerged['hospital'] == 'sports') & (dfMerged['diagnosis'] == 'dislocation')].shape[0] / \
           dfMerged.loc[dfMerged['hospital'] == 'sports'].shape[0]
answer_3 = round(answer_3, 3)

medians = dfMerged.groupby('hospital')['age'].median()
answer_4 = int(medians['general'] - medians['sports'])

df_t = dfMerged[dfMerged['blood_test'] == 't']  # Count only rows where blood_test == 't'
pivot = pd.pivot_table(df_t, index='hospital', values='blood_test', aggfunc='count',
                       fill_value=0)  # Pivot table to count tests per hospital
answer_5 = pivot['blood_test'].idxmax()  # Find the hospital with the most tests - max_hospital
answer_6 = pivot['blood_test'].max()  # Find the hospital with the most tests - max_count

# print(f'The answer to the 1st question is {answer_1}')
# print(f'The answer to the 2nd question is {answer_2}')
# print(f'The answer to the 3rd question is {answer_3}')
# print(f'The answer to the 4th question is {answer_4}')
# print(f'The answer to the 5th question is {answer_5}, {answer_6} blood tests')

"""
5/5: Visualizing with graphs and plots
    1. histogram with matplotlib | seaborn
    2. pie-chart with matplotlib | pandas
    3. "violin" plot with ?
    4. create also output with answers
"""

# 1. Most common age of a patient among all hospitals
bins = [0, 15, 35, 55, 70, 80]
labels = ['0-15', '15-35', '35-55', '55-70', '70-80']

dfMerged['age_bin'] = pd.cut(dfMerged['age'], bins=bins, labels=labels, right=False)
# print(dfMerged['age_bin'].value_counts().idxmax())

answer_7 = dfMerged['age_bin'].value_counts().idxmax()

data = dfMerged['age'].values
data = [int(x) for x in data]

plt.title("Most common age of a patient among all hospitals")
plt.xlabel("Age")
plt.ylabel("Number of people")
plt.hist(data, bins=bins, color="blue", edgecolor="white")
plt.show()

# 2. Most common diagnosis among all hospitals
answer_8 = dfMerged['diagnosis'].value_counts().idxmax()

data8 = dfMerged['diagnosis'].value_counts()

labels = data8.index.astype(str)
diag_data = data8.values

plt.title("Most common diagnosis among all hospitals", fontsize=14)
plt.pie(
    diag_data,
    autopct='%1.1f%%',
    pctdistance=0.6,
    shadow=True,
    startangle=90
)
plt.legend(labels, loc='right', bbox_to_anchor=(1.3, 0.5), fontsize=10)
plt.show()

# 3. Height distribution in hospitals - violin plot
bb = dfMerged[['hospital', 'height']]

hospitals = bb['hospital'].unique().tolist()
data_list = [bb.loc[bb['hospital'] == h, 'height'] for h in hospitals]

fig, axes = plt.subplots()
axes.set_xticks(range(1, len(hospitals) + 1))
axes.set_xticklabels(hospitals)
axes.set_ylabel("Height")
axes.set_title('Height distribution in hospitals')

plt.violinplot(data_list, showmeans=False, showmedians=False)

plt.show()

print(f'The answer to the 1st question: {answer_7}')
print(f'The answer to the 2nd question: {answer_8}')
print('The answer to the 3rd question: It\'s because different age group treated by respective hospitals and '
      ' different units used (cm/inches)')
