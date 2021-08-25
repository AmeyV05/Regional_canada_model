#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This script creates a nc file of all M2 tidals constituents from the tide gauges.
Created on Thu Aug 19 2021 2:05:59 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
import numpy as np 
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import xarray as xr
from postprocessing import tideanalysis
from bathymetry_checks import readchsdata
import time


# sys.stdout = log_file
sdate='2020-01-01T00:00:00Z'  # sdate of all data
edate='2021-01-01T00:00:00Z'  # end date of all data.

#reading all station metadata.

# stationjsonfile='bathymetry_checks/chsstations.json'
stationjsonfile='chsstations.json'
(allstationinfodata,stationamevec,stationidvec,stationlonvec,stationlatvec)=readchsdata.getallstationmetadata(stationjsonfile)

# for each station.
tideconst='M2'
def getampph(tideconst,sdate,edate,stationidvec,stationlonvec,stationlatvec):
    amp=[];ph=[]

    data={}
    i=0
    for id in stationidvec[:]:
        stationid=id
        print(i)
        (Tlvec,Wlvec)=readchsdata.getmergedata(sdate,edate,stationid)
        if len(Wlvec)==0:
            i+=1
            print("Skipping station with id:"+stationid)
            continue
        data['time']=Tlvec,
        data['h']=Wlvec
        data['lon']=[stationlonvec[i]]
        data['lat']=[stationlatvec[i]]
        print(np.shape(Wlvec))
        print(np.shape(Tlvec))
        (Am,Ph)=tideanalysis.compute1stationtidal(data,tideconst)
        amp=np.append(amp,Am)
        ph=np.append(ph,Ph)
        i+=1
        time.sleep(10)

    return(amp,ph)

# create NC file
(amp,ph)=getampph(tideconst,sdate,edate,stationidvec,stationlonvec,stationlatvec)
selectstation={'M2amp':(("stations"),amp),'stationname':stationamevec,'Lon':stationlonvec,'Lat':stationlatvec}
coords={"stations": np.linspace(1,len(stationamevec),len(stationamevec))}
ds=xr.Dataset(selectstation,coords=coords)
ds.to_netcdf('M2stations.nc')


