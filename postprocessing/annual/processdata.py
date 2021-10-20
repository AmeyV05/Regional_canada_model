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
#reading canada model data.
t_all,tf=readdata.timecomputations()
# locindex=(406+np.linspace(0,742,743)).astype(int)
locindex=(1149+np.linspace(0,153,154)).astype(int)
hisfileloc=os.path.join(path1,'model_runs','cartesius_runs', 'annualruns','standardruns')

for times in t_all[:]:
    # times=t_all[0]
    tiym=times[0].strftime("%Y%m")
    if times[0]<tf:
        tiym=tiym[0:4]+'01'
        hisfile=os.path.join(hisfileloc,'canada_model_his_'+tiym+'.nc')
        modelannualdata=readdata.readmodel(hisfile,locindex)
        modelannualdata['time']=modelannualdata['time'][1:]
        modelannualdata['h']=modelannualdata['h'][1:,:]
    else:
        #merging data for annual
        hisfile=os.path.join(hisfileloc,'canada_model_his_'+tiym+'.nc')
        hismonthlydata=readdata.readmodel(hisfile,locindex)
        hismonthlydata['time']=hismonthlydata['time'][1:]
        hismonthlydata['h']=hismonthlydata['h'][1:,:]
        modelannualdata['h']=np.vstack((modelannualdata['h'],hismonthlydata['h']))
        modelannualdata['time']=np.append(modelannualdata['time'],hismonthlydata['time'])


(M2Aannual,M2Pannual,Mlon,Mlat)=tideanalysis.tidalanalysis(modelannualdata,tideconst)
readdata.createNC(M2Aannual,M2Pannual,Mlon,Mlat,'Standardmodelannualgtsmb')





# %%
