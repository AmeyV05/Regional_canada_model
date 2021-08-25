#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on Tue Jul 06 2021 2:04:11 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
import os
import numpy as np
import utide 
import pandas as pd
from matplotlib.dates import date2num

def computetidal(ssh,time,StationLat,StationLon,const,epoch1,tidalconst):
    amp=[]
    ph=[]
    Upstlon=[];Upstlat=[]
#     epoch1="201212250000"
    for i in range(len(StationLat)):
        sshi=np.array(ssh[:,i])
        sumsshi=np.sum(sshi)
        is_empty = sshi.size == 0
        if (is_empty==False and pd.isna(sumsshi)==False):              
            coef = utide.solve(time,sshi ,
                                 lat=StationLat[i],
                                 epoch=epoch1,
                                 constit=const,
                                 conf_int='linear',
                                 white=True,
                                 method='ols')
            Amp=coef['A']
            Ph=coef['g']
            name=coef['name']
            j=np.where(name==tidalconst)
            amp=np.append(amp,Amp[j]) # 0 is for M2
            ph=np.append(ph,Ph[j])
            Upstlon=np.append(Upstlon,StationLon[i])
            Upstlat=np.append(Upstlat,StationLat[i])
    return(amp,ph,Upstlon,Upstlat)

def tidalanalysis(data,tideconst):
    # const=['K1','O1','Q1', 'P1','N2','M2','S2','K2']
    const=['K1','O1','Q1', 'P1','N2','M2','S2','K2','H2','H1']
    epoch1='1970-01-01'
    tidalconst=tideconst
    time=data['time']
    timedatnum=np.array(date2num(time))
    Stationlon=data['lon'];Stationlat=data['lat']
    ssh=data['h']
    (Amp,Ph,nlon,nlat)=computetidal(ssh,timedatnum,Stationlat,Stationlon,const,epoch1,tidalconst)
    return(Amp,Ph,nlon,nlat)

def compute1stationtidal(data,tideconst):
    const=['K1','O1','Q1', 'P1','N2','M2','S2','K2','H2','H1']
    epoch1='1970-01-01'
    tidalconst=tideconst
    time=data['time']
    timedatnum=np.array((date2num(time))).flatten()
    Stationlon=data['lon'];Stationlat=data['lat']
    sshi=np.array((data['h']))
    coef = utide.solve(timedatnum,sshi,lat=Stationlat[0],
                        epoch=epoch1,
                        constit=const,
                        conf_int='linear',
                        white=True,
                        method='ols')
    Amp=coef['A']
    Ph=coef['g']
    name=coef['name']
    j=np.where(name==tidalconst)
    amp=Amp[j] 
    ph=Ph[j]
    return(amp,ph)

def fake_tide(t, M2amp, M2phase):
    """
    Generate a minimally realistic-looking fake semidiurnal tide.
    
    t is time in hours
    phases are in radians
    
    Modified from: http://currents.soest.hawaii.edu/ocn760_4/_static/plotting.html
    """
    return M2amp * np.sin(2 * np.pi * t / 12.42 - M2phase)

def main():
    const=['K1','O1','Q1', 'P1','N2','M2','S2','K2']
    tidalconst='M2'
    epoch1='1970-01-01'
    N=500
    time=pd.date_range(start='2013-01-01',periods= N,freq='H')
    # Signal + some noise.
    h = fake_tide(np.arange(N), M2amp=2, M2phase=0) + np.random.randn(N)
    time=np.array(date2num(time))
    (Amp,Ph,Lon,Lat)=computetidal(h.reshape((len(h),1)),time,[60.0],[0.0],const,epoch1,tidalconst)


if __name__ == "__main__":
    main()
    print("Done")
