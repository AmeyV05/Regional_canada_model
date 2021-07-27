#%%
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
    cont=plt.scatter(Lon,Lat,c=diffam,cmap=cmap,vmin=-0.25,vmax=0.25,transform=ccrs.PlateCarree())
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
    cont=plt.scatter(Lon,Lat,c=diffph,cmap=cmap,vmin=-100,vmax=100,transform=ccrs.PlateCarree())
    cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
    cbar.set_label(cbarlabel, rotation=90) 
    # ax.set_title(title)
    fig.suptitle('Difference of M2 amp and phase ('+name+' ) RMSE:'+'%.4f' % diffamrms+'m', fontsize=16)
    fig.savefig('postprocessing/test_M2/'+name+'.jpg')

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
# compare the results with different datasets. We have 3 ets now:
# 1. FES2014, 2. Altimetry 3. GTSM v4.1

# reading of all these datasets. 

#FES data
fesfile=os.path.join(path1,'postprocessing','test_M2','FESM2canada.nc')
(Fstavec,Ftidvec)=readdata.readtidedata(fesfile)

#GTSM data
gtsmfile=os.path.join(path1,'postprocessing','test_M2','GTSMM2canada.nc')
(Gstavec,Gtidvec)=readdata.readtidedata(gtsmfile)

#Altimetry data
altfile=os.path.join(path1,'Altimetry_vanInger','ModM2Arctic_altimetry.nc')
(Astavec,Atidvec)=readdata.readaltidata(altfile)

# Now we compare our  model results. with each of these datasets and plot them. 
# For this we use the function above. 

# %%
# Standard model comparisons. 

# With FES boundary. 
# reading of the model results 
#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2fesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='sModelwFES-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='sModelwFES-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='sModelwFES-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)

#model with gtsm b

#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2gtsmb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='sModelwGTSM-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='sModelwGTSM-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='sModelwGTSM-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)

#%%
# Model with fast ice and no bottom friction calibration from xiaohui. 

# With FES boundary. 
# reading of the model results 
#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2ficefesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='ficeModelwFES-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='ficeModelwFES-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='ficeModelwFES-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)

#model with gtsm b

#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2gtsmb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='ficeModelwGTSM-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='ficeModelwGTSM-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='ficeModelwGTSM-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)

#%%
print('done')