#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Comparison of different datasets. Stats etc. 
Created on Thu Sep 30 2021 11:41:11 AM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
#%%
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import numpy as np
import os
import xarray as xr
from postprocessing import readdata, tideanalysis

tideconst='M2'
#%% reading FES data on tide gauges and doing a yearly tidal analysis along with creating NC file.
#This sections needs to be run only once. 
# # reading FES data.
# festgfile=os.path.join(path1,'FESCanada','CHSTG_snapped_model_obs.nc')  #with 154 regional model obs
festgfile=os.path.join(path1,'FESCanada','CHSTG.nc') 
festgdata=xr.open_dataset(festgfile)
M2AFtg=[];M2PFtg=[];data={}
for i in range(len(festgdata['lon'])):
    data['h']=np.array(festgdata['tide'])[:,i]
    data['time']=np.array(festgdata['time'])
    data['lon']=[np.array(festgdata['lon'])[i]]
    data['lat']=[np.array(festgdata['lat'])[i]]
    (Am,Ph)=tideanalysis.compute1stationtidal(data,tideconst)
    M2AFtg=np.append(M2AFtg,Am)
    M2PFtg=np.append(M2PFtg,Ph)
    i+=1
name='FESTGannual_nonsnapped'
readdata.createNC(M2AFtg,M2PFtg,festgdata['lon'],festgdata['lat'],name)
print('done')
# %%





