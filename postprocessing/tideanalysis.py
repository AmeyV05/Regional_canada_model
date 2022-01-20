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

#list from fermijn
constlist=['SA','SSA','MSM','MM','MSF','MF', \
    'ALP1','2Q1','SIG1','Q1','RHO1','O1','TAU1','BET1','NO1','CHI1','PI1','P1', \
    'S1','K1','PSI1','PHI1','THE1','J1','SO1','OO1','UPS1', \
    '2NS2','ST37','OQ2','EPS2','ST2','2N2','MU2','N2','NU2','OP2','H1','M2','H2','MKS2','LDA2', \
    'L2','T2','S2','R2','K2','MSN2','ETA2','2SM2','SKM2', \
    'NO3','MO3','M3','SO3','MK3','SK3', \
    'ST8','N4','3MS4','MN4','ST9','ST40','M4','ST10','SN4','KN4','MS4','MK4','SL4','S4','SK4', \
    'MNO5','2MO5','MNK5','2MP5','2MK5','MSK5','2SK5', \
    'ST11','2NM6','ST12','2MN6','ST13','ST41','M6','MSN6','MKN6','2MS6','2MK6','NSK6','2SM6','MSK6', \
    'ST16','3MK7', \
    'ST18','3MN8','ST19','M8','ST20','ST21','3MS8','3MK8','ST22','ST23','ST24', \
    'ST26','4MK9','ST27', \
    'ST28','M10','ST29','ST30','ST31','ST32', \
    'M12','ST34','ST35']

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
    # const=['K1','O1','Q1', 'P1','N2','M2','S2','K2','H2','H1'] # for yearly
    const=constlist
    const=['K1','O1','Q1', 'P1','N2','M2','S2','K2']
    epoch1='1970-01-01'
    tidalconst=tideconst
    time=data['time']
    timedatnum=np.array(date2num(time))
    Stationlon=data['lon'];Stationlat=data['lat']
    ssh=data['h']
    (Amp,Ph,nlon,nlat)=computetidal(ssh,timedatnum,Stationlat,Stationlon,const,epoch1,tidalconst)
    return(Amp,Ph,nlon,nlat)

def compute1stationtidal(data,tideconst):
    # const=['K1','O1','Q1', 'P1','N2','M2','S2','K2','H2','H1'] # for yearly
    # const=['K1','O1','Q1', 'P1','N2','M2','S2','K2']
    const=constlist
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
