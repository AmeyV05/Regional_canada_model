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
from importlib import reload  
reload(readdata)
# selecting data according to different Seas/regions in the model.
Seasvec=['Hudson Bay','The Northwestern Passages','Hudson Strait','Baffin Bay','Davis Strait','Beaufort Sea','Labrador Sea','Arctic Ocean']

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


def getsubdregional(TGstations,TGtid,Modtid,sea):

    # for sea in Seasvec:
    print(sea)
    seafile=os.path.join(path1,'Altimetry_vanInger','SeasTG',sea+'_TG.xyn')
    seastanamevec=np.array(pd.read_csv(seafile,sep="\t",header=None))[:,2]
    seastavec=np.array(pd.read_csv(seafile,sep="\t",header=None))[:,0:2]
    seaTGtidvec=readdata.selectlocs(TGstations,TGtid,seastanamevec)
    seaFtidvec=readdata.selectlocs(TGstations,Modtid,seastanamevec)

    #amplitude
    seastat=computestats(seaTGtidvec[:,0],seaFtidvec[:,0])
    #phase
    seaphdiff=realphasediff(seaTGtidvec[:,1],seaFtidvec[:,1])
    meanphdiff=seaphdiff.mean()

    return(seastat,meanphdiff,seaTGtidvec,seaFtidvec,seastavec)

def scatterplot(stavec,obstid,modtid,ampstat,phdiff,sea,name):
    fig,ax=plt.subplots(figsize=(20,14),frameon=True)
    # fig,ax=plt.figure(figsize=(20,14),frameon=True)
    textstr = '\n'.join((
    r'$\mu=%.2f$' % (ampstat[0], ),
    r'$\sigma=%.2f$' % (ampstat[1],),
    r'$\mathrm{rmse}=%.2f$' % (ampstat[2], ),
    r'$d\phi_{\mu}=%.2f$' % (phdiff, )))

    ax.scatter(obstid[:,0],modtid[:,0],marker='o')
    lims = [np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
            np.max([ax.get_xlim(), ax.get_ylim()]),
            ]  # max of both axes ]
    ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
    ax.set_aspect('equal')
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_xlabel('Observed TG amplitude',fontsize=14)
    ax.set_ylabel(name+' derived amplitude',fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    # place a text box in upper left in axes coords
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
    fig.suptitle('Scatter plot for '+sea, fontsize=20,y=0.91)
    fname=os.path.join(path1,'postprocessing','annual','figures',sea+'_'+name+'_TG.jpg')
    fig.savefig(fname,dpi=300)


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
#FES TG comparison
## FES derived M2 for 154 tidal stations. As 2 stations are a bit inland in Regional and GTSM   
fesncfile=os.path.join(path1,'postprocessing','annual','ncdata','FESTGannual.nc')
# fesncfile=os.path.join(path1,'postprocessing','annual','ncdata','FESTGannual_nonsnapped.nc')
(Ftgstavec,Ftgtidvec)=readdata.readtidedata(fesncfile)
for sea in Seasvec:
    (Fseastat,Fseaphdiff,seaTGtid,seaFtid,seastavec)=getsubdregional(nTGstations,nTGtidvec,Ftgtidvec,sea)
    scatterplot(seastavec,seaTGtid,seaFtid,Fseastat,Fseaphdiff,sea,'FES')

#%%
#standard model TG comparison. 
smodelncfile=os.path.join(path1,'postprocessing','annual','ncdata','Standardmodelannualgtsmb.nc')
# fesncfile=os.path.join(path1,'postprocessing','annual','ncdata','FESTGannual_nonsnapped.nc')
(SModtgstavec,SModtgtidvec)=readdata.readtidedata(smodelncfile)
for sea in Seasvec:
    (Mseastat,Mseaphdiff,seaTGtid,seaMtid,seastavec)=getsubdregional(nTGstations,nTGtidvec,SModtgtidvec,sea)
    scatterplot(seastavec,seaTGtid,seaMtid,Mseastat,Mseaphdiff,sea,'SModel')



# #%%
# #plot rmse mean etc
# # RMSE plot.
# rmse=statvec[:,2]
# plt.plot(Seasvec,rmse)
# plt.xticks(rotation=45)
# plt.show()

# #mean std plot
# plt.errorbar(Seasvec,statvec[:,0],statvec[:,1],fmt='ok')
# plt.xticks(rotation=45)
# plt.show()
