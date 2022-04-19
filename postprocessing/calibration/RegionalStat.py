#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Script which plots regional statistics from TG data in canada.
Created on Fri Apr 15 2022 4:50:48 PM
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
import seaborn as sns
sns.set_theme("notebook")

month='Sep'


#%% function defintions
#plot function definitions.

def gettgindex(tgid,tgidvec,regional_tg_pos,tstaposdata):
    #library needed. scipy.spatial.distance --> cdist
    #first step is to find the lon lat corresponding to tgid from the regional_tg_pos data.
    #then compare these lon lat with tstaposdata and where matching take those indices.
    indreg=np.where(tgidvec==int(tgid))[0]
    itgvec=np.vstack((regional_tg_pos[indreg,0],regional_tg_pos[indreg,1])).T
    #with spatial
    distmat=sdist.cdist(tstaposdata,itgvec)
    tgregindx=np.where(distmat==0)[0]
    #Think about this approach later.
    # #now find where in our normal tstanamdata are these and compute the graphs and stats.
    # longregindex=np.isin(tstaposdata[:,0],itglon)
    # latgregindex=np.isin(tstaposdata[:,1],itglat)
    # tgregindex=longregindex and latgregindex
    # trialtg=tstaposdata[:,0][tgregindex]
    return(tgregindx)

#plot time series.
def plottimeseries(hobs,hmod,label,stationloc,fname):
    left, width = .0, .5
    bottom, height = .0, .5
    right = left + width
    top = bottom + height
    stationloc=np.array(stationloc)
    #rmse compute
    rmse=readdata.rmscompute(hobs,hmod)
    datastr='('+str(round(stationloc[0],2))+','+str(round(stationloc[1],2))+') \n RMSE:'+str(round(rmse,2))
    fig=plt.figure(figsize=(6,2),frameon=True)
    ax = plt.gca()
    ax.plot(hobs,'r--',label='Obs')
    ax.plot(hmod,'b',label=label)
    ax.text(0.0,1.2,datastr, ha='left', va='top', transform=ax.transAxes)
    plt.legend()
    plt.savefig(fname, bbox_inches = 'tight',dpi=300)

## old function not needed anymore.
# def plotalltimeseries(folder,hobs,hmod,label,tstanamdata):
#     for i in range(len(tstanamdata)):
#         tgname=tstanamdata[i]
#         hobsi=hobs[i,:]-hobs[i,:].mean()
#         hmodi=hmod[:,i]
#         fname=os.path.join(path1,'postprocessing','calibration','figures',folder,tgname+'.jpg')
#         plottimeseries(hobsi,hmodi,label,fname)

# making dirs based on regions and plotting regional data.
def plotregionaltimseries(folder,regioname,hobs,hmod,label,tgnamdata,tstaposdata):
    #create a director in the folder with the region name.
    directory=folder+'/'+regioname
    Path(directory).mkdir(parents=True, exist_ok=True)
    for i in range(len(tgnamdata)):
        tgname=tgnamdata[i]
        # print(tgname)
        hobsi=hobs[i,:]-hobs[i,:].mean()
        hmodi=hmod[:,i]
        fname=os.path.join(path1,'postprocessing','calibration','figures',directory,tgname+'.jpg')
        plottimeseries(hobsi,hmodi,label,tstaposdata[i,:].ravel(),fname)

#creating plots for each region.
def plotallregionaltimeseries(label,regnamdf,regional_tg_pos,tstaposdata,hobs,tgidvec,tstanamdata,foldername,hmod):   
    for i in range(len(regnamdf.keys())-1):
        #-1 because rdf reads the first empty element as key too.
        region_name=regnamdf[str(i+1)][0] #str(i+1) because the first element is no key and i starts from 0 while key from 1
        #[0] index implies first element.
        print(region_name)
        #find indexing for the region from tgid.
        tgid=i+1
        regindex=gettgindex(tgid,tgidvec,regional_tg_pos,tstaposdata)
        #folder loc
        loc='/u/vasulkar/p_emodnet_amey/Regional_canada_model/postprocessing/calibration/figures/'
        folder=loc+foldername
        plotregionaltimseries(folder,region_name,hobs[regindex,:],hmod[:,regindex],label,tstanamdata[regindex],tstaposdata[regindex])


#%%#first step is readin obs.
# tgstafile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/snelliusmodels/Canadamodel_1/stochModel/input_model/TGObs_Sep.xyn' #file which has obs on wet cells in canada model.
#second file with only 150 Tg not 154.
tgstafile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/snelliusmodels/Canadamodel_4.1r/stochModel/input_model/TGObs_Sep.xyn'
# Reading the tg name data
headerlist=["Lon","Lat","Name"]
df=pd.read_csv(tgstafile,delim_whitespace=True,names=headerlist,quotechar="'")
tstanamdata=np.array(df['Name'])
#TG obs from the obs folder.
obsfolder=os.path.join(path1,'model_development','Openda_models','Observations','CHSTG','Sept_All')
(hobs,Lonvec,Latvec)=readdata.readnprocessobsdata(tgstafile,obsfolder)
tstaposdata=np.vstack((Lonvec,Latvec)).T
regional_name_file='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/Parameters/canada_subdivision/RegionDescription.csv'
rdf=pd.read_csv(regional_name_file)
#reading the tg id for each tg station.
fname='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/Parameters/canada_subdivision/Canada_TG_subdivision3.xyz' #the number in z location corresponds to the region based on Rnamedict below.
#also the version 3 has some TG shifted from one domain to another for clear visualisaiton.
headerlist=['Lon','Lat','paraid']
cdf=pd.read_csv(fname,names=headerlist,delim_whitespace=True)
tgidvec=cdf.paraid.values
regional_tg_pos=np.vstack((cdf.Lon.values,cdf.Lat.values)).T

#%%

runsfolder=os.path.join(path1,'model_runs','snellius_runs','OpenDAruns','2020runs')
simulationame='Canadamodel_v1.1'
CFfname='CF_'+simulationame+'.jpg'
optworkdir=str(18)
simfolder=runsfolder+'/'+simulationame+'/'
optmodelfolder=simfolder+'stochModel/work'+optworkdir+'/'
#reading the optimal results.
optmoddata=xr.open_dataset(optmodelfolder+'output/canada_model_0000_his.nc')
hopt=optmoddata['waterlevel'][1:,:] 
optrmsevec=readdata.getrmsdata(hobs,hopt.T)
foldername='Optv1.1TimeSeriesSep'
label='Optv1.1'
# plotallregionaltimeseries(label,rdf,regional_tg_pos,tstaposdata,hobs,tgidvec,tstanamdata,foldername,hopt)
# read fes and GTSM4.1 output
#%%
#gtsm data
#removing the 4 TG.
rindex=np.array([121,128,49,31]).astype(int) 
gtsmdata=xr.open_dataset('/u/vasulkar/p_emodnet_amey/Regional_canada_model/postprocessing/calibration/ncdata/GTSMTG15min_Sep.nc')
hgtsm=gtsmdata['H']
hgtsm=np.delete(hgtsm,rindex,axis=1)
foldername='GTSMv4.1TimeSeriesSep'
label='GTSMv4.1'
# plotallregionaltimeseries(label,rdf,regional_tg_pos,tstaposdata,hobs,tgidvec,tstanamdata,foldername,hgtsm)

# %% fes data reading and getting rmse
fesdata=xr.open_dataset('/u/vasulkar/p_emodnet_amey/Regional_canada_model/postprocessing/calibration/ncdata/FESTG15min_Sep.nc')
hfes=fesdata['H']
hfes=np.delete(hfes,rindex,axis=1)
foldername='FESTimeSeriesSep'
label='FES'
# plotallregionaltimeseries(label,rdf,regional_tg_pos,tstaposdata,hobs,tgidvec,tstanamdata,foldername,hfes)


#%% 
# #regional stats.

def computeandplotstat(hobs,hmod,foldername):
    nkeys=len(rdf.keys())-1
    for i in range(nkeys):
        # if i==9:
        #-1 because rdf reads the first empty element as key too.
        region_name=rdf[str(i+1)][0] #str(i+1) because the first element is no key and i starts from 0 while key from 1
        #[0] index implies first element.
        print(region_name)
        #find indexing for the region from tgid.
        tgid=i+1
        regindex=gettgindex(tgid,tgidvec,regional_tg_pos,tstaposdata)
        #folder loc
        loc='/u/vasulkar/p_emodnet_amey/Regional_canada_model/postprocessing/calibration/figures/'
        folder=loc+foldername+'/'+region_name
        rmsevec=readdata.getrmsdata(hobs[regindex,:],hmod[:,regindex].T)
        rmsdf=pd.Series(rmsevec).describe()
        regdf=pd.DataFrame.from_dict({'Region':region_name},orient='index')
        totdf=pd.concat([regdf,rmsdf])
        totdf.to_csv(folder+'/'+region_name+'.stat',header=None, sep='\t', mode='w')
        #now we save a plot in the folder with TG locations and rmse.
        plotname=os.path.join(path1,'postprocessing','calibration','figures',folder,region_name+'_TG.jpg')
        plotregionaltg(region_name,tstanamdata[regindex],tstaposdata[regindex,0],tstaposdata[regindex,1],plotname,rmsevec.round(2))

def plotregionaltg(region_name,stanamdata,rtglon,rtglat,fname,rmsvec):
    #extent dictionary to create maps of correct extent.
    extentdict={'UB':(-75, -60, 55, 65),'BB':(-75.0,-50.0,55.0,70.0),
            'NL':(-70.0,-45.0,45.0,65.0),'HS':(-85.0,-60.0,60,70.0),
            'AW':(-150.0,-100.0,65,80.0),'ANW':(-150.0,-100.0,65,80.0),
            'FB':(-90.0,-63.0,60,75.0),'AN':(-100.0,-50.0,72,85.0),  
            'EAC':(-110.0,-62.0,62,85.0),'EHB':(-95.0,-70.0,50,67.0),'WHB':(-95.0,-70.0,50,67.0)}
    extent=extentdict[region_name]
    fig=plt.figure(figsize=(20, 14), frameon=True)
    # proj=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)
    proj=ccrs.PlateCarree()
    # proj=ccrs.LambertAzimuthalEqualArea(central_longitude=-30,central_latitude=0)
    ax1=fig.add_subplot(1,1,1,projection=proj) 
    ax1.set_extent(extent, crs=ccrs.PlateCarree())
    
    for i in range(len(rmsvec)):
        ax1.scatter(rtglon[i],rtglat[i],transform=ccrs.PlateCarree(),label=stanamdata[i]+'_'+str(rmsvec[i]),edgecolors='black',s=500)
        ax1.annotate(rmsvec[i], (rtglon[i], rtglat[i]),color='red', size=24,transform=ccrs.PlateCarree())
    # ax1.annotate(rtglon, rtglat, rmsvec, color='red', size=15, ha='center', va='center', transform=ccrs.PlateCarree())
    ax1.legend()

    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=0.2)
    ax1.add_feature(feature)
    # plt.show()
    fig.savefig(fname,dpi=300)
    

# %%
foldername='Optv1.1TimeSeriesSep'
hmod=hopt
computeandplotstat(hobs,hmod,foldername)

#%%
foldername='FESTimeSeriesSep'
computeandplotstat(hobs,hfes,foldername)
# %%
foldername='GTSMv4.1TimeSeriesSep'
computeandplotstat(hobs,hgtsm,foldername)
# %%
