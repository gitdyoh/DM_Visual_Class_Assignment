#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:56:39 2020

@author: ggonecrane
"""

import pandas as pd
import numpy

g_raceCode1 = {1: 'White', 2:'Black', 3: 'Other', 4: 'Hispanic', 5: 'Mixed'}

g_incomeCode1 = {1: '<5K', 2:'5K-7.5K', 3: '7.5K-10K', 4: '10K-12.5K', 
                  5: '12.5K-15K', 6:'15K-20K', 7:'20K-25K', 8:'25K-30K',
                  9: '30K-35K', 10:'35K-40K', 11:'40K-50K', 12:'50K-60K',
                  13: '60K-75K', 14:'75K-85K', 15:'85K-100K', 16:'100K-125K',
                  17: '125K-150K', 18:'150K-175K', 19:'>175K'}

g_difficultyCode1 = {1: 'Very Hard', 2:'Somewhat Hard', 3: 'Somewhat Easy', 4: 'Very Easy'}

def printTableLabel(label):
    print('\n')
    print('-------------------------------------------------------------------------------------')
    print(f'\t\t\t\t{label}')
    print('-------------------------------------------------------------------------------------')
    
def printEthnicityTable(data, decimal_value=True, original_key=False):
    raceCode1 = g_raceCode1
    
    for index, value in data.iteritems():
        key = index if original_key==True else raceCode1[index]  
        value_formatted = value if decimal_value==True else round(value * 100, 3)
        print('{: <10} {: >5}'.format(key, value_formatted))
        
        
def printDataframe(df, decimal_value=True, original_key=False):
    incomeCode1 = g_incomeCode1
    
#    sortedByIndex = data.sort_index()
    for index, row in df.iterrows():
        if type(index) == type(0):
            if original_key==True:
                key = f'{int(index)} ({incomeCode1[index]})' 
            else: 
                key = incomeCode1[index] 
                value_formatted = value if decimal_value==True else round(value * 100, 3)
            print(f'{key: <15} {value_formatted}')

        else:
            print(f'{row}\n')
            continue
        # print('{: <10} {: >10}'.format(key, value_formatted))

def printIncomeTable(data, decimal_value=True, original_key=False):
    incomeCode1 = g_incomeCode1
    
#    sortedByIndex = data.sort_index()
    for index, value in data.iteritems():
        if original_key==True:
            key = f'{int(index)} ({incomeCode1[index]})' 
        else: 
            key = incomeCode1[index] 
        value_formatted = value if decimal_value==True else round(value * 100, 3)
        # print('{: <10} {: >10}'.format(key, value_formatted))
        print(f'{key: <15} {value_formatted}')
        
pd.set_option('display.float_format', lambda x:'%f'%x)

# load Outlook Life data set
data = pd.read_csv('OutlookLife.csv', low_memory=False)

df = pd.DataFrame(data)

# map table names to user friendly variable names
race_col = 'PPETHM'
income_col = 'W1_P20'
wealthy_col = 'W1_F4_D'

printTableLabel('Personal Annual Income range')
# replace invalid input to NaN
df[income_col] = df[income_col].replace(-1,numpy.nan)
income_countsT = df[income_col].value_counts().sort_index()
income_percT = df[income_col].value_counts(normalize=True).sort_index()
df2 =  income_countsT.to_frame()
print(f'median: {df2.median()}')
df2['income_percentage'] = income_percT.apply(lambda x: '{:.2f}'.format(round(x * 100, 2)))
df2['cum_sum'] = income_countsT.cumsum()
df2['cum_perc'] = income_percT.cumsum().apply(lambda x: '{:.2f}'.format(round(x * 100, 2)))
df2.index = g_incomeCode1.values()
df2.columns = ['Frequency', 'Percentage(%)', 'Cumulative Frequency', 'Cumulative Percentage(%)']
print(df2)
df2.to_csv('df2.csv', index=True, header=True)

printTableLabel('Race / Ethnicity')
# replace invalid input to NaN
replace_vals = {-1:numpy.nan, -2:numpy.nan}
df[race_col] = df[race_col].replace(replace_vals)
race_countsT = df[race_col].value_counts().sort_index()
race_percT = df[race_col].value_counts(normalize=True).sort_index()
race_df =  race_countsT.to_frame()
race_df['race_percentage'] = race_percT.apply(lambda x: '{:.2f}'.format(round(x * 100, 2)))
race_df['cum_sum'] = race_countsT.cumsum()
race_df['cum_perc'] = race_percT.cumsum().apply(lambda x: '{:.2f}'.format(round(x * 100, 2)))
race_df.index = g_raceCode1.values()
race_df.columns = ['Frequency', 'Percentage(%)', 'Cumulative Frequency', 'Cumulative Percentage(%)']
print(race_df)
race_df.to_csv('race_df.csv', index=True, header=True)

printTableLabel('Difficulty in Reaching Goal to Become Wealthy')
# replace invalid input (-1 as refused) to NaN
df[wealthy_col] = df[wealthy_col].replace(-1,numpy.nan)
difficulty_countsT = df[wealthy_col].value_counts()
difficulty_percT = df[wealthy_col].value_counts(normalize=True)
df3 =  difficulty_countsT.to_frame()
df3['diff_percentage'] = difficulty_percT.apply(lambda x: '{:.2f}'.format(round(x * 100, 2)))
df3['cum_sum'] = difficulty_countsT.cumsum()
df3['cum_perc'] = difficulty_percT.cumsum().apply(lambda x: '{:.2f}'.format(round(x * 100, 2)))
df3.index = g_difficultyCode1.values()
df3.columns = ['Frequency', 'Percentage(%)', 'Cumulative Frequency', 'Cumulative Percentage(%)']
print(df3)
df3.to_csv('df3.csv', index=True, header=True)
