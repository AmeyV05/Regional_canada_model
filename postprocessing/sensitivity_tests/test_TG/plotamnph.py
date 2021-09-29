#%%
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on Wed Sep 14 2021 7:50:26 PM
@Author: Amey Vasulkar
# This script analysis on TG data. TG from CHS
Copyright (c) 2021 Deltares
'''
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

def plotamph(Lon,Lat,am,ph,name):
    fig=plt.figure(figsize=(20,14),frameon=True)
    cmap='viridis'

    # title='M2amp'
    cbarlabel='Amplitude(m)'
    ax=fig.add_subplot(1,2,1,projection=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)) 
    ax.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
    ax.add_feature(feature)
    cont=plt.scatter(Lon,Lat,c=am,cmap=cmap,marker='^',s=800,vmin=0,vmax=2.0,transform=ccrs.PlateCarree())
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
    cont=plt.scatter(Lon,Lat,c=ph,cmap=cmap,marker='^',s=800,vmin=0,vmax=360,transform=ccrs.PlateCarree())
    cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
    cbar.set_label(cbarlabel, rotation=90, fontsize=18) 
    cbar.ax.tick_params(labelsize=18)

    # ax.set_title(title)
    fig.suptitle(tideconst+'amp and phase ('+name+' ) ', fontsize=20,y=0.91)
    fname=os.path.join(path1,'postprocessing','test_TG','figures',name+'.jpg')
    fig.savefig(fname,dpi=300)



#%%
# compare the results with M2 from TG data. remember this data is yearly and it already has H1 and H2
#TG data
tgfile=os.path.join(path1,'bathymetry_checks','TGCHS_RC_M2.nc')
(TGstavec,TGtidvec,TGstations)=readdata.readtgdata(tgfile,tideconst)
name='TG'
plotamph(TGstavec[:,0],TGstavec[:,1],TGtidvec[:,0],TGtidvec[:,1],name)



# %%
# TG sal Standard model comparisons.  

# With GTSM boundary. 
# reading of the model results 
#model fes b
modelffile=os.path.join(path1,'postprocessing','test_TG','ncdata','TGsalModelwgtsmb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)
name='TGSALModelwGTSM'
plotamph(Mfstavec[:,0],Mfstavec[:,1],Mftidvec[:,0],Mftidvec[:,1],name)


# %%
