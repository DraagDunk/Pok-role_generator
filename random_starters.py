# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 00:16:31 2021

@author: Jesper
"""

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import requests

dex_name = "DanmarkDex"
dex = np.array(pd.read_csv("../"+dex_name+".txt", header=None, skiprows=1, sep="\t+", engine="python"))

num  = dex[:,0].astype("int")
name = dex[:,1].astype("str")
type1= dex[:,2].astype("str")
type2= dex[:,3].astype("str")
rare = dex[:,4].astype("str")

start_ind = np.random.choice(np.where(rare == "C")[0], size=10)

for i in start_ind:
    print(name[i])