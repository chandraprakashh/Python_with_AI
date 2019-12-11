# -*- coding: utf-8 -*-
"""
Created on mon Dec  9 09:17:43 2019

@author: BSDU ADMIN
"""
import pandas as pd


file = pd.read_csv('Ratings.csv', names=['movie_id', 'rating', 'numvotes'])
print(file)

data = pd.read_csv('Moviename.csv', engine='python',  names=['movie_id', 'movie_name'])
print(data)

e = file.copy().loc[file['numvotes']>=200 ]
#print(e)


d= pd.merge(e, data , on='movie_id')
print(d)
c=file['rating'].mean()
print(c)

def weighted_rating(x, c=c, m=200):
   
    v=x['numvotes']
    r=x['rating']
    return (v/(v+m)*r)+(m/(v+m) *c)

d['score']= d.apply(weighted_rating, axis=1)
d= d.sort_values('score',ascending = False)
print(d)
f= d[['movie_name', 'movie_id','rating', 'score']]
print(f)

e=d[['score']]
print(e)


from sklearn.metrics.pairwise import linear_kernel
cos_sim = linear_kernel(e,e)
#print(cos_sim)


indices = pd.Series(d.index, index=d['movie_name']).drop_duplicates()
#print(indices)

def get_recommendations(index, cos_sim= cos_sim):
   
    idx= indices[index]
    sim_scores = list(enumerate(cos_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    print( d['movie_name'].iloc[movie_indices])

   
get_recommendations('Post No Bills')