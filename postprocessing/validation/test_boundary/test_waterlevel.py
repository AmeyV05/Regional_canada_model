#%%
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 14:47:57 2021

@author: vasulkar a n

Testing the water level on boundaries. 
This script reads the boundaries from the Regional canada model runs
and compares it to FES runs.
"""
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn as sns
sns.set_theme("paper")
import os
import xarray as xr
from postprocessing import readdata


# locindex=(np.linspace(0,474,475)).astype(int)
locindex=(np.linspace(0,405,406)).astype(int)
# this indexing gets only the boundary data from the observation files. 

# Functions which run based on modeldata and obsdata. So obsdata can be GTSM or FEs for example.
# type is the name of the obsdata it could be FES2014 or GTSM only
def doanimation(modeldata,obsdata,type,locindex,nframes):
    #plotting the animation of boundary values at a certain timeinstant. 
    fig=plt.figure()
    # ax=plt.axes(xlim=(0,475),ylim=(-2,2))
    ax=plt.axes(xlim=(0,406),ylim=(-2,2))
    line1,=ax.plot([],[],label='model')
    line2,=ax.plot([],[],label=type)
    title=ax.set_title('Waterlevel on water boundary points at '+'')
    plt.legend()

    def init():
        line1.set_data([],[])
        line2.set_data([],[])
        title.set_text('')
        return(line1,line2,title)
    def animate(j):
        timeinstant=modeldata['time'][j]
        # getting the mean of the differences between model and obs.
        diffti=modeldata['h'][j,:]-obsdata['h'][j,:]
        index=np.where(diffti>1.)
        modelssh=modeldata['h'][j,:]
        modelssh=np.delete(modelssh,index)
        obsssh=obsdata['h'][j,:]
        obsssh=np.delete(obsssh,index)
        line1.set_data(np.delete(locindex,index),modelssh)
        line2.set_data(np.delete(locindex,index),obsssh)
        title.set_text(str(timeinstant))
        return(line1,line2,)

    FFWriter=animation.FFMpegWriter(extra_args=['-vcodec', 'libx264'])
    anim=animation.FuncAnimation(fig,animate,init_func=init,frames=nframes,interval=30,blit=True)
    anim.save('postprocessing/validation/test_boundary/'+type+'waterlevel_waterboundary.mp4',writer=FFWriter)

def plttiboundary(modeldata,obsdata,type,j,locindex):
    timeinstant=modeldata['time'][j]
    diffti=modeldata['h'][j,:]-obsdata['h'][j,:]
    index=np.where(diffti>4.)
    print(index)
    modelssh=modeldata['h'][j,:]
    modelssh=np.delete(modelssh,index)
    obsssh=obsdata['h'][j,:]
    obsssh=np.delete(obsssh,index)
    fig=plt.figure()
    plt.plot(np.delete(locindex,index),modelssh,label='model')
    plt.plot(np.delete(locindex,index),obsssh,label=type)
    plt.legend()
    plt.xlabel('Boundary points')
    plt.ylabel('Waterlevel (m)')
    plt.title('Waterlevel at water boundary points at '+str(timeinstant))
    fig.savefig(path1+'postprocessing/validation/test_boundary/'+type+'waterlevel_water_all_boundary_'+str(j)+'.jpg')

def plttinstant(modeldata,obsdata,type,j):
    fig=plt.figure()
    plt.plot(modeldata['h'][:,j],label='model')
    plt.plot(obsdata['h'][:,j],label=type)
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Waterlevel (m)')
    plt.title('Waterlevel at boundary point of'+str(j))
    fig.savefig(path1+'postprocessing/validation/test_boundary/'+type+'waterlevel_water_boundary_pt'+str(j)+'.jpg')

#%%
#reading files for data..
# FES boundary
# model versus fes

# modelfile=os.path.join('..','model_runs','cartesius_runs','test_boundary_runs','output','canada_model_0000_his.nc')
# modelfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','fesboundaryoutput','canada_model_0000_his.nc')
modelfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','ficefesboundaryoutput','canada_model_0000_his.nc')
moddata=readdata.readmodel(modelfile,locindex)

# #reading fes data on boundary.
fesboundfile=os.path.join(path1,'FESCanada','fes10km_5e-2_2_obs.nc')
fesdata=readdata.readfes(fesboundfile,locindex)


j=144*7 #time
i=144  # boundary point
type='FES'
plttiboundary(moddata,fesdata,type,j,locindex)
plttinstant(moddata,fesdata,type,i)
doanimation(moddata,fesdata,type,locindex,3000)
# print('done')
#%%

# gtsm boundary
modelfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','ficegtsmboundaryoutput','canada_model_0000_his.nc')
moddata=readdata.readmodel(modelfile,locindex)

# GTSM data. 
# reading gtsm run boundary data.
gtsmboundfile=os.path.join(path1,'gtsm_runs','Jan2013v4.1_3dmodel','gtsm_model_0000_his.nc')
gtsmdata=readdata.readmodel(gtsmboundfile,locindex)

# model versus gtsm
j=144*7 #time
i=144  # boundary point
type='GTSM'
plttiboundary(moddata,gtsmdata,type,j,locindex)
plttinstant(moddata,gtsmdata,type,i)
doanimation(moddata,gtsmdata,type,locindex,3000)

#%%
print("done")






# %%
