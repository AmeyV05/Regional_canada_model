#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Script to read the bottom friction and fast ice friction .xyz files and 
create a .xyz file of a net Chezy coefficient. 
This will be the input in forcingwice.ext file.
Created on Tue Apr 26 2022 10:52:10 AM
@Author: Amey Vasulkar
Copyright (c) 2022 Deltares
'''
#importing modules
import numpy as np
import pandas as pd
import scipy.spatial.distance as sdist
#spatial distance from scipy is needed because 
# we calculate the distance  from the lon lat value at index i from 
# bottom friction position vec to fast ice postion vec.

#%%
#function definition.
#reading a .xyz file.
def readxyzfile(file):
    headerlist=["Lon","Lat","Value"]
    df=pd.read_csv(file,delim_whitespace=True,names=headerlist)   
    posvec=np.vstack((df['Lon'],df['Lat'])).T
    valvec=np.array(df['Value'])
    return(posvec,valvec)


def computeChnet():
    Chnetvec=[]
    #the test lonlat was to test if we get the correct lon lat after the distance matrix computation.
    # testlonlatvec=np.zeros(np.shape(bf_initial_pos))
    for i in range(len(bf_correction_val)):
        (loni,lati)=(bf_initial_pos[i,0],bf_initial_pos[i,1])
        #get index of this lon lat in fice.
        distmat=sdist.cdist(fice_initial_pos,np.array([[loni,lati]]))
        lonlatindex=np.where(distmat==0)[0]
        
        #bf evaluation
        bfeval=bf_correction_val[i]*bf_initial_val[i]
        #fice evaluation
        ficeeval=2*fice_correction_val[lonlatindex]*fice_initial_val[lonlatindex]
        # #testlonlat
        # testlonlatvec[i,:]=fice_initial_pos[lonlatindex,:]
        
        #net eval
        if ficeeval==0:
            #important because when ficeeval is zero there is not fast icee and the inverse is infinity so ignore it.
            neteval=(1/(bfeval**2))  
        else:
            neteval=(1/(bfeval**2))+(1/(ficeeval**2))
        #Chnet
        Chneti=np.sqrt(1/neteval)
        Chnetvec=np.append(Chnetvec,Chneti)
    return(Chnetvec)

def main():
    Chnetvec=computeChnet()
    #converting to a .xyz file
    fname='Chezynet_march.xyz'
    vec=np.vstack((bf_initial_pos.T,Chnetvec.reshape((1,len(Chnetvec)))))
    np.savetxt(fname,vec.T,fmt=['%0.2f','%0.2f','%0.3f'],delimiter='\t')

#%%
#we read this here as we need the variables everywhere.
#reading the 4 files which give us Kb, Chb, Kf, Chf.
bf_initial='bf_initial_16_v5.xyz'
bf_correction='bf_correction_16_v5.xyz'
fice_initial='fastice_initial_frictionvalue_march.xyz'
fice_correction='fastice_correction_march_20_v1.xyz'
(bf_initial_pos,bf_initial_val)=readxyzfile(bf_initial)
(bf_correction_pos,bf_correction_val)=readxyzfile(bf_correction)
(fice_initial_pos,fice_initial_val)=readxyzfile(fice_initial)
(fice_correction_pos,fice_correction_val)=readxyzfile(fice_correction)

if __name__ == '__main__':
    main()
    