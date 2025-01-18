import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df1 = pd.read_csv('/Users/shanmukhamundra/Desktop/test/general.csv')
df2 = pd.read_csv('/Users/shanmukhamundra/Desktop/test/prenatal.csv')
df3 = pd.read_csv('/Users/shanmukhamundra/Desktop/test/sports.csv')
df2.rename(columns={'HOSPITAL': 'hospital', "Sex": "gender"}, inplace=True)
df2.loc[df2['gender'].isna(), 'gender']='f'
df3.rename(columns={'Hospital':'hospital', "Male/Female": "gender"}, inplace=True)
new_df = pd.concat([df1, df2, df3], ignore_index=True)
new_df.drop(columns=['Unnamed: 0', 'Male/female'], inplace=True)
df = new_df.dropna(axis=0, how='all')
#df['gender'] = df['gender'].replace({'man':'m', 'woman':'f'}, inplace=True)
df.loc[df['gender'] == 'woman', 'gender'] = 'f'
df.loc[df['gender']== 'man', 'gender'] = 'm'
df.loc[(df['hospital'].isna(), 'hospital')]= 'general'
df.loc[(df['gender'].isna(), 'gender')]= 'f'
df.loc[df['mri'].isna(), 'mri'] = 0
df.loc[df['diagnosis'].isna(), 'diagnosis'] = 0
df.loc[df['blood_test'].isna(), 'blood_test'] = 0
df.loc[df['ecg'].isna(), 'ecg'] = 0
df.loc[df['ultrasound'].isna(), 'ultrasound'] = 0
df.loc[df['mri'].isna(), 'mri'] = 0
df.loc[df['xray'].isna(), 'xray'] = 0
df.loc[df['children'].isna(), 'children'] = 0
df.loc[df['months'].isna(), 'months'] = 0
df = df
#data_shape = df.shape
#print(f'Data shape: {data_shape}')
#shuffled_df = df.sample(n=20, random_state=30)
#print(shuffled_df.head(2000))
#######*** Visualization Part ***######
df.plot(y='age', kind='hist', bins=5, alpha=0.8, color='red', edgecolor='white' )
#plt.show()
diagnosis_count = df['diagnosis'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(diagnosis_count, labels=diagnosis_count.index, autopct='%1.0f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Most Common Diagnosis among patients in all hospital")
plt.legend(loc='best')
#plt.show()
height_dist = df['height'].value_counts()
data_list = [height_dist]
fig, axes = plt.subplots()
sns.violinplot(data_list)
plt.show()
######*** Statistics Part ***######
df_count = df['hospital'].value_counts().idxmax()
print(f'The answer for the 1st question is {df_count}')
total_general = len(df.loc[(df['hospital']=='general')])
stomach_issue = len(df.loc[(df['hospital']=='general') & (df['diagnosis']=='stomach')])
stomach_problem = round(stomach_issue/total_general, 3)
print(f'The answer for the 2nd question is {stomach_problem}')
total_sports = len(df.loc[(df['hospital']=='sports')])
dislocation_issue = len(df.loc[(df['hospital']=='sports') & (df['diagnosis']=='dislocation')])
dislocation_problem = round(dislocation_issue/total_sports, 3)
print(f'The answer for the 3rd question is {dislocation_problem}')
general_hospital = df.loc[df['hospital']== 'general', 'age']
median_general = general_hospital.median()
sports_hospital = df.loc[df['hospital']== 'sports', 'age']
median_sports = sports_hospital.median()
difference = median_general - median_sports
print(f'The answer for the 4th question is {difference}')
blood_general = len(df.loc[(df['hospital']=='general') & (df['blood_test']=='t')])
blood_prenatal = len(df.loc[(df['hospital']=='prenatal') & (df['blood_test']=='t' )])
blood_sports = len(df.loc[(df['hospital']=='sports') & (df['blood_test']=='t')])
print(f'The answer for the 5th question is prenatal, {blood_prenatal} blood tests')