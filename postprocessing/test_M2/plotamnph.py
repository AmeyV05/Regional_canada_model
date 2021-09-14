#%%
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on Wed Sep 08 2021 7:50:26 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme("paper")
import os
from postprocessing import readdata 
import cartopy.crs as ccrs
import cartopy.feature as cpf 

tideconst='M2'

#defining the plot function.

def plotamph(Lon,Lat,am,ph,name):
    fig=plt.figure(figsize=(20,14),frameon=True)
    cmap='viridis'

    # title='M2amp'
    cbarlabel='Amplitude(m)'
    ax=fig.add_subplot(1,2,1,projection=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)) 
    ax.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
    ax.add_feature(feature)
    cont=plt.scatter(Lon,Lat,c=am,cmap=cmap,vmin=0,vmax=2.0,transform=ccrs.PlateCarree())
    cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
    cbar.set_label(cbarlabel, rotation=90, fontsize=18)
    cbar.ax.tick_params(labelsize=18)
    # Phase subplot
    level=50.
    # title='M2ph'
    cbarlabel='Phase(deg)'
    ax=fig.add_subplot(1,2,2,projection=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)) 
    ax.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
    ax.add_feature(feature)
    cont=plt.scatter(Lon,Lat,c=ph,cmap=cmap,vmin=0,vmax=360,transform=ccrs.PlateCarree())
    cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
    cbar.set_label(cbarlabel, rotation=90, fontsize=18) 
    cbar.ax.tick_params(labelsize=18)

    # ax.set_title(title)
    fig.suptitle(tideconst+'amp and phase ('+name+' ) ', fontsize=20,y=0.91)
    fname=os.path.join(path1,'postprocessing','test_M2','figures',name+'.jpg')
    fig.savefig(fname,dpi=300)



#%%
# compare the results with different datasets. We have 3 ets now:
# 1. FES2014, 2. Altimetry 3. GTSM v4.1

# reading of all these datasets. 

#FES data
fesfile=os.path.join(path1,'postprocessing','test_M2','FESM2canada.nc')
(Fstavec,Ftidvec)=readdata.readtidedata(fesfile)
name='FES'
plotamph(Fstavec[:,0],Fstavec[:,1],Ftidvec[:,0],Ftidvec[:,1],name)

#%%

#GTSM data
gtsmfile=os.path.join(path1,'postprocessing','test_M2','GTSMM2canada.nc')
(Gstavec,Gtidvec)=readdata.readtidedata(gtsmfile)
name='GTSM'
plotamph(Gstavec[:,0],Gstavec[:,1],Gtidvec[:,0],Gtidvec[:,1],name)

#Altimetry data
altfile=os.path.join(path1,'Altimetry_vanInger','ModM2Arctic_altimetry.nc')
(Astavec,Atidvec)=readdata.readaltidata(altfile)
name='Altimetry'
plotamph(Astavec[:,0],Astavec[:,1],Atidvec[:,0],Atidvec[:,1],name)



# %%
# Standard model comparisons. 

# With FES boundary. 
# reading of the model results 
#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2fesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)
name='SModelwFES'
plotamph(Mfstavec[:,0],Mfstavec[:,1],Mftidvec[:,0],Mftidvec[:,1],name)

#%%
#model with gtsm b

#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2gtsmb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='sModelwGTSM-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='sModelwGTSM-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='sModelwGTSM-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)

#%%
# Model with fast ice and no bottom friction calibration from xiaohui. 

# With FES boundary. 
# reading of the model results 
#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2ficefesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='ficeModelwFES-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='ficeModelwFES-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='ficeModelwFES-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)

#model with gtsm b

#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2ficegtsmb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='ficeModelwGTSM-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='ficeModelwGTSM-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='ficeModelwGTSM-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)

#%%

# Model with fast ice and no bottom friction calibration from xiaohui
# # but with different drag coefficient of 37

# With FES boundary. 
# reading of the model results 
#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2fice37fesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='fice37ModelwFES-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='fice37ModelwFES-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='fice37ModelwFES-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)

#%%
#model with fes boundary and no ice and no bottom friction calibration. 

#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2noicenobottomfesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='noicenobottomModelwFES-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='noicenobottomModelwFES-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='noicenobottomModelwFES-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)
print('done')

#%%

# Model with fast ice and no bottom friction calibration from xiaohui
# # but with different drag coefficient of 18

# With FES boundary. 
# reading of the model results 
#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2fice18fesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='fice18ModelwFES-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='fice18ModelwFES-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='fice18ModelwFES-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)
print('done')

# %%
# model with standard model forcings and SAL
# With FES boundary. 
# reading of the model results 
#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2salfesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='SALModelwFES-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='SALModelwFES-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='SALModelwFES-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)
print('done')

# %%
# model with standard model forcings and SAL
# With GTSM boundary. 
# reading of the model results 
#model gtsm
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2salgtsmb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='SALModelwGTSM-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='SALModelwGTSM-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='SALModelwGTSM-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)
print('done')
# %%
# model with standard model forcings and SAL but different friction coeff for HB HS UB 
# With GTSM boundary. 
# reading of the model results 
#model gtsm
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2salbottomgtsmb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='SALbottom1ModelwGTSM-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='SALbottom1ModelwGTSM-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='SALbottom1ModelwGTSM-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)
print('done')


# %%
# model with standard model forcings and SAL but different friction coeff for HB HS UB 
# With FES boundary. 
# reading of the model results 
#model gtsm
modelffile=os.path.join(path1,'postprocessing','test_M2','ModM2salbottomfesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='SALbottom3ModelwFES-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='SALbottom3ModelwFES-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='SALbottom3ModelwFES-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)
print('done')

# %%
