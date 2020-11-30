#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 06:58:15 2020

@author: ggonecrane
"""

import pandas as pd
import numpy
import seaborn
import matplotlib.pyplot as plt

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
        
        
def generateTupleList(series, additional_col, decimal_value=True):
    alist = []
    for index, value in series.iteritems():
        value_formatted = value if decimal_value==True else round(value * 100, 3)
        atuple = (index, additional_col, value_formatted)
        alist.append(atuple)
        
    return alist

def assignment2():
    income_countsT = df[income_col].value_counts().sort_index()
    income_countsT.index = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    income_percT = df[income_col].value_counts(normalize=True).sort_index()
    df2 =  income_countsT.to_frame()
    
    df2['income_percentage'] = income_percT.apply(lambda x: round(x * 100, 2))
    df2['cum_sum'] = income_countsT.cumsum()
    df2['cum_perc'] = income_percT.cumsum().apply(lambda x: round(x * 100, 2))
    df2.index = g_incomeCode1.values()
    df2.columns = ['Frequency', 'Percentage(%)', 'Cumulative Frequency', 'Cumulative Percentage(%)']
    print(df2)
    df2.to_csv('df2.csv', index=True, header=True)
    
    # printTableLabel('Race / Ethnicity')
    # replace invalid input to NaN
    replace_vals = {-1:numpy.nan, -2:numpy.nan}
    df[race_col] = df[race_col].replace(replace_vals)
    race_countsT = df[race_col].value_counts().sort_index()
    race_percT = df[race_col].value_counts(normalize=True).sort_index()
    race_df =  race_countsT.to_frame()
    race_df['race_percentage'] = race_percT.apply(lambda x: round(x * 100, 2))
    race_df['cum_sum'] = race_countsT.cumsum()
    race_df['cum_perc'] = race_percT.cumsum().apply(lambda x: round(x * 100, 2))
    race_df.index = g_raceCode1.values()
    race_df.columns = ['Frequency', 'Percentage(%)', 'Cumulative Frequency', 'Cumulative Percentage(%)']
    print(race_df)
    race_df.to_csv('race_df.csv', index=True, header=True)
    
    #printTableLabel('Difficulty in Reaching Goal to Become Wealthy')
    # replace invalid input (-1 as refused) to NaN
    df[wealthy_col] = df[wealthy_col].replace(-1,numpy.nan)
    difficulty_countsT = df[wealthy_col].value_counts()
    difficulty_percT = df[wealthy_col].value_counts(normalize=True)
    df3 =  difficulty_countsT.to_frame()
    df3['diff_percentage'] = difficulty_percT.apply(lambda x: round(x * 100, 2))
    df3['cum_sum'] = difficulty_countsT.cumsum()
    df3['cum_perc'] = difficulty_percT.cumsum().apply(lambda x: round(x * 100, 2))
    df3.index = g_difficultyCode1.values()
    df3.columns = ['Frequency', 'Percentage(%)', 'Cumulative Frequency', 'Cumulative Percentage(%)']
    print(df3)
    df3.to_csv('df3.csv', index=True, header=True)
    
pd.set_option('display.float_format', lambda x:'%f'%x)

# load Outlook Life data set
data = pd.read_csv('OutlookLife.csv', low_memory=False)

df = pd.DataFrame(data)

# map table names to user friendly variable names
race_col = 'PPETHM'
income_col = 'W1_P20'
wealthy_col = 'W1_F4_D'

# printTableLabel('Personal Annual Income range')
# replace invalid input to NaN
df[income_col] = df[income_col].replace(-1,numpy.nan)

# previousAssignments()

approx_income = {1: 2500, 2: 6250, 3: 8750, 4: 11250, 5: 13750, 6: 17500, 7: 22500,
                 8: 27500, 9:32500, 10: 37500, 11: 45000, 12: 55000, 13: 67500, 14: 80000,
                 15: 92500, 16: 112500, 17: 137500, 18: 162500, 19: 200000}

frq_white_col = 'Freq. (White)'
frq_black_col = 'Freq. (Black)'
perc_white_col = 'Perc.(%) (White)'
perc_black_col = 'Perc.(%) (Black)'

# Income Category vs. Income Range Map
income_countsT = df[income_col].value_counts().sort_index()
income_countsT.index = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
inc_map_c = list(zip(income_countsT.index, g_incomeCode1.values(), approx_income.values()))

inc_map = pd.DataFrame(inc_map_c, columns = ['Category(W1_P20)', 'Income Range', 'Approx. Value ($)'])
printTableLabel('Income Category Mapped to Range and Approx. Value')
print(inc_map )
inc_map.to_csv('Income Map.csv', index=True, header=True)

wb_df = df[(df[race_col]==1) | (df[race_col]==2)].copy()
wb_df['median_div'] = wb_df[income_col].apply(lambda x: 1 if x > 8 else 0)

# Managed Variable 1 (ANNINC_IN_QUAT) for White
w_df = wb_df.groupby(race_col).get_group(1).copy()
w_df['income_quar'] = pd.qcut(w_df[income_col], 4, labels=["25%tile","50%tile","75%tile","100%tile"])
w_df['median_div'] = w_df[income_col].apply(lambda x: 1 if x > 8 else 0)
w_df[wealthy_col] = w_df[wealthy_col].replace(-1,numpy.nan)

ANNINC_IN_QUAT = pd.DataFrame()
ANNINC_IN_QUAT[frq_white_col] = w_df['income_quar'].value_counts(sort=False, dropna=True)
ANNINC_IN_QUAT[perc_white_col] = w_df['income_quar'].value_counts(sort=False, dropna=True, normalize=True).apply(lambda x: round(x * 100, 2))

# Managed Variable 1 (ANNINC_IN_QUAT) for Black
b_df = wb_df.groupby(race_col).get_group(2).copy()
b_df['income_quar']=pd.qcut(b_df[income_col], 4, labels=["25%tile","50%tile","75%tile","100%tile"])
b_df['median_div'] = b_df[income_col].apply(lambda x: 1 if x > 8 else 0)
b_df[wealthy_col] = b_df[wealthy_col].replace(-1,numpy.nan)

ANNINC_IN_QUAT[frq_black_col] = b_df['income_quar'].value_counts(sort=False, dropna=True)
ANNINC_IN_QUAT[perc_black_col] = b_df['income_quar'].value_counts(sort=False, dropna=True, normalize=True).apply(lambda x: round(x * 100, 2))

# Managed Variable 1 (ANNINC_IN_QUAT) - Rename Columns for Printing
ANNINC_IN_QUAT.columns = [frq_white_col, perc_white_col, frq_black_col, perc_black_col]

printTableLabel ('Income Quartiles by Race (ANNINC_IN_QUAT)')
print(f'{ANNINC_IN_QUAT}')
ANNINC_IN_QUAT.to_csv('ANNINC_IN_QUAT.csv', index=True, header=True)

# Managed Variable 2 - MEDINC_BY_RACE
# subset data to 2 races (African American and White)

median_inc_cat = int(df[income_col].median())
median_inc_val = g_incomeCode1[median_inc_cat]

# Managed Variable 2 (INCLEVEL_BI_MEDIAN) for White
median_inc_cat_w = int(w_df[income_col].median())
median_inc_val_w = g_incomeCode1[median_inc_cat_w]

# Managed Variable 2 (INCLEVEL_BI_MEDIAN) for Black
median_inc_cat_f = int(b_df[income_col].median())
median_inc_val_f = g_incomeCode1[median_inc_cat_f]


MEDINC_BY_RACE = pd.DataFrame({'M-Income Cat.': [median_inc_cat_w, median_inc_cat_f], 
                            'M-Income Range': [median_inc_val_w, median_inc_val_f],
                            'M-Income Approx.': [approx_income[median_inc_cat_w], approx_income[median_inc_cat_f]],
                            'Race Code': [1, 2]}, 
                           index = ['White', 'Black'])

printTableLabel ('Median Income Range by Race (MEDINC_BY_RACE)')
print(f'{MEDINC_BY_RACE}')
MEDINC_BY_RACE.to_csv('MEDINC_BY_RACE.csv', index=True, header=True)


# Managed Variable 3 - INCLEVEL_BI_MEDIAN 
df['median_div'] = df[income_col].apply(lambda x: 1 if x > 8 else 0)
df_med = df['median_div'].value_counts()

INCLEVEL_BI_MEDIAN = pd.DataFrame()

# Managed Variable 3 (INCLEVEL_BI_MEDIAN) for White
INCLEVEL_BI_MEDIAN[frq_white_col] = w_df['median_div'].value_counts()
INCLEVEL_BI_MEDIAN[perc_white_col] = w_df['median_div'].value_counts(normalize=True).apply(lambda x: round(x * 100, 2))

# Managed Variable 3 (INCLEVEL_BI_MEDIAN) for Black
INCLEVEL_BI_MEDIAN[frq_black_col] = b_df['median_div'].value_counts()
INCLEVEL_BI_MEDIAN[perc_black_col] = b_df['median_div'].value_counts(normalize=True).apply(lambda x: round(x * 100, 2))

# Managed Variable 3 (INCLEVEL_BI_MEDIAN) - Rename Columns for Printing
INCLEVEL_BI_MEDIAN.columns = [frq_white_col, perc_white_col, frq_black_col, perc_black_col]
INCLEVEL_BI_MEDIAN = INCLEVEL_BI_MEDIAN.sort_index()
INCLEVEL_BI_MEDIAN.index = ['Below Median', 'Above Median']
printTableLabel('Income Level against Media Income (INCLEVEL_BI_MEDIAN)')
print(INCLEVEL_BI_MEDIAN)
INCLEVEL_BI_MEDIAN.to_csv('INCLEVEL_BI_MEDIAN.csv', index=True, header=True)

DIFFICULTY_WEALTH = pd.DataFrame()

# replace invalid input (-1 as refused) to NaN
DIFFICULTY_WEALTH[frq_white_col] =  w_df[wealthy_col].value_counts()
DIFFICULTY_WEALTH[perc_white_col] = w_df[wealthy_col].value_counts(normalize=True).apply(lambda x: round(x * 100, 2))

# Difficulty by White in Reaching Goal to Become Wealthy by White
DIFFICULTY_WEALTH[frq_black_col] = b_df[wealthy_col].value_counts()
DIFFICULTY_WEALTH[perc_black_col] = b_df[wealthy_col].value_counts(normalize=True).apply(lambda x: round(x * 100, 2))

DIFFICULTY_WEALTH.columns = [frq_white_col, perc_white_col, frq_black_col, perc_black_col]
DIFFICULTY_WEALTH.index = g_difficultyCode1.values()

printTableLabel('Difficulty felt with Becoming Wealthy (DIFFICULTY_WEALTH)')
print(DIFFICULTY_WEALTH)
DIFFICULTY_WEALTH.to_csv('DIFFICULTY_WEALTH.csv', index=True, header=True)

