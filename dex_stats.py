# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:34:10 2021

@author: Jesper
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dex_name = "DanmarkDex"
dex = np.array(pd.read_csv("../"+dex_name+".txt", header=None, skiprows=1, sep="\t+", engine="python"))

num  = dex[:,0].astype("int")
name = dex[:,1].astype("str")
type1= dex[:,2].astype("str")
type2= dex[:,3].astype("str")
rare = dex[:,4].astype("str")

def rem_space(lst):
    for i in range(len(lst)):
        lst[i] = lst[i].replace(" ","")
    return lst
        
type1 = rem_space(type1)
type2 = rem_space(type2)

types = np.append(type1,type2)
none_i = np.where(types == "None")
types = np.delete(types, none_i)

def num_type(arr, typ):
    num = len(np.where(arr == typ)[0])
    return num

def count_types(arr):
    unique_types = np.unique(arr)
    unique_nums = np.array([])
    for i in range(len(unique_types)):
        num_i = len(np.where(arr == unique_types[i])[0])
        unique_nums = np.append(unique_nums, num_i)
    return unique_types, unique_nums

def count_r_types(type1, type2, rarity, wanted_rarity, out_types):
    indices = np.where(rarity == wanted_rarity)
    types = np.append(type1[indices], type2[indices])
    none_i = np.where(types == "None")
    types = np.delete(types, none_i)
    out_nums = np.zeros(len(out_types))
    for i in range(len(out_types)):
        out_nums[i] = len(np.where(types == out_types[i])[0])
    return out_nums
    

btypes, bnums = count_types(types)
    
cnums = count_r_types(type1, type2, rare, "C", btypes)
unums = count_r_types(type1, type2, rare, "U", btypes)
rnums = count_r_types(type1, type2, rare, "R", btypes)
mnums = count_r_types(type1, type2, rare, "M", btypes)

sort_ind = np.flipud(np.argsort(bnums))

plt.close('all')
plt.figure()
plt.title(dex_name + " Typefordeling")
plt.bar(range(len(btypes)), cnums[sort_ind], edgecolor="black", width=0.8, zorder=10, 
        label="Common")
plt.bar(range(len(btypes)), unums[sort_ind], edgecolor="black", width=0.8, zorder=10, 
        bottom=cnums[sort_ind], 
        label="Uncommon")
plt.bar(range(len(btypes)), rnums[sort_ind], edgecolor="black", width=0.8, zorder=10, 
        bottom=cnums[sort_ind]+unums[sort_ind], 
        label="Rare")
plt.bar(range(len(btypes)), mnums[sort_ind], edgecolor="black", width=0.8, zorder=10, 
        bottom=cnums[sort_ind]+unums[sort_ind]+rnums[sort_ind], 
        label="Mythic Rare")
plt.xticks(range(len(btypes)), btypes[sort_ind], rotation=90)
plt.yticks([10,20,30,40,50])
plt.grid(zorder=1, axis="y")
plt.legend()
plt.tight_layout()
plt.savefig("../"+dex_name+"_types.png")
plt.show()



#crare, cnums = count_types(rare)
#
#plt.figure()
#plt.title(dex_name + " Sjældenhedsfordeling")
#plt.bar(crare, cnums, edgecolor="black", width=0.8, zorder=10)
#plt.yticks([20,40,60,80])
#plt.grid(zorder=1, axis="y")
#plt.tight_layout()
#plt.savefig("../"+dex_name+"_rarities.png")
#plt.show()