#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on Mon Jul 05 2021 11:21:18 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
import os
import numpy as np
import xarray as xr
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/postprocessing/')
import readdata


## Time analysis
## readin boundary and creating the .bc file.
file=os.path.join('gtsm_runs','Jan2013v4.1_3dmodel','gtsm_model_0000_his.nc')
# locindex=(np.linspace(0,474,475)).astype(int)  #reading only boundary. 
locindex=(np.linspace(0,405,406)).astype(int) 
gtsmbdata=readdata.readmodel(file,locindex)

time=gtsmbdata['time']
lon=gtsmbdata['lon']
lat=gtsmbdata['lat']
h=gtsmbdata['h']




def writeheader(file,boundname):
    with open('FESCanada/boundarytrial.bc','r') as f:
        i=0
        for line in f:
            if i==1:
                file.write('Name                            = '+boundname+'\n')
            else:
                file.write(line)
            i+=1
        file.write('\n')

def createbc(time,h,filename):
    timemins=np.linspace(0,(len(time)-1)*10,5473) #5473 for one month 
    nfileobj=open(filename,'w')
    i=0
    for i in range(len(lon)):
        if i<140:
            boundname='right_boundary_0'+"{:03d}".format(i+1)
        else:
            boundname='left_boundary_0'+"{:03d}".format(i-139)        
        writeheader(nfileobj,boundname)
        for j in range(len(time)):
            nfileobj.write(str(timemins[j])+'  '+"{:.6f}".format(h[j,i])+'\n')
        
    nfileobj.close()

newfile='gtsm_runs/gtsmwaterlevel10km_5e-2_2_month_try.bc'

createbc(time,h,newfile)
print('boundary file created.')