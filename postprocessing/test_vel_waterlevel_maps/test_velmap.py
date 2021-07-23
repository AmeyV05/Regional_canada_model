#%%
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on Mon Jul 05 2021 5:56:04 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''

import sys
from matplotlib import animation
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import cartopy.crs as ccrs
import cartopy.feature as cpf 
import seaborn as sns
sns.set_theme("paper")
import os
import xarray as xr
from postprocessing import readdata
from scipy.interpolate import griddata

#reading map merged model file.
# mapfile=os.path.join(path1,'model_runs','cartesius_runs','test_boundary_runs','fesboundaryoutput','canada_model_merged_map.nc')
# mapfile=os.path.join(path1,'model_runs','cartesius_runs','test_boundary_runs','gtsmboundaryoutput','canada_model_merged_map.nc')
mapfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','fesboundaryoutput','canada_model_merged_map.nc')
mapdata=readdata.readmodelmap(mapfile)

lon=mapdata['lon']
lat=mapdata['lat']
u=mapdata['u']
v=mapdata['v']
time=mapdata['time']

# processing the velocity vector data to interpolate it to a grid,
lonmin=lon.min();lonmax=lon.max()
print(lonmin,lonmax)
latmin=lat.min();latmax=lat.max()
print(latmin,latmax)
lonvec=np.linspace(lonmin,lonmax,200);latvec=np.linspace(latmin,latmax,150)
longrid,latgrid=np.meshgrid(lonvec,latvec)

j=24*8
ugrid=griddata((lon,lat),u[j,:],(longrid,latgrid),method='linear',fill_value=np.nan)
vgrid=griddata((lon,lat),v[j,:],(longrid,latgrid),method='linear',fill_value=np.nan)
umag=np.sqrt(ugrid**2+vgrid**2)
umag.shape
##plotting of velocity magnitude map and quiver using triangulations and interpolations

triang=readdata.gettriangulation(lon,lat)
proj=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)
skip=(slice(None,None,5),slice(None,None,5))
# norm = mcolors.Normalize(vmin=0.,vmax=0.7,clip=False)
# cmap = mcolors.ListedColormap(plt.cm.jet(np.linspace(0,1,20)), "name")

# x, y, _= proj.transform_points(ccrs.PlateCarree(), xflowem, yflowem).T
# mask = np.invert(np.logical_or(np.isinf(x), np.isinf(y)))
# x = np.compress(mask, x)
# y = np.compress(mask, y)
fig=plt.figure(figsize=(12, 12), frameon=True)

ax1=fig.add_subplot(1,1,1,projection=proj) 
ax1.set_extent((-158, -47, 45, 84), crs=ccrs.PlateCarree())
feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
ax1.add_feature(feature)
cont=ax1.contourf(longrid,latgrid,umag,levels=np.linspace(0,0.3,50),cmap='jet',transform=ccrs.PlateCarree())
#below quiver is good for colored vectors
# quiv=ax1.quiver(longrid[skip],latgrid[skip],ugrid[skip],vgrid[skip],colors[skip],transform=ccrs.PlateCarree(),units='xy',cmap=cmap,norm=norm,scale_units='width')
quiv=ax1.quiver(longrid[skip],latgrid[skip],ugrid[skip],vgrid[skip],transform=ccrs.PlateCarree(),units='xy',scale_units='width',color='white')
fig.colorbar(cont)
fig.savefig(path1+'postprocessing/test_vel_waterlevel_maps/velocity_'+str(j)+'.jpg',dpi=1000)
print('done')

# %%
