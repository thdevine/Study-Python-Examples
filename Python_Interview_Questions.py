"""
Created on Thu Mar 25 15:07:41 2021
@author: Thomas Devine
@Description: The goal of this script is to track interview questions I've solved using python to demonstrate working knowledge of python.
        There is no overlap for the questions in the SQL_interview_queries.sql file in https://github.com/thdevine/Study---R-Sql---Analysis-Examples/tree/main/Code

        NOTE: until the examples become unreasonably complicated, I'll not comment portions of the script out.
"""
# HARD

#-----------------#-----------------#-----------------#-----------------
# MEDIUM

#-----------------#-----------------#-----------------#-----------------
# EASY
#%% pandas method, super easy
#...Q1 Given a list of user_ids and tips, find the user that tipped the most.
user_ids = [103, 105, 105, 107, 106, 103, 102, 108, 107, 103, 102];
tips = [2, 5, 1, 0, 2, 1, 1, 0, 0, 2, 2];
import pandas as pd
df = pd.DataFrame( {“userids” :userids, “tips” : tips,}, )
df.groupby(‘userids’).sum().sortvalues(‘tips’, ascending =False).head(1)
#...Q1 alternative method without importing a library, faster methods use libraries.
user_ids = [103, 105, 105, 107, 106, 103, 102, 108, 107, 103, 102] 
tips = [2, 5, 1, 0, 2, 1, 1, 0, 0, 2, 2]

dct = {} 
for i, v in enumerate(user_ids):
    if v in dct:
        dct[v] += tips[i]
    else:
        dct[v] = tips[i]
print("user_id:",max(dct,key=dct.get), "tips the most")
#-----------------
#%% 
#...Q2
existing_ids = [15234, 20485, 34536, 95342, 94857]
names = ['Calvin', 'Jason', 'Cindy', 'Kevin']
urls = [  'domain.com/resume/15234', 
        'domain.com/resume/23645', 
        'domain.com/resume/64337', 
        'domain.com/resume/34536',
]
dct = {}
for n in names:
    for i in urls:
        dct[n] = int(i.split('/')[2])
        urls.remove(i)
        break  
    if dct[n] in existing_ids:
        dct.pop(n)
    else:
        next
print(dct)