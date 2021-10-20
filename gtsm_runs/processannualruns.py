#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on Mon Jul 05 2021 11:21:18 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
#%%
import os
import numpy as np
import xarray as xr
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/postprocessing/')
import readdata
import datetime
from calendar import monthrange
from postprocessing import readdata



#%%
def writeheader(file,boundname,refdate):
    #bcfile header
    # filewheader='FESCanada/boundarytrial.bc'
    filewheader='../FESCanada/boundarytrial.bc'
    #mins since
    timstring='minutes since '+refdate+' 00:00:00'
    with open(filewheader,'r') as f:
        i=0
        for line in f:
            if i==1:
                file.write('Name                            = '+boundname+'\n')
            elif i==5:
                file.write('Unit                            = '+timstring+'\n')
            else:
                file.write(line)
            i+=1
        file.write('\n')

def createbc(time,tlenhisfile,h,tiym,refdate):
    # folder='gtsm_runs/allyearruns_2013/'
    folder='allyearruns_2013/'
    timemins=np.linspace(0,(len(time)-1)*10,tlenhisfile+1)  
    #create left boundary
    filename=folder+'gtsmwaterlevel_left_'+tiym+'.bc'
    nfileobj=open(filename,'w')
    i=0
    for i in range(len(lon)):
        if i>139:
            boundname='left_boundary_0'+"{:03d}".format(i-139)        
            writeheader(nfileobj,boundname,refdate)
            for j in range(len(time)):
                nfileobj.write(str(timemins[j])+'  '+"{:.6f}".format(h[j,i])+'\n')    
    nfileobj.close()
    filename=folder+'gtsmwaterlevel_right_'+tiym+'.bc'
    nfileobj=open(filename,'w')
    i=0
    for i in range(len(lon)):
        if i<140:
            boundname='right_boundary_0'+"{:03d}".format(i+1)       
            writeheader(nfileobj,boundname,refdate)
            for j in range(len(time)):
                nfileobj.write(str(timemins[j])+'  '+"{:.6f}".format(h[j,i])+'\n')    
    nfileobj.close()

#%%
t_all,tf=readdata.timecomputations()

#%% 

for times in t_all:
    # times=t_all[0] 
    tiym=times[0].strftime("%Y%m")
    if times[0]<tf:
        tiym=tiym[0:4]+'01'

        

    ## readin boundary and creating the .bc file.
    #when through main directory
    # file=os.path.join('gtsm_runs','allyearruns_2013','gtsm_model_his_'+tiym+'.nc')
    #when in jupyter lab
    file=os.path.join('allyearruns_2013','gtsm_model_his_'+tiym+'.nc')
    # locindex=(np.linspace(0,474,475)).astype(int)  #reading only boundary. 
    locindex=(np.linspace(0,405,406)).astype(int) 
    gtsmbdata=readdata.readmodel(file,locindex)

    time=gtsmbdata['time']
    lon=gtsmbdata['lon']
    lat=gtsmbdata['lat']
    h=gtsmbdata['h']

    refdate=times[0].date()
    t_ref=datetime.datetime.combine(refdate,datetime.time(0))
    refdate_str=t_ref.strftime("%Y%m%d")
    tstart=(times[0]-t_ref).total_seconds()/3600.
    print ("TSTART = %f"%tstart)
    tstop=(times[1]-t_ref).total_seconds()/3600.
    tlenhisfile=int((tstop-tstart)*6) #per 10 mins so 6. 


#   createbc(time,tlenhisfile,h,tiym,str(refdate))
    print('boundary file created.')
# %%
