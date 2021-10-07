#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Computing stats for the region.
Created on Tue Oct 05 2021 5:45:00 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''

#%%
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_theme("paper")
import os
from postprocessing import readdata

import cartopy.crs as ccrs
import cartopy.feature as cpf 

tideconst='M2'

#%%
# all region.
# compare the results with annual M2 from TG data. remember this data is yearly and it already has H1 and H2
#TG data
tgfile=os.path.join(path1,'bathymetry_checks','TGCHS_RC_M2.nc')
(TGstavec,TGtidvec,TGstations)=readdata.readtgdata(tgfile,tideconst)
#deleting 2 points which are not in regional model.
nTGstavec=np.delete(TGstavec,[52,74],axis=0)
nTGtidvec=np.delete(TGtidvec,[52,74],axis=0)
nTGstations=np.delete(TGstations,[52,74])
#%%

## FES derived M2 for 154 tidal stations. As 2 stations are a bit inland in Regional and GTSM   
fesncfile=os.path.join(path1,'postprocessing','annual','ncdata','FESTGannual.nc')
# fesncfile=os.path.join(path1,'postprocessing','annual','ncdata','FESTGannual_nonsnapped.nc')
(Ftgstavec,Ftgtidvec)=readdata.readtidedata(fesncfile)

#%%
#compute RMSE amp. 
def computestats(obs,mod):
    error=obs-mod
    meanerror=np.mean(error)
    stderror=np.std(error)
    rmserror=np.sqrt((error**2).mean())
    stat=np.array([meanerror,stderror,rmserror])
    return(stat)

#computing phase differences considering 360==0 phase idea from Inger.
def realphasediff(ph1,ph2):
    diff=np.empty((len(ph1)))
    for i in range(len(ph1)):
        if ph1[i]>270 and ph2[i]<90:
            diff[i]=-(360-ph1[i])-ph2[i]
        elif ph1[i]<90 and ph2[i]>270:
            diff[i]=(360-ph2[i])+ph1[i]
        else:
            diff[i]=ph1[i]-ph2[i]    
    return(diff)
#%%
from importlib import reload  
reload(readdata)
# selecting data according to different Seas/regions in the model.
Seasvec=['Hudson Bay','The Northwestern Passages','Hudson Strait','Baffin Bay','Davis Strait','Beaufort Sea','Labrador Sea','Arctic Ocean']

# sea=Seasvec[0]
statvec=[]
phdiffvec=[]

for sea in Seasvec:
    print(sea)
    seafile=os.path.join(path1,'Altimetry_vanInger','SeasTG',sea+'_TG.xyn')
    seastanamevec=np.array(pd.read_csv(seafile,sep="\t",header=None))[:,2]

    seaTGtidvec=readdata.selectlocs(nTGstations,nTGtidvec,seastanamevec)
    seaFtidvec=readdata.selectlocs(nTGstations,Ftgtidvec,seastanamevec)
    #amplitude
    seastat=computestats(seaTGtidvec[:,0],seaFtidvec[:,0])
    #phase
    seaphdiff=realphasediff(seaTGtidvec[:,1],seaFtidvec[:,1])
    meanphdiff=seaphdiff.mean()
    statvec.append(seastat)
    phdiffvec.append(meanphdiff)

    







# %%
