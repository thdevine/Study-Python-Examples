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

#%% 
#...Q2
existing_ids = [15234, 20485, 34536, 95342, 94857]
names = ['Calvin', 'Jason', 'Cindy', 'Kevin']
urls = [  'domain.com/resume/15234', 'domain.com/resume/23645','domain.com/resume/64337', 'domain.com/resume/34536']
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
#%%
#...Q3
def moving_window(inpt, v):
    moving_avg=[]
    i=0
    while i <= len(inpt)-1:
        if i <= v-1 :
            if i==0:
                curr = inpt[0]
                avg = curr
            else:            
                curr = inpt[0:i+1]
                avg = sum(curr)/(len(curr))
        else: 
            curr = inpt[i-v+1:i+1]
            avg = sum(curr)/v
        moving_avg.append(avg)
        i += 1
    return moving_avg 
# moving_window(input1, val) -> [1, 1.5, 2, 3, 4, 5]
# moving_window(input2, val2) -> [1, 1.5, 2, 2.5, 3.5, 4.5]
print(moving_window(inpt=[1,2,3,4,5,6],v=3))
print(moving_window(inpt=[1,2,3,4,5,6],v=4))
#%%
#...Q4
    # Let's say you have to draw two cards from a shuffled deck, one at a time.
    # What's the probability that the second card is not an Ace?
    # MY NOTES:
    #  p(draw 1 is ace) = 4/52
    #  p(draw 1 is NOT ace) = 1-4/52
    # thus, if draw 1 IS ACE then for draw 2 the non-ace proportion of 48/51 whereas if draw 1 IS NOT ACE then for draw 2 the non-ace proportion is 47/51; thus,
    #  p(draw 2 is NOT ace) = p(draw 2 is NOT ace|draw 1 is ace) + p(draw 2 is not ace|draw 1 is not ace)
    #  p(draw 2 is NOT ace) = 4/52*48/51 + 48/52 * 47/51
print(4/52*48/51 + 48/52 * 47/51, "is the probability of the second draw being a non-ace")

#%%
#...Q5
    # Write a function that can take in a word (string) and return a dictionary of n-gram count.
    # Example 1: string = 'banana', n=2, output = {'ba':1, 'an':2, 'na':2} 
    # Example 2: string = 'banana', n=3, output = {'ban':1, 'ana':2, 'nan':1}
#MY NOTES:
#       I had the most concise answer of all submissions
def ngram(s,n): #string, value; a key-value pair
    grams = {}
    for i in range(0,len(s)-n+1): 
        x=s[0+i:i+n]   #define the current string
        if x not in grams: #initiate key,value in dict if not there already
            grams[x] = 1
        else:              #if key is in dict increment value
            grams[x] +=1   
    return grams
print(ngram(s="banana",n=2))
print(ngram(s="banana",n=3))

# %%
#...Q6
# Given a list of stop words, write a function that takes a string and returns a string stripped of the stop words. Output: stripped_paragraph = 'want figure out how can better data scientist'
paragraph = 'I want to figure out how I can be a better data scientist'
def rm_stopwards(par):
 stopwords = ['I', 'as', 'to', 'you', 'your','but','be', 'a']
 osss = list(dict.fromkeys(par.split(' '))) # ordered_split_shortened_set
 x = list(osss)
 for word in osss:
    if word.strip() in stopwords:
        x.remove(word)
 ret = ' '.join(x)
 return ret
print("stripped_paragraph = "+"'"+(rm_stopwards(paragraph))+"'")
#DIFFERENT APPROACH
paragraph = 'I want to figure out how I can be a better data scientist'
def rm_stopwards(par):
    stopwords = ['I', 'as', 'to', 'you', 'your','but','be', 'a']
    filtered = ' '.join([word for word in paragraph.split() if word not in stopwords])
    return filtered
print("stripped_paragraph = "+"'"+(rm_stopwards(paragraph))+"'")

# %%
