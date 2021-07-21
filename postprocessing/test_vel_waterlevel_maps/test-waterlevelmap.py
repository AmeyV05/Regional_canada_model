#%%
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on Mon Jul 05 2021 3:13:13 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/postprocessing/')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import cartopy.crs as ccrs
import cartopy.feature as cpf 
import seaborn as sns
sns.set_theme("paper")
import os
import xarray as xr
import readdata

#reading map merged model file.
# mapfile=os.path.join('..','model_runs','cartesius_runs','test_boundary_runs','output','canada_model_merged_map.nc')
mapfile=os.path.join('model_runs','cartesius_runs','test_boundary_runs','gtsmboundaryoutput','canada_model_merged_map.nc')
mapdata=readdata.readmodelmap(mapfile)

lon=mapdata['lon']
lat=mapdata['lat']
h=mapdata['h']
time=mapdata['time']
##plotting of waterlevel map and animation using triangulations.
j=24*7
triang=readdata.gettriangulation(lon,lat)
proj=ccrs.NorthPolarStereo(central_longitude=-45.0,true_scale_latitude=None, globe=None)
fig=plt.figure(figsize=(12, 12), frameon=True)

ax1=fig.add_subplot(1,1,1,projection=proj) 
ax1.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())
feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
ax1.add_feature(feature)
contour_opts = {'levels': np.linspace(-2,2,50),
                'cmap':'jet','transform':ccrs.PlateCarree()}
cont=ax1.tricontourf(triang,h[j,:],**contour_opts)
fig.colorbar(cont)
title=ax1.set_title('Waterlevel map at'+str(time[j]))
fig.savefig('postprocessing/test_vel_waterlevel_maps/gtsmwaterlevel_'+str(j)+'.jpg',dpi=1000)
print('done')

##failed animation attempt!!! ignore! or find a solution to it.
# def init():
#     cont.set_array([])
#     title.set_text('')
#     return(title,cont,)
# # j=0
# def animate(j):
#     # global cont, title
#     ax1=fig.add_subplot(1,1,1,projection=proj) 
#     ax1.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())
#     feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
#     ax1.add_feature(feature)
#     ax1.collections=[]
#     timeinstant=time[j]
#     hj=h[j,:]

#     contour_opts = {'levels': 20,
#                     'cmap':'jet','transform':ccrs.PlateCarree()}
#     cont=ax1.tricontourf(triang,h[j,:],**contour_opts)
#     fig.colorbar(cont)
#     # title=ax1.set_title('Waterlevel map at'+str(time[0]))
#     ax1.set_title('Waterlevel map at'+str(timeinstant))

#     return [ax1,] 
# # artists=[]
# # for j in range(len(time[:101])):
# #     cont=ax1.tricontourf(triang,h[j,:],levels=50,cmap='jet',transform=ccrs.PlateCarree())
# #     title=ax1.set_title('Waterlevel map at'+str(time[j]))
# #     artists.append(cont.collections)

# FFWriter=animation.FFMpegWriter(fps=1,extra_args=['-vcodec', 'libx264'])
# anim=animation.FuncAnimation(fig,animate,frames=10,blit=True)
# anim.save('test_vel_waterlevel_maps/waterlevel_map.mp4',writer=FFWriter)
# print('done')

# %% Matplotlib plot
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,20,199)
plt.plot(x,np.sin(x))
plt.show()

# %%
