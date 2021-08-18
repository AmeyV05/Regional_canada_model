#%%
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Created on Tue Jul 06 2021 5:28:28 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
This script takes the waterlevel data time and lon lat and performs a tidal analysis.
Once the analysis is done, the data is saved as a nc file for plotfunction to use. 
'''
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import numpy as np
import os
import xarray as xr
from postprocessing import readdata, tideanalysis

# compare the results with different datasets. We have 5 datasets now:
# 1. FEK1014, 2. Altimetry 3. Canada modelwFesb 4. Canada model wGTSMb  5. GTSM v4.1

# reading of the datasets.
# reading canada model w FES boundary
# locindex=(475+np.linspace(0,742,743)).astype(int)  
locindex=(406+np.linspace(0,742,743)).astype(int) 
tideconst='K1'
#%%
#Modelwfes data
modelffile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','fesboundaryoutput','canada_model_0000_his.nc')
modelfdata=readdata.readmodel(modelffile,locindex)
#tidla analysis and conversion to NC
(K1AMf,K1PMf,Mflon,Mflat)=tideanalysis.tidalanalysis(modelfdata,tideconst)
readdata.createNC(K1AMf,K1PMf,Mflon,Mflat,'ModK1fesb')

#%%
# # reading FES data.
fesfile=os.path.join(path1,'FESCanada','Altimetry_boundary_obs','January2013','fes_boundary_altimetry.nc')
fesdata=readdata.readfes(fesfile,locindex)
#tidal analysis and conversion to NC

(K1AF,K1PF,Flon,Flat)=tideanalysis.tidalanalysis(fesdata,tideconst)
readdata.createNC(K1AF,K1PF,Flon,Flat,'FESK1canada')

#%%
#GTSM data
gtsmfile=os.path.join(path1,'gtsm_runs','Jan2013v4.1_3dmodel','gtsm_model_0000_his.nc')
gtsmdata=readdata.readmodel(gtsmfile,locindex)
# # tidal analysis and conversion of to NC file. 
(K1AG,K1PG,Glon,Glat)=tideanalysis.tidalanalysis(gtsmdata,tideconst)
readdata.createNC(K1AG,K1PG,Glon,Glat,'GTSMK1canada')

#%%
#Modelwgtsm data
modelgfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','gtsmboundaryoutput','canada_model_0000_his.nc')
modelgdata=readdata.readmodel(modelgfile,locindex)
#tidla analysis and conversion to NC
(K1AMg,K1PMg,Mglon,Mglat)=tideanalysis.tidalanalysis(modelgdata,tideconst)
readdata.createNC(K1AMg,K1PMg,Mglon,Mglat,'ModK1gtsmb')

#%%
#fastice runs without bottom correction from xiaohui. 

#Modelwfes boundary data
modelgfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','ficefesboundaryoutput','canada_model_0000_his.nc')
modelgdata=readdata.readmodel(modelgfile,locindex)
#tidla analysis and conversion to NC
(K1AMg,K1PMg,Mglon,Mglat)=tideanalysis.tidalanalysis(modelgdata,tideconst)
readdata.createNC(K1AMg,K1PMg,Mglon,Mglat,'ModK1ficefesb')
print('done')

# %%
#%%
#fastice runs without bottom correction from xiaohui. 

#Modelwfes boundary data
modelgfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','ficegtsmboundaryoutput','canada_model_0000_his.nc')
modelgdata=readdata.readmodel(modelgfile,locindex)
#tidla analysis and conversion to NC
(K1AMg,K1PMg,Mglon,Mglat)=tideanalysis.tidalanalysis(modelgdata,tideconst)
readdata.createNC(K1AMg,K1PMg,Mglon,Mglat,'ModK1ficegtsmb')
print('done')
# %%

#Modelwfes boundary data and no ice and no bottom friction calibration
modelfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','noicenobottomfesboundaryoutput','canada_model_0000_his.nc')
modeldata=readdata.readmodel(modelfile,locindex)
#tidla analysis and conversion to NC
(K1AMg,K1PMg,Mglon,Mglat)=tideanalysis.tidalanalysis(modeldata,tideconst)
readdata.createNC(K1AMg,K1PMg,Mglon,Mglat,'ModK1noicenobottomfesb')


#%%

#Modelwfes boundary data and fast ice but with larger drag coefficient of 37.
modelgfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','fice_37fesboundaryoutput','canada_model_0000_his.nc')
modelgdata=readdata.readmodel(modelgfile,locindex)
#tidla analysis and conversion to NC
(K1AMg,K1PMg,Mglon,Mglat)=tideanalysis.tidalanalysis(modelgdata,tideconst)
readdata.createNC(K1AMg,K1PMg,Mglon,Mglat,'ModK1fice37fesb')


#%%

#Modelwfes boundary data and fast ice but with larger drag coefficient of 18
modelgfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','fice_18fesboundaryoutput','canada_model_0000_his.nc')
modelgdata=readdata.readmodel(modelgfile,locindex)
#tidla analysis and conversion to NC
(K1AMg,K1PMg,Mglon,Mglat)=tideanalysis.tidalanalysis(modelgdata,tideconst)
readdata.createNC(K1AMg,K1PMg,Mglon,Mglat,'ModK1fice18fesb')
# %%
#%%

#Modelwfes boundary data and sal (standard model with sal)
modelgfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','salfesboundaryoutput','canada_model_0000_his.nc')
modelgdata=readdata.readmodel(modelgfile,locindex)
#tidla analysis and conversion to NC
(K1AMg,K1PMg,Mglon,Mglat)=tideanalysis.tidalanalysis(modelgdata,tideconst)
readdata.createNC(K1AMg,K1PMg,Mglon,Mglat,'ModK1salfesb')
# %%

#Modelwgtsm boundary data and sal (standard model with sal)
modelgfile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','salgtsmboundaryoutput','canada_model_0000_his.nc')
modelgdata=readdata.readmodel(modelgfile,locindex)
#tidla analysis and conversion to NC
(K1AMg,K1PMg,Mglon,Mglat)=tideanalysis.tidalanalysis(modelgdata,tideconst)
readdata.createNC(K1AMg,K1PMg,Mglon,Mglat,'ModK1salgtsmb')
print('done')
# %%
