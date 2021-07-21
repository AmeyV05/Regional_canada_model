#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on Tue Jul 06 2021 2:02:16 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import seaborn as sns
sns.set_theme("paper")
import os
import xarray as xr
from postprocessing import readdata 
import cartopy.crs as ccrs
import cartopy.feature as cpf 


#defining the plot function.

def plotdiff(Lon,Lat,diffam,diffph,name):
    diffamrms = np.sqrt(np.mean(diffam**2))
    fig=plt.figure(figsize=(14, 14))
    cmap='seismic'

    # title='M2amp'
    cbarlabel='Amplitude(m)'
    ax=fig.add_subplot(1,2,1,projection=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)) 
    ax.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
    ax.add_feature(feature)
    cont=plt.scatter(Lon,Lat,c=diffam,cmap=cmap,vmin=-0.5,vmax=0.5,transform=ccrs.PlateCarree())
    cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
    cbar.set_label(cbarlabel, rotation=90) 
    # Phase subplot
    level=50.
    # title='M2ph'
    cbarlabel='Phase(deg)'
    ax=fig.add_subplot(1,2,2,projection=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)) 
    ax.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
    ax.add_feature(feature)
    cont=plt.scatter(Lon,Lat,c=diffph,cmap=cmap,vmin=-50,vmax=50,transform=ccrs.PlateCarree())
    cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
    cbar.set_label(cbarlabel, rotation=90) 
    # ax.set_title(title)
    fig.suptitle('Difference of M2 amp and phase ('+name+' ) RMSE:'+'%.4f' % diffamrms+'m', fontsize=16)
    fig.savefig('postprocessing/test_M2/'+name+'.jpg')

# compare the results with different datasets. We have 5 datasets now:
# 1. FES2014, 2. Altimetry 3. Canada modelwFesb 4. Canada model wGTSMb  5. GTSM v4.1

# reading of the datasets.
#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2fesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

#FES data
fesfile=os.path.join(path1,'postprocessing','test_M2','FESM2canada.nc')
(Fstavec,Ftidvec)=readdata.readtidedata(fesfile)

#GTSM data
gtsmfile=os.path.join(path1,'postprocessing','test_M2','GTSMM2canada.nc')
(Gstavec,Gtidvec)=readdata.readtidedata(gtsmfile)

#Altimetry data
altfile=os.path.join(path1,'Altimetry_vanInger','ModM2Arctic_altimetry.nc')
(Astavec,Atidvec)=readdata.readaltidata(altfile)

# fes and modelwfes

(nMfstavec,nFstavec,nMftidvec,nFtidvec)=readdata.snapstations(Mfstavec,Fstavec,Mftidvec,Ftidvec,1e-3)

# gtsm and modelwfes

(nMfstavec,nGstavec,nMftidvec,nGtidvec)=readdata.snapstations(Mfstavec,Gstavec,Mftidvec,Gtidvec,1e-3)      

# altimetry and modelwfes
(nMfAstavec,nAstavec,nMfAtidvec,nAtidvec)=readdata.snapstations(Mfstavec,Astavec,Mftidvec,Atidvec,1e-3)

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

# plots

#fes-modelwfes
name='ModelwFES-FES'
diffamfmwf=nMftidvec[:,0]-nFtidvec[:,0]
diffphfmwf=realphasediff(nMftidvec[:,1],nFtidvec[:,1])
plotdiff(nFstavec[:,0],nFstavec[:,1],diffamfmwf,diffphfmwf,name)

#gtsm-modelwfes
name='ModelwFES-GTSM'
diffamgmwf=nMftidvec[:,0]-nGtidvec[:,0]
diffphgmwf=realphasediff(nMftidvec[:,1],nGtidvec[:,1])
plotdiff(nFstavec[:,0],nFstavec[:,1],diffamgmwf,diffphgmwf,name)


#Altimetry-modelwfes
name='ModelwFES-Altimetry'
diffamamwf=nMfAtidvec[:,0]-nAtidvec[:,0]
diffphamwf=realphasediff(nMfAtidvec[:,1],nAtidvec[:,1])
plotdiff(nAstavec[:,0],nAstavec[:,1],diffamamwf,diffphamwf,name)



#%% modelwith GTSM boundary. 
#model fes b
modelgfile=os.path.join(path1,'postprocessing','test_M2','ModM2gtsmb.nc')
(Mgstavec,Mgtidvec)=readdata.readtidedata(modelgfile)

#snapping the model results to individual datasets.
# fes and modelwfes

(nMgstavec,nFstavec,nMgtidvec,nFtidvec)=readdata.snapstations(Mgstavec,Fstavec,Mgtidvec,Ftidvec,1e-3)

# gtsm and modelwfes

(nMgstavec,nGstavec,nMgtidvec,nGtidvec)=readdata.snapstations(Mgstavec,Gstavec,Mgtidvec,Gtidvec,1e-3)      

# altimetry and modelwfes
(nMgAstavec,nAstavec,nMgAtidvec,nAtidvec)=readdata.snapstations(Mgstavec,Astavec,Mgtidvec,Atidvec,1e-3)


# plots

#fes-modelwfes
name='ModelwGTSM-FES'
diffamfmwg=nMgtidvec[:,0]-nFtidvec[:,0]
diffphfmwg=realphasediff(nMgtidvec[:,1],nFtidvec[:,1])
plotdiff(nFstavec[:,0],nFstavec[:,1],diffamfmwg,diffphfmwg,name)

#gtsm-modelwfes
name='ModelwGTSM-GTSM'
diffamgmwg=nMgtidvec[:,0]-nGtidvec[:,0]
diffphgmwg=realphasediff(nMgtidvec[:,1],nGtidvec[:,1])
plotdiff(nFstavec[:,0],nFstavec[:,1],diffamgmwg,diffphgmwg,name)


#Altimetry-modelwfes
name='ModelwGTSM-Altimetry'
diffamamwg=nMgAtidvec[:,0]-nAtidvec[:,0]
diffphamwg=realphasediff(nMgAtidvec[:,1],nAtidvec[:,1])
plotdiff(nAstavec[:,0],nAstavec[:,1],diffamamwg,diffphamwg,name)
print('done')
# %%
