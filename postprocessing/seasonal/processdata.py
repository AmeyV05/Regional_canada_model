#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
processing of different datasets
Created on Thu Sep 30 2021 11:41:11 AM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
#%%
# 2 seasonal comparisons possible!! TG and altimetry. (We do only march and sept comparisons. )
# WE process data based on both. 
# for each of march and septh we compute amplitudes and save 2 files separately. 
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import numpy as np
import os
import datetime
import xarray as xr
from postprocessing import readdata, tideanalysis

tideconst='M2'

#%%
## TG 
# Initially we start with FES reading the TG fes data and altimetry fes data for march and sept. 

# reading FES data on CHS TG 
#This section needs to be run only once. 
# # reading FES data.
festgfile=os.path.join(path1,'FESCanada','CHSTG_snapped_model_obs.nc')  #with 154 regional model obs
# festgfile=os.path.join(path1,'FESCanada','CHSTG.nc') 
festgdata=xr.open_dataset(festgfile)
# getting march and sept data.

def createmonthlydata(tstart,tend,festgdata,name):
    tvec=np.array(festgdata['time'])

    tf64=np.datetime64(datetime.datetime.strptime(tstart,"%Y%m%d%H%M"))
    te64=np.datetime64(datetime.datetime.strptime(tend,"%Y%m%d%H%M"))
    s=np.where(tvec==tf64)[0][0]
    e=np.where(tvec==te64)[0][0]
    tmon=tvec[s:e]
    hmon=np.array(festgdata['tide'])[s:e,:]

    M2AFtg=[];M2PFtg=[];data={}
    for i in range(len(festgdata['lon'])):
        data['h']=hmon[:,i]
        data['time']=tmon
        data['lon']=[np.array(festgdata['lon'])[i]]
        data['lat']=[np.array(festgdata['lat'])[i]]
        (Am,Ph)=tideanalysis.compute1stationtidal(data,tideconst)
        M2AFtg=np.append(M2AFtg,Am)
        M2PFtg=np.append(M2PFtg,Ph)
        i+=1
    readdata.createNC(M2AFtg,M2PFtg,festgdata['lon'],festgdata['lat'],name)
    print('done')
#march
tstart='201303010000'
tend='201304010000'
name='FESTGmarch2013'
createmonthlydata(tstart,tend,festgdata,name)
#sept
tstart='201309010000'
tend='201310010000'
name='FESTGsept2013'
createmonthlydata(tstart,tend,festgdata,name)


# %%
# Standard canada model TG computations. 
#reading canada model data.
t_all,tf=readdata.timecomputations()
# locindex=(406+np.linspace(0,742,743)).astype(int)
locindex=(1149+np.linspace(0,153,154)).astype(int)
hisfileloc=os.path.join(path1,'model_runs','cartesius_runs', 'annualruns','standardruns')

for times in t_all[:]:
    # times=t_all[0]
    tiym=times[0].strftime("%Y%m")
    if tiym=='201303' or tiym=='201309':
        hisfile=os.path.join(hisfileloc,'canada_model_his_'+tiym+'.nc')
        print(hisfile)
        modelannualdata=readdata.readmodel(hisfile,locindex)
        modelannualdata['time']=modelannualdata['time']
        modelannualdata['h']=modelannualdata['h']
        (M2Aannual,M2Pannual,Mlon,Mlat)=tideanalysis.tidalanalysis(modelannualdata,tideconst)
        readdata.createNC(M2Aannual,M2Pannual,Mlon,Mlat,'Standardmodel'+tiym+'gtsmb')

#%% 
## ALTIMETRY
locindex=(406+np.linspace(0,742,743)).astype(int) 
# # reading FES data.
#march
fesfile=os.path.join(path1,'FESCanada','Altimetry_boundary_obs','fes_boundary_altimetry_mar2013.nc')
fesdata=readdata.readfes(fesfile,locindex)
#tidal analysis and conversion to NC
(M2AF,M2PF,Flon,Flat)=tideanalysis.tidalanalysis(fesdata,tideconst)
readdata.createNC(M2AF,M2PF,Flon,Flat,'FESAltiM2Mar2013')
#sept
fesfile=os.path.join(path1,'FESCanada','Altimetry_boundary_obs','fes_boundary_altimetry_sep2013.nc')
fesdata=readdata.readfes(fesfile,locindex)
#tidal analysis and conversion to NC
(M2AF,M2PF,Flon,Flat)=tideanalysis.tidalanalysis(fesdata,tideconst)
readdata.createNC(M2AF,M2PF,Flon,Flat,'FESAltiM2Sep2013')
# %%
# Altimetry canada model
t_all,tf=readdata.timecomputations()
locindex=(406+np.linspace(0,742,743)).astype(int)
# locindex=(1149+np.linspace(0,153,154)).astype(int)
hisfileloc=os.path.join(path1,'model_runs','cartesius_runs', 'annualruns','standardruns')

for times in t_all[:]:
    # times=t_all[0]
    tiym=times[0].strftime("%Y%m")
    if tiym=='201303' or tiym=='201309':
        hisfile=os.path.join(hisfileloc,'canada_model_his_'+tiym+'.nc')
        print(hisfile)
        modelannualdata=readdata.readmodel(hisfile,locindex)
        modelannualdata['time']=modelannualdata['time']
        modelannualdata['h']=modelannualdata['h']
        (M2Aannual,M2Pannual,Mlon,Mlat)=tideanalysis.tidalanalysis(modelannualdata,tideconst)
        readdata.createNC(M2Aannual,M2Pannual,Mlon,Mlat,'AltiStandardmodel'+tiym+'gtsmb')
# %%
