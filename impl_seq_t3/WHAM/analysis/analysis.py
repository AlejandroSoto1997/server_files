#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:13:05 2024

@author: alejandrosoto
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#matplotlib inline

data_set = []

for i in range(1,6):
    data = np.array(pd.read_fwf(f'../ENERGY{i}/energy.dat',header = None)[[5,6,7]])[1000:]
    keys = -data[:,1]+data[:,0]
    weights = data[:,2]
    data_set.append([keys,weights])
    
f,ax = plt.subplots(5,1,figsize = (3,9),sharex = True)
for i in range(5):
    ax[i].plot(data_set[i][0])
    
f,ax = plt.subplots(5,1,figsize = (3,9),sharex = True)
for i in range(5):
    ax[i].hist(data_set[i][0],bins = [-3.5,-2.5,-1.5,-0.5,0.5,1.5,2.5,3.5,4.5])
_=ax[-1].set_xlabel('state')
_=ax[2].set_ylabel('visits')

probs = []

f,ax = plt.subplots(5,1,figsize = (3,9))
for i in range(5):
    probs.append(ax[i].hist(data_set[i][0],bins = [-3.5,-2.5,-1.5,-0.5,0.5,1.5,2.5,3.5,4.5],weights = 1/data_set[i][1])[0])
    
normed = []

for i in probs:
    plt.plot(i/sum(i))
    normed.append(i/sum(i))

1/np.mean(normed,axis = 0)