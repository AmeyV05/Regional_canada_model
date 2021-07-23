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

#reading the his model file.
#fes boundary
# modelfile=os.path.join('..','model_runs','cartesius_runs','test_boundary_runs','output','canada_model_0000_his.nc')
# gtsm boundary
# modelfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','fesboundaryoutput','canada_model_0000_his.nc')
modelfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','gtsmboundaryoutput','canada_model_0000_his.nc')
# locindex=(np.linspace(0,474,475)).astype(int)
locindex=(np.linspace(0,405,406)).astype(int)
moddata=readdata.readmodel(modelfile,locindex)

# #reading fes data on boundary.
fesboundfile=os.path.join(path1,'FESCanada','fes10km_5e-2_2_obs.nc')
fesdata=readdata.readfes(fesboundfile,locindex)

# reading gtsm run boundary data.
gtsmboundfile=os.path.join(path1,'gtsm_runs','Jan2013v4.1_3dmodel','gtsm_model_0000_his.nc')
gtsmdata=readdata.readmodel(gtsmboundfile,locindex)

#plotting the animation of boundary values at a certain timeinstant. 

fig=plt.figure()
# ax=plt.axes(xlim=(0,475),ylim=(-2,2))
ax=plt.axes(xlim=(0,406),ylim=(-2,2))
line1,=ax.plot([],[],label='model')
# line2,=ax.plot([],[],label='FES2014')
line2,=ax.plot([],[],label='GTSM')
title=ax.set_title('Waterlevel at water boundary points at '+'')
plt.legend()

def init():
    line1.set_data([],[])
    line2.set_data([],[])
    title.set_text('')
    return(line1,line2,title)
# j=0
def animate(j):
    timeinstant=moddata['time'][j]
    # getting the mean of the differences between model and fes.
    diffti=moddata['h'][j,:]-fesdata['h'][j,:]
    # diffti=moddata['h'][j,:]-gtsmdata['h'][j,:]
    index=np.where(diffti>1.)
    modelssh=moddata['h'][j,:]
    modelssh=np.delete(modelssh,index)
    # fesssh=fesdata['h'][j,:]
    # fesssh=np.delete(fesssh,index)
    gtsmssh=gtsmdata['h'][j,:]
    gtsmssh=np.delete(gtsmssh,index)
    line1.set_data(np.delete(locindex,index),modelssh)
    # line2.set_data(np.delete(locindex,index),fesssh)
    line2.set_data(np.delete(locindex,index),gtsmssh)
    title.set_text(str(timeinstant))
    return(line1,line2,)

FFWriter=animation.FFMpegWriter(extra_args=['-vcodec', 'libx264'])
anim=animation.FuncAnimation(fig,animate,init_func=init,frames=3000,interval=20,blit=True)
anim.save('postprocessing/test_boundary/gtsmwaterlevel_waterboundary.mp4',writer=FFWriter)
# anim.save('postprocessing/test_boundary/feswaterlevel_waterboundary.mp4',writer=FFWriter)
# plt.show()


def plttiboundary(moddata,fesdata,gtsmdata,j,locindex):
    timeinstant=moddata['time'][j]
    diffti=moddata['h'][j,:]-fesdata['h'][j,:]
    # diffti=moddata['h'][j,:]-gtsmdata['h'][j,:]
    index=np.where(diffti>4.)
    print(index)
    modelssh=moddata['h'][j,:]
    modelssh=np.delete(modelssh,index)
    # fesssh=fesdata['h'][j,:]
    # fesssh=np.delete(fesssh,index)
    gtsmssh=gtsmdata['h'][j,:]
    gtsmssh=np.delete(gtsmssh,index)
    fig=plt.figure()
    plt.plot(np.delete(locindex,index),modelssh,label='model')
    plt.plot(np.delete(locindex,index),gtsmssh,label='GTSM')
    # plt.plot(np.delete(locindex,index),fesssh,label='FES2014')
    plt.legend()
    plt.xlabel('Boundary points')
    plt.ylabel('Waterlevel (m)')
    plt.title('Waterlevel at water boundary points at '+str(timeinstant))
    # fig.savefig(path1+'postprocessing/test_boundary/gtsmWaterlevel_water_all_boundary_'+str(j)+'.jpg')
    fig.savefig(path1+'postprocessing/test_boundary/gtsmWaterlevel_water_all_boundary_'+str(j)+'.jpg')

def plttinstant(moddata,fesdata,gtsmdata,j,locindex):
    # timeinstant=moddata['time'][j]
    # diffti=moddata['h'][j,:]-fesdata['h'][j,:]
    # # diffti=moddata['h'][j,:]-gtsmdata['h'][j,:]
    # index=np.where(diffti>1.)
    # modelssh=moddata['h'][j,:]
    # modelssh=np.delete(modelssh,index)
    # # fesssh=fesdata['h'][j,:]
    # # fesssh=np.delete(fesssh,index)
    # gtsmssh=gtsmdata['h'][j,:]
    # gtsmssh=np.delete(gtsmssh,index)
    fig=plt.figure()
    plt.plot(moddata['h'][:,j],label='model')
    plt.plot(gtsmdata['h'][:,j],label='GTSM')
    # plt.plot(fesdata['h'][:,j],label='FES')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Waterlevel (m)')
    plt.title('Waterlevel at boundary point of'+str(j))
    fig.savefig(path1+'postprocessing/test_boundary/gtsmWaterlevel_water_boundary_pt'+str(j)+'.jpg')



#%%
j=144*7 #time
i=144  # boundary point
plttinstant(moddata,fesdata,gtsmdata,i,locindex)
plttiboundary(moddata,fesdata,gtsmdata,j,locindex)

print("done")






# %%
