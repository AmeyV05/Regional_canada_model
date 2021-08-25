#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
download waterlevel data from the CHS website and save it in folders.
Created on Tue Aug 24 2021 2:20:02 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
#%%
from os import mkdir
import numpy as np 
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import xarray as xr
from postprocessing import tideanalysis
from bathymetry_checks import readchsdata
import time
from matplotlib.dates import date2num

sdate='2020-01-01T00:00:00Z'  # sdate of all data
edate='2021-01-01T00:00:00Z'  # end date of all data.

#reading all station metadata.

# stationjsonfile='bathymetry_checks/chsstations.json'
stationjsonfile='chsstations.json'
(allstationinfodata,stationamevec,stationidvec,stationlonvec,stationlatvec)=readchsdata.getallstationmetadata(stationjsonfile)


def getwldata(sdate,edate,stationid,stationlon,stationlat):
    data={}
    (Tlvec,Wlvec)=readchsdata.getmergedata(sdate,edate,stationid)      
    data['time']=Tlvec,
    data['h']=Wlvec
    data['lon']=stationlon
    data['lat']=stationlat
    print(np.shape(Wlvec))
    print(np.shape(Tlvec))
    return(data)

j=0  #upto where the last station was saved
for i in range(len(stationidvec[j:])):
    stationid=stationidvec[i]
    stationlon=[stationlonvec[i]]
    stationlat=[stationlatvec[i]]
    print(i)
    (data)=getwldata(sdate,edate,stationid,stationlon,stationlat)
    sshi=np.array((data['h']))
    if len(sshi)==0:
        i+=1
        print("Skipping station with id:"+stationid)
        continue
    sshi=np.array((data['h']))
    ti=np.array(data['time']).flatten()
    vec=np.hstack((ti.reshape(len(ti),1),sshi.reshape(len(sshi),1)))
    header='Station Name:'+stationamevec[i]+'\t Station number:'+str(i)+'\tStation id:'+stationid+'\n'+'Lon:'+str(stationlon[0])+'\tLat:'+str(stationlat[0])
    # np.savetxt('bathymetry_checks/CHSdata/'+stationamevec[i]+'.wl',vec,fmt='%s',delimiter="\t\t",header=header)
    np.savetxt('CHSdata/'+stationamevec[i]+'.wl',vec,fmt='%s',delimiter="\t\t",header=header)

# #%%
# wldatatxt = np.loadtxt('bathymetry_checks/CHSdata/'+stationamevec[i]+'.wl',dtype='str',skiprows=2)

# print(wldatatxt[:,0])
# print(wldatatxt[:,1])
# timedatnum=np.array((date2num(wldatatxt[:,0]))).flatten()
# sshi=wldatatxt[:1].astype(np.float64)





# %%
