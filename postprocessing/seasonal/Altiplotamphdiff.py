#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This script plots the amplitude and phase difference between different datasets.
Created on Thu Sep 30 2021 3:32:58 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
#%%
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme("paper")
import os
from postprocessing import readdata 
import cartopy.crs as ccrs
import cartopy.feature as cpf 

tideconst='M2'

#defining the plot function.

def plotdiff(Lon,Lat,diffam,diffph,name):
    diffamrms = np.sqrt(np.mean(diffam**2))
    fig=plt.figure(figsize=(20,14),frameon=True)
    cmap='seismic'
    # title='M2amp'
    cbarlabel='Amplitude(m)'
    ax=fig.add_subplot(1,2,1,projection=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)) 
    ax.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
    ax.add_feature(feature)
    cont=plt.scatter(Lon,Lat,c=diffam,cmap=cmap,marker='o',vmin=-0.25,vmax=0.25,transform=ccrs.PlateCarree(),s=100)
    cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
    cbar.set_label(cbarlabel, rotation=90, fontsize=18)
    cbar.ax.tick_params(labelsize=18)
    # Phase subplot
    level=50.
    # title='M2ph'
    cbarlabel='Phase(deg)'
    ax=fig.add_subplot(1,2,2,projection=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)) 
    ax.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
    ax.add_feature(feature)
    cont=plt.scatter(Lon,Lat,c=diffph,cmap=cmap,marker='o',vmin=-100,vmax=100,transform=ccrs.PlateCarree(),s=100)
    cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
    cbar.set_label(cbarlabel, rotation=90, fontsize=18) 
    cbar.ax.tick_params(labelsize=18)

    # ax.set_title(title)
    fig.suptitle('Difference of '+tideconst+'amp and phase ('+name+' ) RMSE:'+'%.4f' % diffamrms+'m', fontsize=20,y=0.91)
    fname=os.path.join(path1,'postprocessing','seasonal','figures',name+'.jpg')
    fig.savefig(fname,dpi=300)

def plotMSdiff(Lon,Lat,diffam,diffph,name):
    # diffamrms = np.sqrt(np.mean(diffam**2))
    fig=plt.figure(figsize=(20,14),frameon=True)
    cmap='seismic'
    # title='M2amp'
    cbarlabel='Amplitude(m)'
    ax=fig.add_subplot(1,2,1,projection=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)) 
    ax.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())

    cont=plt.scatter(Lon,Lat,c=diffam,cmap=cmap,marker='o',vmin=-0.25,vmax=0.25,transform=ccrs.PlateCarree(),s=100)
    cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
    cbar.set_label(cbarlabel, rotation=90, fontsize=18)
    cbar.ax.tick_params(labelsize=18)
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
    ax.add_feature(feature)
    # Phase subplot
    level=50.
    # title='M2ph'
    cbarlabel='Phase(deg)'
    ax=fig.add_subplot(1,2,2,projection=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)) 
    ax.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
    ax.add_feature(feature)
    cont=plt.scatter(Lon,Lat,c=diffph,cmap=cmap,marker='o',vmin=-50,vmax=50,transform=ccrs.PlateCarree(),s=100)
    cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
    cbar.set_label(cbarlabel, rotation=90, fontsize=18) 
    cbar.ax.tick_params(labelsize=18)
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
    ax.add_feature(feature)
    # ax.set_title(title)
    fig.suptitle('Difference of '+tideconst+'amp and phase ('+name+' )', fontsize=20,y=0.91)
    fname=os.path.join(path1,'postprocessing','seasonal','figures',name+'.jpg')
    fig.savefig(fname,dpi=300)

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


def comparedatasets(Modstavec,Modtidvec,Obsstavec,Obstidvec,name):
    (nModstavec,nObsstavec,nModtidvec,nObstidvec)=readdata.snapstations(Modstavec,Obsstavec,Modtidvec,Obstidvec,1e-3)
    diffamfmwf=nModtidvec[:,0]-nObstidvec[:,0]
    diffphfmwf=realphasediff(nModtidvec[:,1],nObstidvec[:,1])
    plotdiff(nObsstavec[:,0],nObsstavec[:,1],diffamfmwf,diffphfmwf,name)
#%%
# all region.
## Observations 
# Altimetry obs  
# read march and sept data

#Altimetry data
altfile=os.path.join(path1,'Altimetry_vanInger','ModM2Arctic_altimetry.nc')
month='March'
(Astavec,Atidvecmar)=readdata.readmonthaltidata(altfile,month)
month='Sept'
(Astavec,Atidvecsep)=readdata.readmonthaltidata(altfile,month)



#%%

# Now model dat for comparisons

## FES derived M2 for altimetru
#march
   
fesncfilemar=os.path.join(path1,'postprocessing','seasonal','ncdata','FESAltiM2Mar2013.nc')
(Ftgstavec,Ftgtidvecmar)=readdata.readtidedata(fesncfilemar)
fesncfilesep=os.path.join(path1,'postprocessing','seasonal','ncdata','FESAltiM2Sep2013.nc')
(Ftgstavec,Ftgtidvecsep)=readdata.readtidedata(fesncfilesep)

# March difference
name=tideconst+'_(FES-Alti)_march'
comparedatasets(Ftgstavec,Ftgtidvecmar,Astavec,Atidvecmar,name)
# sep difference
name=tideconst+'_(FES-Alti)_sept'
comparedatasets(Ftgstavec,Ftgtidvecsep,Astavec,Atidvecsep,name)

# %%

## Standard model derived M2 altimetry
#march
   
smodncfilemar=os.path.join(path1,'postprocessing','seasonal','ncdata','AltiStandardmodel201303gtsmb.nc')
(SMtgstavec,SMtgtidvecmar)=readdata.readtidedata(smodncfilemar)
#sep
smodncfilesep=os.path.join(path1,'postprocessing','seasonal','ncdata','AltiStandardmodel201309gtsmb.nc')
(SMtgstavec,SMtgtidvecsep)=readdata.readtidedata(smodncfilesep)

# March difference
name=tideconst+'_(Smod-Alti)_march'
comparedatasets(SMtgstavec,SMtgtidvecmar,Astavec,Atidvecmar,name)
# sep difference
name=tideconst+'_(Smod-Alti)_sept'
comparedatasets(SMtgstavec,SMtgtidvecsep,Astavec,Atidvecsep,name)

# %%
#march -sept differences
#Altimetry

AlttidvecMS=Atidvecmar-Atidvecsep
name=tideconst+"_Alti_March-Sept"
plotMSdiff(Astavec[:,0],Astavec[:,1],AlttidvecMS[:,0],AlttidvecMS[:,1],name)
#%%
# Model
SMtgtidvecMS=SMtgtidvecmar-SMtgtidvecsep
name=tideconst+'_Alti_SModel_March-Sept'
plotMSdiff(SMtgstavec[:,0],SMtgstavec[:,1],SMtgtidvecMS[:,0],SMtgtidvecMS[:,1],name)
#%%
#FES
FtgtidvecMS=Ftgtidvecmar-Ftgtidvecsep
name=tideconst+'_Alti_FES_March-Sept'
plotMSdiff(Ftgstavec[:,0],Ftgstavec[:,1],FtgtidvecMS[:,0],FtgtidvecMS[:,1],name)

#%% optimized model march sept differnece.
#sep
omodncfilesep=os.path.join(path1,'postprocessing','seasonal','ncdata','AltiOptmodel_sep_all_gtsmb.nc')
(OMaltistavec,OMaltitidvecsep)=readdata.readtidedata(omodncfilesep)
# sep difference
name=tideconst+'_(Omod-Alti)_sept'
# comparedatasets(OMaltistavec,OMaltitidvecsep,Astavec,Atidvecsep,name)
#march
omodncfilemar=os.path.join(path1,'postprocessing','seasonal','ncdata','AltiOptmodel_mar_all_gtsmb.nc')
(OMaltistavec,OMaltitidvecmar)=readdata.readtidedata(omodncfilemar)
# sep difference
name=tideconst+'_(Omod-Alti)_mar'
# comparedatasets(OMaltistavec,OMaltitidvecmar,Astavec,Atidvecmar,name)

#%%
#March-Sept diference
OMAlttidvecMS=OMaltitidvecmar-OMaltitidvecsep
name=tideconst+'_Alti_Opt_March-Sept'
plotMSdiff(OMaltistavec[:,0],OMaltistavec[:,1],OMAlttidvecMS[:,0],OMAlttidvecMS[:,1],name)
# %%
