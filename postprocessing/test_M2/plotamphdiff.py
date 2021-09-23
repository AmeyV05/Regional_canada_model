#%%
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on Tue Jul 06 2021 2:02:16 PM
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

def plotdiff(Lon,Lat,diffam,diffph,name):
    diffamrms = np.sqrt(np.mean(diffam**2))
    fig=plt.figure(figsize=(20,14),frameon=True)
    cmap='seismic'

    # title='M2amp'
    cbarlabel='Amplitude(m)'
    ax=fig.add_subplot(1,2,1,projection=ccrs.NorthPolarStereo(central_longitude=0.0,true_scale_latitude=None, globe=None)) 
    ax.set_extent((-158, -47, 49, 84), crs=ccrs.PlateCarree())
    feature=cpf.GSHHSFeature(scale='i',levels=[1],facecolor='black',alpha=1,edgecolor='none')
    ax.add_feature(feature)
    cont=plt.scatter(Lon,Lat,c=diffam,cmap=cmap,vmin=-0.25,vmax=0.25,transform=ccrs.PlateCarree())
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
    cont=plt.scatter(Lon,Lat,c=diffph,cmap=cmap,vmin=-100,vmax=100,transform=ccrs.PlateCarree())
    cbar=fig.colorbar(cont,fraction=0.078, pad=0.04)
    cbar.set_label(cbarlabel, rotation=90, fontsize=18) 
    cbar.ax.tick_params(labelsize=18)

    # ax.set_title(title)
    fig.suptitle('Difference of '+tideconst+'amp and phase ('+name+' ) RMSE:'+'%.4f' % diffamrms+'m', fontsize=20,y=0.91)
    fname=os.path.join(path1,'postprocessing','test_M2','figures',name+'.jpg')
    fig.savefig(fname,dpi=300)

#computing phase differences considering 360==0 phase idea from Inger.
def realphasediff(ph1,ph2):
    diff=np.empty((len(ph1)))
    for i in range(len(ph1)):
        if ph1[i]>270 and ph2[i]<90:
            diff[i]=-(360-ph1[i])-ph2[i]
        elif ph1[i]<90 and ph2[i]>270:
            diff[i]=(360-ph2[i])+ph1[i]
        else:
            diff[i]=ph1[i]-ph2[i]    
    return(diff)

def comparedatasets(Modstavec,Modtidvec,Obsstavec,Obstidvec,name):
    (nModstavec,nObsstavec,nModtidvec,nObstidvec)=readdata.snapstations(Modstavec,Obsstavec,Modtidvec,Obstidvec,1e-3)
    diffamfmwf=nModtidvec[:,0]-nObstidvec[:,0]
    diffphfmwf=realphasediff(nModtidvec[:,1],nObstidvec[:,1])
    plotdiff(nObsstavec[:,0],nObsstavec[:,1],diffamfmwf,diffphfmwf,name)

#%%
# compare the results with different datasets. We have 3 ets now:
# 1. FES2014, 2. Altimetry 3. GTSM v4.1

# reading of all these datasets. 

#FES data
fesfile=os.path.join(path1,'postprocessing','test_M2','ncdata','FESM2canada.nc')
(Fstavec,Ftidvec)=readdata.readtidedata(fesfile)

#GTSM data
gtsmfile=os.path.join(path1,'postprocessing','test_M2','ncdata','GTSMM2canada.nc')
(Gstavec,Gtidvec)=readdata.readtidedata(gtsmfile)

#Altimetry data
altfile=os.path.join(path1,'Altimetry_vanInger','ModM2Arctic_altimetry.nc')
(Astavec,Atidvec)=readdata.readaltidata(altfile)

#%%

#GTSM and FES current comparison. 
#model fes b

name='GTSM-FES'
comparedatasets(Gstavec,Gtidvec,Fstavec,Ftidvec,name)

# Now we compare our  model results. with each of these datasets and plot them. 
# For this we use the function above. 

# %%
# Standard model comparisons. 

# With FES boundary. 
# reading of the model results 
#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2fesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='sModelwFES-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='sModelwFES-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='sModelwFES-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)

#model with gtsm b

#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2gtsmb.nc')
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
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2ficefesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='ficeModelwFES-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='ficeModelwFES-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='ficeModelwFES-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)

#model with gtsm b

#model fes b
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2ficegtsmb.nc')
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
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2fice37fesb.nc')
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
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2noicenobottomfesb.nc')
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
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2fice18fesb.nc')
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
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2salfesb.nc')
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
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2salgtsmb.nc')
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
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2salbottomgtsmb.nc')
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
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2salbottomfesb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='SALbottom3ModelwFES-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='SALbottom3ModelwFES-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='SALbottom3ModelwFES-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)
print('done')

# %%
# %%
# model with standard model forcings and SAL but 0.1 bathymetry corr added
# With GTSM boundary. 
# reading of the model results 
#model gtsm
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2salbath0.1gtsmb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='SALbath0.1ModelwGTSM-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='SALbath0.1ModelwGTSM-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='SALbath0.1ModelwGTSM-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)
print('done')

# %%
# model with standard model forcings and SAL but 0.1 bathymetry corr added in part of HB
# With GTSM boundary. 
# reading of the model results 
#model gtsm
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2salbathHBgtsmb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='SALbathHBModelwGTSM-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='SALbathHBModelwGTSM-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='SALbathHBModelwGTSM-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)
print('done')

# %%
# model with standard model forcings and SAL but no 0.1 bathymetry corr added in part of HB
# With GTSM boundary. 
# reading of the model results 
#model gtsm
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2salnobathgtsmb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='SALnobathHBModelwGTSM-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='SALnobathHBModelwGTSM-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='SALnobathHBModelwGTSM-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)
print('done')

# %%
# model with standard model forcings and SAL but 0.1 bathymetry corr added in part of HB
# With GTSM boundary. 
# reading of the model results 
#model gtsm
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2salbathLAT0.1gtsmb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='SALbathLAT0.1ModelwGTSM-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='SALbathLAT0.1ModelwGTSM-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='SALbathLAT0.1ModelwGTSM-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)
print('done')
# %%
# model with standard model forcings and SAL but no 0.1 bathymetry corr added in part of HB
# With GTSM boundary. 
# reading of the model results 
#model gtsm
modelffile=os.path.join(path1,'postprocessing','test_M2','ncdata','ModM2vis2gtsmb.nc')
(Mfstavec,Mftidvec)=readdata.readtidedata(modelffile)

name='Vis2ModelwGTSM-FES'
comparedatasets(Mfstavec,Mftidvec,Fstavec,Ftidvec,name)

name='Vis2ModelwGTSM-GTSM'
comparedatasets(Mfstavec,Mftidvec,Gstavec,Gtidvec,name)

name='Vis2ModelwGTSM-Altimetry'
comparedatasets(Mfstavec,Mftidvec,Astavec,Atidvec,name)
print('done')
# %%
