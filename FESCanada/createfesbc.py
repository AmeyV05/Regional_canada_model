#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Script to create .bc file with fes boundary conditions for given .xyn file and tstart and tstop.
@Author: Amey Vasulkar
Copyright (c) 2022 Deltares
'''

import numpy as np
import os
import sys
import xarray as xr
import matplotlib.pyplot as plt

#function to create .nc file with fes wl data. 
# file fes2netcdf.sh should be present in the folder you are running this script from. 
def runfes2netcdf(filename,tstart,tstop):
    command="sh fes2netcdf.sh "+filename+" "+tstart+" "+tstop
    print (command)
    os.system(command)


tstart='201309010000'
tstop ='201310010000'
boundaryxyn='ABC.xyn' #xyn file of boundary points

#create .netcdf file
runfes2netcdf(boundaryxyn,tstart,tstop)

#read netcdf data. to see if everything worked.

data=xr.open_dataset('ABC.nc')
h=data.tide.values
lon=data.lon.values
lat=data.lat.values
time=data.time.values

print(h,lon,time)


# creating .bc file

#getting the appropritate header with boundary name. 
#boundarytrial.bc file should be present in the folder where you run this script. 
def writeheader(file,boundname):
    with open('boundarytrial.bc','r') as f:
        i=0
        for line in f:
            if i==1:
                file.write('Name                            = '+boundname+'\n')
            else:
                file.write(line)
            i+=1
        file.write('\n')

timemins=np.linspace(0,(len(time)-1)*10,5473) #5473 for one month 
# timemins=np.linspace(0,(len(time)-1)*10,289) 
print(timemins[-1])


newfile='ABC.bc'
nfileobj=open(newfile,'w')
i=0
for i in range(len(lon)):
    if i<140:
        boundname='right_boundary_0'+"{:03d}".format(i+1)
    else:
        boundname='left_boundary_0'+"{:03d}".format(i-139)        
    writeheader(nfileobj,boundname)
    for j in range(len(time)):
        nfileobj.write(str(timemins[j])+'  '+str(h[j,i])+'\n')
    
nfileobj.close()