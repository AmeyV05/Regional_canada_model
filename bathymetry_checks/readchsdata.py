#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
script to read data from the CHS server.
Created on Thu Aug 19 2021 1:48:22 PM
@Author: Amey Vasulkar
Copyright (c) 2021 Deltares
'''
import numpy as np 
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import datetime
import json
import time
def readCHStide(stationid,sdate,edate):
    headers = {
        'accept': '*/*',
    }

    params = (
        ('time-series-code', 'wlp'),
        ('from', sdate ),
        ('to', edate),
    )
    #the below sometimes gave Json decode error
    chsurl='https://api-iwls.dfo-mpo.gc.ca/api/v1/stations/'+stationid+'/data'
    # response = requests.get(chsurl, headers=headers, params=params)
    done=0
    #sometimes response headers fail
    while done==0:
        chsurl='https://api-iwls.dfo-mpo.gc.ca/api/v1/stations/'+stationid+'/data'
        # session=requests.Session()
        # retry=Retry(connect=3, backoff_factor=0.5)
        # adapter=HTTPAdapter(max_retries=retry)
        # session.mount('http://',adapter)
        # session.mount('https://', adapter)
        # response = session.get(chsurl, headers=headers, params=params)
        try:
            response = requests.get(chsurl, headers=headers, params=params)
            if 'json' in response.headers.get('Content-Type'):
                data=response.json()
                done=1
            else:
                print('Response content is not in JSON format. Trying again...')
                time.sleep(10)
        except:  # requests.exceptions.ConnectionError:
            print("Connection refused")
            time.sleep(10)

    # data=response.json()
    return(data)

#getting the time and waterlevel vector
def gettimewaterlevel(data):
    tvec=[];wlvec=[]
    for ele in data:
        # print(ele)
        tvec=np.append(tvec,ele['eventDate'])
        wlvec=np.append(wlvec,ele['value'])
    return(tvec,wlvec)

#A function which gives the data for the tide gauge from CHS portal which it provides data for only 7 days.
# But we can script it to get a longer data
def getmergedata(sdate,edate,stationid):
    #getting a time vec of start and end dates based on two big start and end dates.

    tdelta=6
    ti=datetime.timedelta(days=tdelta)
    t0=datetime.datetime.strptime(sdate,"%Y-%m-%dT%H:%M:%SZ")
    tl=datetime.datetime.strptime(edate,"%Y-%m-%dT%H:%M:%SZ")
    tf_current=t0
    tl_current=t0+ti
    done=0
    t_all=[]
    while done==0:
        if (tl_current>=tl):
            done=1
            tl_current=tl
        t_all.append([tf_current,tl_current])
        tf_current=tl_current
        tl_current=tl_current+ti
    # getting time and waterlevel data and merging. 

    Tvec=[];Wlvec=[]
    for times in t_all:
        sdate=times[0].strftime("%Y-%m-%dT%H:%M:%SZ")
        edate=times[1].strftime("%Y-%m-%dT%H:%M:%SZ")
        # print( sdate+' - '+edate)
        datati=readCHStide(stationid,sdate,edate)
        (tvec,wlvec)=gettimewaterlevel(datati)
        # print(tvec[0],wlvec[0])
        # print(tvec[-1],wlvec[-1])
        Tvec=np.append(Tvec,tvec[:-1])
        Wlvec=np.append(Wlvec,wlvec[:-1])
    return(Tvec,Wlvec)

## Reading the meta data for all the stations from the json file. 
# we don't consider stations which are discontinued.
# And only consider ones which give wlp i.e. water level predictions.
def getallstationmetadata(stationjsonfile):
    #getting the station data of all possible stations at CHS 
    allstationinfo=open(stationjsonfile)
    allstationinfodata=json.load(allstationinfo)
    # From the station data we get a set of stations which are not discontinued and
    #  which are prediction based. (wlp)

    stationamevec=[];stationidvec=[];stationlonvec=[];stationlatvec=[]
    for ele in allstationinfodata:
        # print(ele)
        if ele['type']=='DISCONTINUED':
            continue
        if ele['timeSeries'][0]['code']=='wlp':
            stationamevec=np.append(stationamevec,ele['officialName'])
            stationidvec=np.append(stationidvec,ele['id'])
            stationlonvec=np.append(stationlonvec,ele['longitude'])
            stationlatvec=np.append(stationlatvec,ele['latitude'])
    return(allstationinfodata,stationamevec,stationidvec,stationlonvec,stationlatvec)

def main():
    stationjsonfile='bathymetry_checks/chsstations.json'
    (allstationinfodata,stationamevec,stationidvec,stationlonvec,stationlatvec)=getallstationmetadata(stationjsonfile)


if __name__ == "__main__":
    main()