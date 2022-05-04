#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
This is a script made to quickly check which points are contained in a ice polygon from the fibnacci grid,
On jupyter it is super slow so created here. 
Created on Mon May 02 2022 1:08:37 PM
@Author: Amey Vasulkar
Copyright (c) 2022 Deltares
'''
#basic importing
import os
import sys
path1=sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point, MultiPolygon, shape
import shapefile

import cartopy.crs as ccrs
import cartopy.feature as cpf 
from global_land_mask import globe
import pandas as pd
import pyproj
from osgeo import ogr
from osgeo import gdal
import fiona
from shapely.geometry import shape,mapping, Point, Polygon, MultiPolygon
gdal.UseExceptions()
from pyproj import Proj, transform
from cartopy.feature import ShapelyFeature

#reading fibonacci points

fname='modelpoints_fb_fine.xyz'
headerlist=['Lon','Lat','pname']
df=pd.read_csv(fname,names=headerlist,delim_whitespace=True)
df.head()
finemodoceanlonpointvec=np.array(df['Lon'])
finemodoceanlatpointvec=np.array(df['Lat'])

#reading ice polygon buffer file
#get the projected buff file which gives us the polygon on ice cover. 
#now depending on march and september we have different files. Also, for march we will have the friction term too.
month='Mar'
typ='all_ice'
if month=='Sep':
    # prjbuffile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/Icedata/nh_20200917/tc_mid/Buffer_proj.shp'
    # buffile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/Icedata/nh_20200917/tc_mid/Buffer.shp'
    prjbuffile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/Icedata/nh_20200917/all_ice/Buffer_proj.shp'
    buffile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/Icedata/nh_20200917/all_ice/Buffer.shp'

else:
    buffile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/Icedata/nh_20200313/tc_mid/Buffer.shp'
    prjbuffile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/Icedata/nh_20200313/tc_mid/Buffer_proj.shp'
    if typ=='all_ice':
    #all ice
        prjbuffile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/Icedata/nh_20200313/all_ice/Buffer_proj.shp'
        buffile='/u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/Icedata/nh_20200313/all_ice/Buffer.shp'
# reader=shapefile.Reader(buffile)
# multipol=shape(reader.shape())
multipolcollection = fiona.open(buffile)
# multipolprj=fiona.open(prjbuffile)
for record in multipolcollection:
    multipol= shape(record['geometry'])   # only one feature in the shapefile

#checking which points lie in the polygon and giving those points a param id of 1.
#check if a point lies in sea ice polygon. If so, give the point a param id of 1 and else a param id of 100.  
paramid=[]
inProj = Proj(init='epsg:4326', preserve_units=True)
outProj = Proj(init='epsg:6931')
for i in range(len(finemodoceanlatpointvec)):
    x2,y2 = transform(inProj,outProj,finemodoceanlonpointvec[i],finemodoceanlatpointvec[i])
    point=shape(Point(x2,y2))
    # print(point)
    if point.within(multipol.buffer(0)):
        paramid=np.append(paramid,1)
        
        # inicelon=np.append(inicelon,finemodoceanlonpointvec[i])
        # inicelat=np.append(inicelat,finemodoceanlatpointvec[i])
        # count+=1
    else:
        paramid=np.append(paramid,100)
    print(i)
#now based on paramid, we  get the index of all the inpolygon points.

# inicepolindex=np.where(paramid==1.)[0]

#plotting to verify
# fig=plt.figure(figsize=(20, 14), frameon=True)
# # proj=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)
# proj=ccrs.PlateCarree()
# ax1=fig.add_subplot(1,1,1,projection=proj) 
# ax1.set_extent((-158, -46, 49, 84.7), crs=ccrs.PlateCarree())
# ax1.scatter(finemodoceanlonpointvec[inicepolindex],finemodoceanlatpointvec[inicepolindex],transform=ccrs.PlateCarree(),s=200)
# # ax1.legend()
# shape_feature = ShapelyFeature(multipol.buffer(0), ccrs.LambertAzimuthalEqualArea(central_latitude=90.0), facecolor="lime", edgecolor='black',alpha=0.2)
# ax1.add_feature(shape_feature)
# feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='grey',alpha=1)
# ax1.add_feature(feature)
# ax1.scatter(finemodoceanlonpointvec,finemodoceanlatpointvec,transform=ccrs.PlateCarree(),s=3)
# fig.savefig('Icedata/ice_poly_march.jpg',dpi=1000)

#saving the file as .xyz so that don't have to run the slow code agaib.

#since the above in polygon check takes a lot of time. we just save the generated file so as to not have  to run it again and again.
# vec=np.vstack((oceanpointlonvec,oceanpointlatvec))
vec=np.vstack((finemodoceanlonpointvec,finemodoceanlatpointvec))
# paraidvec=1*(np.ones(len(oceanpointlonvec))).astype(int)
vec=np.vstack((vec,paramid.reshape((1,len(paramid)))))
np.savetxt('icepolygonpoints_march_14.xyz',vec.T,fmt=['%0.5f','%0.5f','%d'],delimiter='\t')