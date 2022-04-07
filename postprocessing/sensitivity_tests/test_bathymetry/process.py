#%%
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on Tue Mar 29 2022 5:28:28 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
This script takes compares the output of the two model runs with GEBC2019 and GEBCO2021 with th TG data.
'''
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import numpy as np
import os
import xarray as xr
from postprocessing import readdata, tideanalysis
import pandas as pd
import datetime
# compare the results with different datasets. We have 5 datasets now:
# 1. FES2014, 2. Altimetry 3. Canada modelwFesb 4. Canada model wGTSMb  5. GTSM v4.1

# reading of the datasets.
# reading canada model w FES boundary
# locindex=(475+np.linspace(0,742,743)).astype(int)  
locindex=(1149+np.linspace(0,153,154)).astype(int)  #2 locations are not snapped! 

tideconst='M2'

#%%
#resampling the his data to 15min interval for direct comparison to tg.
def getncresample(modelsepdata,fname):
    hmat=np.array(modelsepdata['h'])[:,:]
    time=np.array(modelsepdata['time'])[:] 
    slon=np.array(modelsepdata['lon'])
    slat=np.array(modelsepdata['lat'])
    stations=np.array(modelsepdata['station'])

    for i in range(len(modelsepdata['lon'])):
        if i==0:
            h=hmat[:,i]
            s=pd.Series(h,index=time)
            hresamp=s.resample('15min').interpolate()
            timresamp=np.array(hresamp.index.values)
            hresamp=np.array([hresamp.values])
            hresampmat=hresamp
        else:
            h=hmat[:,i]
            s=pd.Series(h,index=time)
            hresamp=s.resample('15min').interpolate()
            timresamp=np.array(hresamp.index.values)
            hresamp=np.array([hresamp.values])
            hresampmat=np.vstack((hresampmat,hresamp))
        
    ds=xr.Dataset({'H':(('time','stations'),hresampmat.T),'lon':(('stations'),slon),'lat':(('stations'),slat)},
                    coords={'stations':stations,
                            'time':timresamp})
    ds.to_netcdf(fname)

import math
def rmscompute(hobs,hmod):
    #first remove the mean from hobs.
    hobsmean=hobs-hobs.mean()
    hmodmean=hmod-hmod.mean()
    MSE = np.square(np.subtract(hobsmean,hmodmean)).mean() 
    RMSE = math.sqrt(MSE)
    return(RMSE)

def getrmsdata(hobsmat,hmodmat):
    nstations=154
    rmsevec=[]
    for i in range(154):
        RMSE=rmscompute(hobsmat[i,:],hmodmat[i,:])
        rmsevec=np.append(rmsevec,RMSE)
    return(rmsevec)

#%%
#Standard model with SAL and TG and altimtry in his file.
modelffile=os.path.join(path1,'model_runs','snellius_runs','bathymetrytestruns','gebco2019run','canada_model_0000_his.nc')
smodelfdata=readdata.readmodel(modelffile,locindex)
sfname=os.path.join('ncdata','Gebco10model15min.nc')
getncresample(smodelfdata,sfname)


#%%

#Standard model with SAL and TG and altimtry in his file.
# modelffile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','TGsalgtsmboundaryoutput','canada_model_0000_his.nc')
modelffile=os.path.join(path1,'model_runs','snellius_runs','bathymetrytestruns','standardmodelrun','canada_model_0000_his.nc')
smodelcfdata=readdata.readmodel(modelffile,locindex)
sfcname=os.path.join('ncdata','Standardmodelwcali15min.nc')
getncresample(smodelcfdata,sfcname)
#%%
#Standard model but with GEBCO21 documents.
modelffile=os.path.join(path1,'model_runs','snellius_runs','bathymetrytestruns','gebco2021run','canada_model_0000_his.nc')
gbmodelfdata=readdata.readmodel(modelffile,locindex)
gfname=os.path.join('ncdata','Gebco21model15min.nc')
getncresample(gbmodelfdata,gfname)
# #tidla analysis and conversion to NC
# (M2AMf,M2PMf,Mflon,Mflat)=tideanalysis.tidalanalysis(modelfdata,tideconst)
# readdata.createNC(M2AMf,M2PMf,Mflon,Mflat,'TGsalModelwgtsmb')


# %%
tstafile=os.path.join(path1,'model_development','Openda_models','Observations','CHSTG','Jan_All','TGObs_Jan.xyn') #file which has obs on wet cells in canada model.
headerlist=["Lon","Lat","Name"]
df=pd.read_csv(tstafile,delim_whitespace=True,names=headerlist,quotechar="'")
tstaposdata=np.vstack((df['Lon'],df['Lat'])).T
tstanamdata=np.array(df['Name'])
#TG obs from the obs folder. 
#station data
Lon=df['Lon']
Lat=df['Lat']
#time data


obsfolder=os.path.join(path1,'model_development','Openda_models','Observations','CHSTG','Jan_All')
files=os.listdir(obsfolder)
headerlist=["Time","Waterlevel"]
for i in range(len(tstanamdata)):
    tgfile=obsfolder+'/'+tstanamdata[i]+'.wl'
    if i==0:
        dftg=pd.read_csv(tgfile,delim_whitespace=True,names=headerlist,skiprows=1)
        hmattg=dftg['Waterlevel']
    else:
        dftg=pd.read_csv(tgfile,delim_whitespace=True,names=headerlist,skiprows=1)
        hmattg=np.vstack((hmattg,dftg['Waterlevel']))
# %%
smdeldata=xr.open_dataset(sfname)
hgeb19=smdeldata['H'][672:,:]
time=smdeldata['time']
geb19rmsevec=getrmsdata(hmattg,hgeb19.T)
gmdeldata=xr.open_dataset(gfname)
hgeb21=gmdeldata['H'][672:,:]
gebrmsevec=getrmsdata(hmattg,hgeb21.T)
scmdeldata=xr.open_dataset(sfcname)
hstacali=scmdeldata['H'][672:,:]
stacalirmsevec=getrmsdata(hmattg,hstacali.T)
#%%
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(20, 14), frameon=True)
plt.scatter(np.arange(0,len(geb19rmsevec),1),geb19rmsevec,label='GEBCO2019')
plt.scatter(np.arange(0,len(gebrmsevec),1),gebrmsevec,label='GEBCO2021')
plt.scatter(np.arange(0,len(stacalirmsevec),1),stacalirmsevec,label='standardwcali')
plt.legend()
fname=os.path.join(path1,'postprocessing','sensitivity_tests','test_bathymetry','figures','rmsecomp.jpg')
fig.savefig(fname,dpi=300)
# %%
# marking the x-axis and y-axis 
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cpf
fig=plt.figure(figsize=(20, 14), frameon=True)
proj=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)
ax1=fig.add_subplot(1,1,1,projection=proj) 
ax1.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())

feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1)
ax1.add_feature(feature)
scatter_opts = {'marker':'^','s':300,'cmap':'viridis','transform':ccrs.PlateCarree(),'alpha':1,'vmin':0.0,'vmax':1.0}
cont=ax1.scatter(Lon,Lat,c=gebrmsevec,**scatter_opts)
cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
# plt.show()
plt.title('RMSE for Jan in m', fontsize=20)
fname=os.path.join(path1,'postprocessing','sensitivity_tests','test_bathymetry','figures','geb21rmse.jpg')
fig.savefig(fname,dpi=300)
# %%
#RMSE diff
# marking the x-axis and y-axis 
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cpf
fig=plt.figure(figsize=(20, 14), frameon=True)
proj=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)
ax1=fig.add_subplot(1,1,1,projection=proj) 
ax1.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())

feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1)
ax1.add_feature(feature)
scatter_opts = {'marker':'^','s':300,'cmap':'seismic','transform':ccrs.PlateCarree(),'alpha':1,'vmin':-1.0,'vmax':1.0}
cont=ax1.scatter(Lon,Lat,c=gebrmsevec-geb19rmsevec,**scatter_opts)
cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
# plt.show()
plt.title('RMSE for Jan in m', fontsize=20)
fname=os.path.join(path1,'postprocessing','sensitivity_tests','test_bathymetry','figures','rmsediff.jpg')
fig.savefig(fname,dpi=300)
# %%
# marking the x-axis and y-axis 
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cpf
fig=plt.figure(figsize=(20, 14), frameon=True)
proj=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)
ax1=fig.add_subplot(1,1,1,projection=proj) 
ax1.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())

feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1)
ax1.add_feature(feature)
scatter_opts = {'marker':'^','s':300,'cmap':'seismic','transform':ccrs.PlateCarree(),'alpha':1,'vmin':-1.0,'vmax':1.0}
cont=ax1.scatter(Lon,Lat,c=stacalirmsevec-geb19rmsevec,**scatter_opts)
cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
# plt.show()
plt.title('RMSE for Jan in m', fontsize=20)
fname=os.path.join(path1,'postprocessing','sensitivity_tests','test_bathymetry','figures','rmsediffcali.jpg')
fig.savefig(fname,dpi=300)
# %%
