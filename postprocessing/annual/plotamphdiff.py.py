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
    cont=plt.scatter(Lon,Lat,c=diffam,cmap=cmap,marker='^',s=800,vmin=-0.25,vmax=0.25,transform=ccrs.PlateCarree())
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
    cont=plt.scatter(Lon,Lat,c=diffph,cmap=cmap,marker='^',s=800,vmin=-100,vmax=100,transform=ccrs.PlateCarree())
    cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
    cbar.set_label(cbarlabel, rotation=90, fontsize=18) 
    cbar.ax.tick_params(labelsize=18)

    # ax.set_title(title)
    fig.suptitle('Difference of '+tideconst+'amp and phase ('+name+' ) RMSE:'+'%.4f' % diffamrms+'m', fontsize=20,y=0.91)
    fname=os.path.join(path1,'postprocessing','annual','figures',name+'.jpg')
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

def comparedatasets(TGstavec,TGtidvec,Mfstavec,Mftidvec,name):
    (nTGstavec,nTGtidvec)=snapTG(TGstavec,TGtidvec)
    diffamfmwf=(Mftidvec[:,0]-nTGtidvec[:,0])
    diffphfmwf=realphasediff(Mftidvec[:,1],nTGtidvec[:,1])
    plotdiff(nTGstavec[:,0],nTGstavec[:,1],diffamfmwf,-diffphfmwf,name)

def snapTG(TGstavec,TGtidvec):

    # only two stations are not snapped in regional model. Fort Albany and Port Nelson
    # their values are 52 and 74. 
    nTGstavec=np.delete(TGstavec,[52,74],axis=0)
    nTGtidvec=np.delete(TGtidvec,[52,74],axis=0)
    # below commented code was when the xyn file from TG and given to gtsm or regional model is exactly the same
    # But this is not the condition as we determine the wetcells first! 
    # for i in range(len(Mfstavec[:,0])):
    #     lon=Mfstavec[i,0]
    #     lat=Mfstavec[i,1]
    #     for j in range(len(TGstavec[:,0])):
    #         if (lon==TGstavec[j,0] and lat==TGstavec[j,1]):
    #             nTGstavec[i,0]=TGstavec[j,0];nTGstavec[i,1]=TGstavec[j,1]
    #             nTGtidvec[i,0]=TGtidvec[j,0];nTGtidvec[i,1]=TGtidvec[j,1]
    return(nTGstavec,nTGtidvec)

#%%
# compare the results with annual M2 from TG data. remember this data is yearly and it already has H1 and H2
#TG data
tgfile=os.path.join(path1,'bathymetry_checks','TGCHS_RC_M2.nc')
(TGstavec,TGtidvec,TGstations)=readdata.readtgdata(tgfile,tideconst)


## FES derived M2 for 154 tidal stations. As 2 stations are a bit inland in Regional and GTSM   
fesncfile=os.path.join(path1,'postprocessing','annual','ncdata','FESTGannual.nc')
# fesncfile=os.path.join(path1,'postprocessing','annual','ncdata','FESTGannual_nonsnapped.nc')
(Ftgstavec,Ftgtidvec)=readdata.readtidedata(fesncfile)
name=tideconst+'_(FES-TG)_annual'
comparedatasets(TGstavec,TGtidvec,Ftgstavec,Ftgtidvec,name)




# %%
