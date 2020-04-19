# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:06:28 2019

@author: idont
"""

import pandas as pd
import numpy as np
import random

print ("BY GENERATING THE RANDOM NUMBERS:")
print ("*********************************")
data=[i for i in range(20)]
best=random.sample(range(0,20),10)
best.sort()
worst=[i for i in data if i not in best]
print ("Data:", data)
print ("Best:",best)
print ("Worst:",worst)

print ("\nBY USING THE DATA SET:")
print ("**********************")

#1: read dataset into pandas from data frames
filename = 'diabetes.csv'
result= pd.read_csv(filename)

#2 : read n create list of all features
list_all = list(result.columns.values)
print("LIST:",list_all)

#3 : define best features list
random_best_list = random.sample(range(0, 8), 4)
random_best_list.sort()
best_columns = list(result.columns[random_best_list])
print("BEST:",best_columns)

#4 : define worst features list
worst_columns = [i for i in list_all if i not in best_columns]
print("WORST:",worst_columns)