#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Processing the month long gtsm data and create bc condition. The bc condition are such that we need atleast a few 
days spinup too in the simulations.
Created on Fri Mar 11 2022 2:17:02 PM
@Author: Amey Vasulkar
Copyright (c) 2022 Deltares
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
    folder='monthruns_2020/'
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

tstart='202001010000'
tstop ='202012310000'
t_all,tf=readdata.timecomputations(tstart,tstop)


#%% 
oldtimes=t_all[0]
for times in t_all:
    # times=t_all[0] 
    tiym=times[0].strftime("%Y%m")
    if times[0]<tf:
        tiym=tiym[0:4]+'01'
    timo=times[0].strftime("%m")
    if timo=='03':
        #spin up period:
        #sept
        #days=8
        # march
        days=7 
        timindex=int(days*24*6) #6 because our data is every 10mins.
        ## readin boundary and creating the .bc file.
        #when through main directory
        # file=os.path.join('gtsm_runs','allyearruns_2013','gtsm_model_his_'+tiym+'.nc')
        #when in jupyter lab
        file=os.path.join('allyearruns_2020','newversion','gtsm_model_his_'+tiym+'.nc')
        #and get the data from the old file too for spin up
        otiym=oldtimes[0].strftime("%Y%m")
        print(otiym)
        fileo=os.path.join('allyearruns_2020','newversion','gtsm_model_his_'+otiym+'.nc')
        # locindex=(np.linspace(0,474,475)).astype(int)  #reading old boundary. 
        locindex=(np.linspace(0,405,406)).astype(int) 
        gtsmbdata=readdata.readmodel(file,locindex)
        ogtsmbdata=readdata.readmodel(fileo,locindex)
        time=gtsmbdata['time']
        lon=gtsmbdata['lon']
        lat=gtsmbdata['lat']
        h=gtsmbdata['h']
        otime=ogtsmbdata['time'][-timindex-1:-1]
        oh=ogtsmbdata['h'][-timindex-1:-1,:]
        #total h and time.
        time=np.append(otime,time)
        h=np.vstack((oh,h))
        #getting ref date
        
        refdate=times[0].date()-datetime.timedelta(days=days)

        t_ref=datetime.datetime.combine(refdate,datetime.time(0))
        refdate_str=t_ref.strftime("%Y%m%d")
        # tstart=(times[0]-t_ref).total_seconds()/3600.
        tstart=0.0
        print ("TSTART = %f"%tstart)
        tstop=(times[1]-t_ref).total_seconds()/3600.
        tlenhisfile=int((tstop-tstart)*6) #per 10 mins so 6. 
        createbc(time,tlenhisfile,h,tiym,str(refdate))
        break
        
    oldtimes=times
    print('boundary file created.')
    
# %%
