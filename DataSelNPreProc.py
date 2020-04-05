# -*- coding: utf-8 -*-
"""
1. Created on Sat Mar 28 22:15:01 2020
2. Added descriptive stats - 3/29/20  4PM

Name: DataSelNPrePrec.py
Course: 550 Massive Data Mining
Final Project 
Step 1: Data Seletion and Pre Processing

@author: Mani (Krishnamurthy Subramanian)
"""

import os
import pandas as pd
import numpy as np

os.chdir('U:\ML')
os.getcwd()
df = pd.read_json('./reviews_Movies_and_TV_5.json',lines=True,typ='frame')
dftemp = df.copy()
#
# random_state - Seed 101 used for random# generator
# Training set size 75% was suggested in the assignment
#
movie_review_train = dftemp(frac=0.75,random_state=101)
movie_review_test = dftemp.drop(movie_review_train.index)

# Write compressed training and test files
movie_review_train.to_csv('./movie_review_train.tsv.gz', sep='\t',
                          compression='infer')
movie_review_test.to_csv('./movie_review_test.tsv.gz', sep='\t',
                         compression='infer')

# stats to figure out row and column min, max, sparseness etc.
# by movie
x = df.groupby(['asin']).count()
x.describe()
# by reviewer
y = df.groupby(['reviewerID']).count()
y.describe()

# Get ratings histogram - it is very skewed to right
df['overall'].plot.hist()
