#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on Fri Jul 02 2021 2:42:31 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares

This script is a module which has functions to read the nc data files from models. 
'''
import numpy as np
import os
import xarray as xr
import matplotlib.tri as tri


def readmodel(file,locindex):
    moddata=xr.open_dataset(file)
    timemod=moddata.time.values
    modlon=moddata.station_x_coordinate.values[locindex] #0:78 for coarse #0:245 fine
    modlat=moddata.station_y_coordinate.values[locindex]
    name=moddata.station_name.values[locindex]
    hmod=moddata.waterlevel.values[:,locindex]
    print("Model data reading done.")
    moddata.close()
    modata={'time':timemod,'lon':modlon,'lat':modlat,'h':hmod,'station':name}
    return(modata)

def readfes(file,locindex):
    fesdata=xr.open_dataset(file)
    timfes=fesdata.time.values
    feslon=fesdata.lon.values[locindex]
    feslat=fesdata.lat.values[locindex]
    hfes=fesdata.tide.values[:,locindex]
    stations=fesdata.stations.values[locindex]
    print("FES2014 data reading done.")
    fesdata.close()
    fesdat={'time':timfes,'lon':feslon,'lat':feslat,'h':hfes,'station':stations}
    return(fesdat)

def readmodelmap(file):
    mapset=xr.open_dataset(file)
    nfelem=mapset.nFlowElem.values
    xfelem=mapset.FlowElem_xcc.values
    yfelem=mapset.FlowElem_ycc.values
    hfelem=mapset.s1.values
    ufelem=mapset.ucx.values
    vfelem=mapset.ucy.values
    time=mapset.time.values
    mapset.close()
    print("Reading map file done.")
    mapdata={'time':time,'lon':xfelem,'lat':yfelem,'h':hfelem,'u':ufelem,'v':vfelem,'nelem':nfelem}
    return(mapdata)

def readtidedata(file):
    tideset=xr.open_dataset(file)
    Lon=tideset.lon.values
    Lat=tideset.lat.values
    Amp=tideset.Amp.values
    Ph=tideset.Ph.values
    stavec=np.vstack((Lon,Lat)).T
    tidvec=np.vstack((Amp,Ph)).T
    return(stavec,tidvec)

def readaltidata(file):
    altdata=xr.open_dataset(file)
    lonsta=altdata.longitude.values
    latsta=altdata.latitude.values
    lonlatvec=np.vstack((lonsta,latsta)).T
    M2amp=altdata.Ampl_mean.values
    M2ph=altdata.Phase_mean.values
    #Coordinates anticlockwise from left bottom. Remember to update this based on new canada modelgrid.
    lon0,lat0=-157.5,50.39
    lon1,lat1=-47.1,50.39
    lon2,lat2=-47.1,83.21
    lon3,lat3=-157.5,83.21
    (svec,sM2amp)=snappingcanadagrid(lonlatvec,M2amp,lon0,lon1,lat0,lat2)
    (svec,sM2ph)=snappingcanadagrid(lonlatvec,M2ph,lon0,lon1,lat0,lat2)
    tidvec=np.vstack((sM2amp,sM2ph)).T
    return(svec,tidvec)


def gettriangulation(x,y):
    # Create the Triangulation; no triangles so Delaunay triangulation created.
    triang = tri.Triangulation(x, y)

    max_radius = 2
    triangles = triang.triangles
    # Mask off unwanted triangles. which have hypotenuse greater than 2.
    xtri = x[triangles] - np.roll(x[triangles], 1, axis=1)
    ytri = y[triangles] - np.roll(y[triangles], 1, axis=1)
    maxi = np.max(np.sqrt(xtri**2 + ytri**2), axis=1)
    triang.set_mask(maxi > max_radius)
    return(triang)

## but the issue is that model data is not always available at all the points. 
# so we need to snap the data such that all the points common to two models are there.
#This funcion snaps a vector say vec1 to locations in vec2. So for example in the case of Inger's altimetry data we had an issue 
# where altimetry didn't give good results at all the 2717 points. so she had results at 2610 points. This will help us get those 2610 points from 2717 points.

def snapstations(vec1,vec2,tidvec1,tidvec2,reltol):
    #vec2 one to compare to, one with lower number of values. 
    # vec1 the superset of vec2 # these are both n x 2 arrays x 2 are lon and lat respectively.
    # tidvec1 and tidvec2 are the amplitude and phase corresponding to vec1 and vec2 respectively.
    delindex=[]
    xvec1=[];yvec1=[]
    namp1=[];nph1=[]
    for i in range(len(vec2[:,0])):
        x=vec2[i,0];y=vec2[i,1]
        commonx=np.isclose(vec1[:,0],x,rtol=reltol,atol=0.0 )
        commony=np.isclose(vec1[:,1],y,rtol=reltol,atol=0.0)
        trueindexx=np.where(commonx==True)
        trueindexy=np.where(commony==True)
        index=(np.intersect1d(trueindexx,trueindexy))
        if len(index)==0:
            delindex=np.append(delindex,i)
            # print(delindex)
            continue
        else:
            index=int(index)                                  
        xvec1=np.append(xvec1,vec1[index,0])
        yvec1=np.append(yvec1,vec1[index,1])
        namp1=np.append(namp1,tidvec1[index,0])
        nph1=np.append(nph1,tidvec1[index,1])

    nvec1=np.vstack((xvec1,yvec1)).T    
    ntidvec1=np.vstack((namp1,nph1)).T 
    # removing the indices which didn't match with any.
    xvec2=np.delete(vec2[:,0],delindex.astype(int))
    yvec2=np.delete(vec2[:,1],delindex.astype(int))
    nvec2=np.vstack((xvec2,yvec2)).T  
    namp2=np.delete(tidvec2[:,0],delindex.astype(int))
    nph2=np.delete(tidvec2[:,1],delindex.astype(int))
    ntidvec2=np.vstack((namp2,nph2)).T     
    return (nvec1,nvec2,ntidvec1,ntidvec2)

def createNC(Amp,Ph,Lon,Lat,name):
    ds=xr.Dataset({'Amp':Amp,'Ph':Ph,'lon':Lon,'lat':Lat})
    ds.to_netcdf(name+'.nc')

 #here is obs is nx2 vector with lon and lat and obsname is name of the obs it could also be something like M2 amp or phase etc.

def snappingcanadagrid(obs,obsname,lon0,lon1,lat0,lat2): 
    nobs=np.zeros((2,1))
    nobsname=[]
    for i in range(len(obs[:,0])):
        if (lon0<=obs[i,0]<=lon1) and (lat0<=obs[i,1]<=lat2):
            nobs=np.append(nobs,[[obs[i,0]],[obs[i,1]]],axis=1)
            nobsname=np.append(nobsname,obsname[i])
    nobs=nobs[:,1:].T
    # print(nobs.shape)
    # print(nobsname.shape)
    return(nobs,nobsname)
