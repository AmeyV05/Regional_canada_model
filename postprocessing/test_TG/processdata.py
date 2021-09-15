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
# 1. FES2014, 2. Altimetry 3. Canada modelwFesb 4. Canada model wGTSMb  5. GTSM v4.1

# reading of the datasets.
# reading canada model w FES boundary
# locindex=(475+np.linspace(0,742,743)).astype(int)  
locindex=(1149+np.linspace(0,155,156)).astype(int) 
tideconst='M2'
#%%
#Standard model with SAL and TG and altimtry in his file.
modelffile=os.path.join(path1,'model_runs','cartesius_runs','test_3rd_boundary_runs','TGsalgtsmboundaryoutput','canada_model_0000_his.nc')
modelfdata=readdata.readmodel(modelffile,locindex)
#tidla analysis and conversion to NC
(M2AMf,M2PMf,Mflon,Mflat)=tideanalysis.tidalanalysis(modelfdata,tideconst)
readdata.createNC(M2AMf,M2PMf,Mflon,Mflat,'TGsalModelwgtsmb')



