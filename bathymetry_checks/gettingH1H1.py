#%%
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Getting the H1 and H2 amplitudes from CHS. 
Created on Thu Aug 19 2021 7:12:03 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
import numpy as np 
import sys
sys.path.append('/u/vasulkar/p_emodnet_amey/Regional_canada_model/')
path1=sys.path[-1]
import xarray as xr
from postprocessing import tideanalysis
from bathymetry_checks import readchsdata
import time
from matplotlib.dates import date2num
import utide
# import sys
# old_stdout = sys.stdout

# log_file = open("message.log","w")

# sys.stdout = log_file
sdate='2020-01-01T00:00:00Z'  # sdate of all data
edate='2021-01-01T00:00:00Z'  # end date of all data.

#reading all station metadata.

stationjsonfile='bathymetry_checks/chsstations.json'
# stationjsonfile='chsstations.json'
(allstationinfodata,stationamevec,stationidvec,stationlonvec,stationlatvec)=readchsdata.getallstationmetadata(stationjsonfile)

#%%
# for each station.

def getwldata(sdate,edate,stationid,stationlon,stationlat):
    data={}
    (Tlvec,Wlvec)=readchsdata.getmergedata(sdate,edate,stationid)      
    data['time']=Tlvec,
    data['h']=Wlvec
    data['lon']=stationlon
    data['lat']=stationlat
    print(np.shape(Wlvec))
    print(np.shape(Tlvec))
    return(data)


i=32
print(i)
amp=[];ph=[]
stationlon=[stationlonvec[i]]
stationlat=[stationlatvec[i]]
stationid=stationidvec[i]
(data)=getwldata(sdate,edate,stationid,stationlon,stationlat)
sshi=np.array((data['h']))

ti=data['time']
timedatnum=np.array((date2num(ti))).flatten()
vec=np.hstack((timedatnum.reshape(len(timedatnum),1),sshi.reshape(len(sshi),1)))
np.savetxt('bathymetry_checks/'+stationamevec[i]+'wl.txt',vec,fmt='%s',delimiter="\t")

#%%
# create NC file
i=32
stationlon=[stationlonvec[i]]
stationlat=[stationlatvec[i]]
stationid=stationidvec[i]
wldatatxt = np.loadtxt('bathymetry_checks/'+stationamevec[i]+'wl.txt',dtype='float')

const1=['M2','H2','H1']
# const1=['M2']
const=['K1','O1','Q1', 'P1','N2','M2','S2','K2','H2','H1']
epoch1='1970-01-01'
# tidalconst=tideconst
timedatnum=np.array(wldatatxt[:,0])
sshi=np.array(wldatatxt[:,1])
coef = utide.solve(timedatnum,sshi,lat=stationlat[0],
                    epoch=epoch1,
                    constit=const,
                    conf_int='linear',
                    trend=False,
                    white=True,
                    method='ols')
Amp=coef['A']
Ph=coef['g']
name=coef['name']
ampvec=[];phvec=[]
for tidconst in const1:
    j=np.where(name==tidconst)
    print(j)
    amp=Amp[j]
    ampvec=np.append(ampvec,amp) 
    ph=Ph[j]
    phvec=np.append(phvec,ph)
# (Am,Ph)=tideanalysis.compute1stationtidal(data,tideconst)
    print(tidconst+' tide constituent values are:'+str(amp)+', '+str(ph))

#%%
#reconstruct
#basic idea of what i did.
# tvec=np.arange(len(timedatnum))
# OM2=2*np.pi/(12.42*4)
# OH1=2*np.pi/(12.438*4)
# OH2=2*np.pi/(12.403*4)
# reconstrucsignal=(ampvec[0]*np.cos(OM2*tvec+np.deg2rad(phvec[0]))+
#                  ampvec[1]*np.cos(OH2*tvec+np.deg2rad(phvec[1]))+
#                  ampvec[2]*np.cos(OH1*tvec+np.deg2rad(phvec[2])))

# another idea is put to amplitudes of others to zero.
from utide import reconstruct
# constnewval=np.array([ampvec[0],0.0,0.0,0.0,0.0,ampvec[2],ampvec[1],0.0,0.0,0.0])

# coef.update({'A':constnewval})
# print(coef['A'])
tide = reconstruct(timedatnum, coef,constit=const)
print(tide.keys())
reconstrucsignal=tide.h

#%%
#getting peaks
from scipy.signal import find_peaks
from scipy.interpolate import UnivariateSpline
peaks=find_peaks(reconstrucsignal)
peaksignal=reconstrucsignal[peaks[0]]
modulation=peaksignal.max()-peaksignal.min()
timepeaks=np.array(timedatnum)[peaks[0]]
s=UnivariateSpline(timepeaks,peaksignal,s=0)
peaksignalall=s(timedatnum)
import matplotlib.pyplot as plt
from matplotlib.dates import num2date
timedate=num2date(timedatnum)
j=4*30
plt.plot(timedate[::j],reconstrucsignal[::j],'--b',label='reconstructed sig')
plt.plot(timedate[::j],peaksignalall[::j],'r',label='peaks sig_mod:'+str(modulation))
plt.xlabel('time')
plt.ylabel('Waterlevel (m)')
plt.title('Reconstructed M2 signal with H1 and H2 components for: '+stationamevec[i])
plt.legend()
plt.savefig('bathymetry_checks/reconstructTA'+stationamevec[i]+'monthly.jpg')

# tideconst='H2'
# (Am,Ph)=tideanalysis.compute1stationtidal(data,tideconst)
# print('H2 tide constituent values are:'+str(Am)+', '+str(Ph))
# tideconst='M2'
# (Am,Ph)=tideanalysis.compute1stationtidal(data,tideconst)
# print('M2 tide constituent values are:'+str(Am)+', '+str(Ph))
# selectstation={'M2amp':(("stations"),amp),'stationname':stationamevec,'Lon':stationlonvec,'Lat':stationlatvec}
# coords={"stations": np.linspace(1,len(stationamevec),len(stationamevec))}
# ds=xr.Dataset(selectstation,coords=coords)
# ds.to_netcdf('M2stations.nc')

# %%
