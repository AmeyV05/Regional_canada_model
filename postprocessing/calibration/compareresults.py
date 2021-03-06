
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Script to compare the calibration runs for TG output with FES and current Standard. 
Created on Tue Apr 12 2022 4:23:12 PM
@Author: Amey Vasulkar
Copyright (c) 2022 Deltares
'''
#%%

import sys

from requests import delete
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import numpy as np
import os
import datetime
import xarray as xr
import pandas as pd
from postprocessing import readdata, tideanalysis
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cpf
from pathlib import Path
import scipy.spatial.distance as sdist


month='Mar'


#%%#first step is readin obs.
# tgstafile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/snelliusmodels/Canadamodel_1/stochModel/input_model/TGObs_Sep.xyn' #file which has obs on wet cells in canada model.
# tgstafile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/snelliusmodels/Canadamodel_4.1r/stochModel/input_model/TGObs_Sep.xyn'
# tgstafile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/snelliusmodels/Canadamodel_8r_2/stochModel/input_model/TGObs_Sep.xyn'
if month=='Sep':
    tgstafile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/snelliusmodels/Canadamodel_9_combined_final/stochModel/input_model/TGObs_Sep.xyn'
    obsfolder=os.path.join(path1,'model_development','Openda_models','Observations','CHSTG','Sept_All')
else:
    tgstafile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/snelliusmodels/Canadamodel_march_2/stochModel/input_model/TGObs_Mar.xyn'
    obsfolder=os.path.join(path1,'model_development','Openda_models','Observations','CHSTG','March_All')
# #TG obs from the obs folder.
# obsfolder=os.path.join(path1,'model_development','Openda_models','Observations','CHSTG','Sept_All')
(hobs,Lonvec,Latvec)=readdata.readnprocessobsdata(tgstafile,obsfolder)
#Now we check models fes and gtsm data.
#%%
# # reading FES data.
festgfile=os.path.join(path1,'FESCanada','CHSTG_snapped_model_obs_allyear20202.nc')  #with 154 regional model obs
# festgfile=os.path.join(path1,'FESCanada','CHSTG.nc') 
festgdata=xr.open_dataset(festgfile)
data={}
#index fes based on month.
if month=='Sep':
    # 1 september is 244th day
    sday=244
    sindexfes=int(6*24*sday)
    eindexfes=int(6*24*(sday+30)+1)
else:
    sday=60
    sindexfes=int(6*24*sday)
    eindexfes=int(6*24*(sday+31)+1)
hmat=np.array(festgdata['tide'])[sindexfes:eindexfes,:]
time=np.array(festgdata['time'])[sindexfes:eindexfes]  #for september
slon=np.array(festgdata['lon'])
slat=np.array(festgdata['lat'])
stations=np.array(festgdata['station_id'])

for i in range(len(festgdata['lon'])):
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
fname=os.path.join('ncdata','FESTG15min_'+month+'.nc')
ds.to_netcdf(fname)

#%% reading GTSM data and creatin .nc file.
# locindex=(406+np.linspace(0,742,743)).astype(int)
# locindex=(1149+np.linspace(0,153,154)).astype(int)
locindex=(1130+np.linspace(0,152,153)).astype(int)
# locindex=(np.linspace(0,153,154)).astype(int)
# hisfileloc=os.path.join(path1,'model_runs','cartesius_runs', 'annualruns','standardruns')
# hisfileloc=os.path.join(path1,'model_runs','snellius_runs', 'bathymetrytestruns','standardmodel_seprun')
# hisfile=hisfileloc+'/canada_model_0000_his.nc'
hisfileloc='/u/vasulkar/p_emodnet_amey/GTSM_prefive_2020/output/'
hisfile=hisfileloc+'/gtsm_model_0000_his.nc'
modelsepdata=readdata.readmodel(hisfile,locindex)

# hmat=np.array(modelsepdata['h'])[1:,:]
# time=np.array(modelsepdata['time'])[1:]  #for september
#for v5.
hmat=np.array(modelsepdata['h'])[1152:,:]
time=np.array(modelsepdata['time'])[1152:]  #for september
# print(time)
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
fname=os.path.join('ncdata','GTSMv5TG15min_'+month+'.nc')
ds.to_netcdf(fname)

#%% read the optimized output.
runsfolder=os.path.join(path1,'model_runs','snellius_runs','OpenDAruns','2020runs')
simulationame='Canadamodel_march_2.1'
CFfname='CF_'+simulationame+'.jpg'
optworkdir=str(48)
simfolder=runsfolder+'/'+simulationame+'/'
optmodelfolder=simfolder+'stochModel/work'+optworkdir+'/'
#reading the optimal results.
optmoddata=xr.open_dataset(optmodelfolder+'output/canada_model_0000_his.nc')
hopt=optmoddata['waterlevel'][1:,:] 
optrmsevec=readdata.getrmsdata(hobs,hopt.T)
# read fes and GTSM4.1 output
#%%
#gtsm data
#removing the 4 TG.
rindex=np.array([121,128,49,31]).astype(int) 
#now we add more TG because of them lying in fiords etc.
# indexarray=np.array([88,69,84,64,111,4,19,133,54,78,22,73,77,99,66,46,30,98,23,92,74,33,47,105,58,96,122,153,123,134,140,131,144,110,141,113,29]).astype(int)
indexarray=np.array([44,124,88,111,19,133,54,78,22,73,77,99,66,46,30,98,23,92,74,33,47,105,122,153,123,134,140,131,144,110,141,113,29]).astype(int)

rindex=np.append(rindex,indexarray)

#%%
gtsmdata=xr.open_dataset(os.path.join('ncdata','GTSMTG15min_'+month+'.nc'))
hgtsm=gtsmdata['H']
hgtsm=np.delete(hgtsm,rindex,axis=1)
gtsmrmsevec=readdata.getrmsdata(hobs,hgtsm.T)

#%%
#gtsmv5
gtsmdata=xr.open_dataset(os.path.join('ncdata','GTSMv5TG15min_'+month+'.nc'))
hgtsmv5=gtsmdata['H']
# add an element at disreali fiord to have easy coding.
hdisford=np.zeros(len(hgtsmv5[:,0]))
hgtsmv5=np.insert(hgtsmv5,88,hdisford,axis=1)
hgtsmv5=np.delete(hgtsmv5,rindex,axis=1)
gtsmv5rmsevec=readdata.getrmsdata(hobs,hgtsmv5.T)
# %% fes data reading and getting rmse
fesdata=xr.open_dataset(os.path.join('ncdata','FESTG15min_'+month+'.nc'))
hfes=fesdata['H']
hfes=np.delete(hfes,rindex,axis=1)
fesrmsevec=readdata.getrmsdata(hobs,hfes.T)
# %%
#now we plot and compare results. First we comput RMSE of inidividual and then compare between models.
# then we finally plot for each TG how the rmse looks with different models. 
def plotrmse(modrmse,Lonvec,Latvec,fname):
    from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
    # marking the x-axis and y-axis 
    fig=plt.figure(figsize=(12, 5), frameon=True)
    # proj=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)
    proj=ccrs.PlateCarree()
    # ax1=fig.add_subplot(1,1,1,projection=proj) 
    ax1=plt.axes(projection=proj)
    ax1.set_extent((-145, -47, 49, 85), crs=ccrs.PlateCarree())
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1)
    ax1.add_feature(feature)
    cax = fig.add_axes([ax1.get_position().x1+0.01,ax1.get_position().y0,0.01,ax1.get_position().height])
    scatter_opts = {'marker':'^','s':300,'cmap':'viridis','transform':ccrs.PlateCarree(),'alpha':1,'vmin':0,'vmax':1.0}
    cont=ax1.scatter(Lonvec,Latvec,c=modrmse,**scatter_opts)
    cbar=plt.colorbar(cont,cax=cax)
    cbarlabel='RMSE in m'
    cbar.set_label(cbarlabel)
    # plt.show() 
    # ax1.set_title('Difference in RMSE (blue showing improvement)', fontsize=20)
    fig.savefig(fname,dpi=300)

 
def plotrmsediff(modrmse1,modrmse2,Lonvec,Latvec,fname):
    from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
    diff=modrmse2-modrmse1
    # marking the x-axis and y-axis 
    fig=plt.figure(figsize=(12, 5), frameon=True)
    # proj=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)
    proj=ccrs.PlateCarree()
    # ax1=fig.add_subplot(1,1,1,projection=proj) 
    ax1=plt.axes(projection=proj)
    ax1.set_extent((-145, -47, 49, 85), crs=ccrs.PlateCarree())
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1)
    ax1.add_feature(feature)
    cax = fig.add_axes([ax1.get_position().x1+0.01,ax1.get_position().y0,0.01,ax1.get_position().height])
    scatter_opts = {'marker':'^','s':300,'cmap':'seismic','transform':ccrs.PlateCarree(),'alpha':1,'vmin':-0.25,'vmax':0.25}
    cont=ax1.scatter(Lonvec,Latvec,c=diff,**scatter_opts)
    cbar=plt.colorbar(cont,cax=cax)
    cbarlabel='Differences in m'
    cbar.set_label(cbarlabel)
    # plt.show() 
    # ax1.set_title('Difference in RMSE (blue showing improvement)', fontsize=20)
    fig.savefig(fname,dpi=300)


#%%
#FES plot
fname=os.path.join(path1,'postprocessing','calibration','figures','RMSEFES2014_Marr.jpg')
plotrmse(fesrmsevec,Lonvec,Latvec,fname)
# # GTSM plot
# fname=os.path.join(path1,'postprocessing','calibration','figures','RMSEGTSMv4.1_Sepr.jpg')
# plotrmse(gtsmrmsevec,Lonvec,Latvec,fname)

# # GTSMv5 plot
# fname=os.path.join(path1,'postprocessing','calibration','figures','RMSEGTSMv5_Sepr.jpg')
# plotrmse(gtsmv5rmsevec,Lonvec,Latvec,fname)
#OPT plot
fname=os.path.join(path1,'postprocessing','calibration','figures','RMSEOPT_march_2.1Mar.jpg')
plotrmse(optrmsevec,Lonvec,Latvec,fname)
# %%
#difference plots.
fname=os.path.join(path1,'postprocessing','calibration','figures','RMSEdiffFES-OPT_march2.1Mar.jpg')
plotrmsediff(fesrmsevec,optrmsevec,Lonvec,Latvec,fname)
# %%
# fname=os.path.join(path1,'postprocessing','calibration','figures','RMSEdiffGTSM4.1-9_combined_final.2Sep.jpg')
# plotrmsediff(gtsmrmsevec,optrmsevec,Lonvec,Latvec,fname)
# # #difference plots.
# fname=os.path.join(path1,'postprocessing','calibration','figures','RMSEdiffFES-GTSM4.1_Sepr.jpg')
# plotrmsediff(fesrmsevec,gtsmrmsevec,Lonvec,Latvec,fname)
#%%
## GTSMv5
#difference plots.
# # #FES
# fname=os.path.join(path1,'postprocessing','calibration','figures','RMSEdiffFES-GTSv5_Sep.jpg')
# plotrmsediff(fesrmsevec,gtsmv5rmsevec,Lonvec,Latvec,fname)
# #GTSMv4.1.
# fname=os.path.join(path1,'postprocessing','calibration','figures','RMSEdiffGTSMv4.1-GTSv5_Sep.jpg')
# plotrmsediff(gtsmrmsevec,gtsmv5rmsevec,Lonvec,Latvec,fname)
# #OPT
# fname=os.path.join(path1,'postprocessing','calibration','figures','RMSEdiffOPT_8r_2.2_Sep_beforecali-GTSv5_Sep.jpg')
# plotrmsediff(optrmsevec,gtsmv5rmsevec,Lonvec,Latvec,fname)

# %%
# testing cost function from rmse.
cfopt=np.sum(optrmsevec**2)
cffes=np.sum(fesrmsevec**2)
cfgtsm=np.sum(gtsmrmsevec**2)
rindex=np.array([121,128,49,31]).astype(int)
optrmsevec2=np.delete(optrmsevec,rindex)
cfopt2=np.sum(optrmsevec2**2)
