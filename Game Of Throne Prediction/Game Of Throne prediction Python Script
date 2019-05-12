# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:15:22 2019

@author: binxi
"""

import pandas as pd
import numpy as np

file = 'GOT_character_predictions.xlsx'

got_df = pd.read_excel(file)

#Overview of dataset
got_df.head()

got_df.shape

got_df.isnull().sum()


# house,title,culture var convert to binary

got_df['house']=got_df['house'].str.lower()

got_df['culture']=got_df['culture'].str.lower()

got_df['title']=got_df['title'].str.lower()

got_df[['house','culture','title']] = got_df[['house','culture','title']].fillna('na')

size_cut = 5

house_size = got_df.groupby('house').nunique()['name'].sort_values(ascending = False)

title_size = got_df.groupby('title').nunique()['name'].sort_values(ascending = False)

culture_size = got_df.groupby('culture').nunique()['name'].sort_values(ascending = False)

pop_house = house_size[house_size>= size_cut].index.tolist()

pop_title = title_size[title_size>= size_cut].index.tolist()

pop_culture = culture_size[culture_size>= size_cut].index.tolist()

for house in pop_house:
    got_df['bi_house_'+house]=(got_df['house']==house)

for title in pop_title:
    got_df['bi_title_'+title]=(got_df['title']==title)

for culture in pop_culture:
    got_df['bi_culture_'+culture]=(got_df['culture']==culture)

#
to_del = got_df.isnull().any()[got_df.isnull().any()].index.tolist()

for i in to_del:
    del(got_df[i])

#correlation dectect    
got_corr = got_df.corr().round(2)

Alive_cor = abs(got_corr.loc['isAlive']).sort_values(ascending = False)

#Select significant variables and delete meaningless variables

min_cor = 0.17

selected_var = Alive_cor[Alive_cor >= min_cor].index.tolist()

got_df_selected = got_df[selected_var]

meaningless_var = ['S.No','death','dateOfBirth']

for i in meaningless_var:

    if i in selected_var:
        selected_var.remove(i)
        del(got_df_selected[i])

#run random forest classification

y = got_df_selected['isAlive'].values

x = got_df_selected[selected_var[1:]].values

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

full_forest_entropy = \
    RandomForestClassifier(n_estimators = 500,criterion = \
                           'entropy',max_depth = None,min_samples_leaf = 15,\
                           bootstrap = True,warm_start = False,random_state = 508)

cv_scores = cross_val_score(full_forest_entropy,x,y,cv=3,scoring='roc_auc')

print(got_corr.loc[selected_var,'isAlive'].sort_values(ascending = False))

print(np.mean(cv_scores).round(3))

# follow all 5 recommendations vs others

filt = (got_df['book4_A_Feast_For_Crows']==1) \
    & (got_df['bi_house_house targaryen']==0) \
    & (got_df['popularity'] < got_df['popularity'].median()) \
    & (got_df['numDeadRelations'] <= got_df['numDeadRelations'].median()) \
    & (got_df['bi_culture_valyrian'] ==0)

got_df['filt'] = filt

print(got_df.groupby(['filt','isAlive']).nunique()['name'])


# run regression and prediction based on test_size and random_state given and output result

from sklearn.model_selection import train_test_split

X = got_df_selected[selected_var[1:]]

Y = got_df_selected['isAlive']

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.1, random_state=508)

full_forest_entropy = \
    RandomForestClassifier(n_estimators = 500,criterion = \
                           'entropy',max_depth = None,min_samples_leaf = 15,\
                           bootstrap = True,warm_start = False,random_state = 508)

full_forest_entropy.fit(X_train,y_train)

y_pred = full_forest_entropy.predict(X_test)

output = pd.DataFrame()

output['prediction'] = y_pred

output['actual'] = y_test.values


output.to_excel('prediction vs actual.xlsx')



