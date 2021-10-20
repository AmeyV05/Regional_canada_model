#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on 20210413
This script was created for cartesius. In this, the partitioning which was done separately for everymonth is now done only once at the start.
That partitioning will continue for the rest of the months. 

Start dflow runs .

python schedule_runs.py "ndom=$ndom" "tstart=$tstart" "tstop=$tstop"  "tinit=$tinit"

@author: ANV
"""

import os
import sys
import shutil
import glob
import datetime
import time
import templates
import subprocess
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree
from calendar import monthrange
# import time_average

#sys.stdout = open("run.log", "w")

# deleting any model files.
os.system('rm -rf model*')

def runmodelcartesius(rundir,mdufile,nodes):
    # if len(glob.glob(os.path.join(rundir,'*.dia')))==0:
    # command="cd "+rundir+"; ../dflowfm_linux64_binaries/bin/dflowfm_parallel.sh %d %s"%(ndom,templatefile)
    # print command
    # os.system(command)
    command="cd "+rundir+"; sh run_cartesius_parallel.sh %d"%(nodes)
    print (command)
    os.system(command)
    while not os.path.exists(os.path.join(rundir,'sim.done')):
        print "Python program sleeping until simulation is done."
        time.sleep(100)
    # command="export model="+mdufile
    # 
    # os.system(command)


def runpartitioncartesius(rundir,mdufile,nodes):
    #if len(glob.glob(os.path.join(rundir+"/output",'*.dia')))==0:
    # # command="cd "+rundir+"; ../dflowfm_linux64_binaries/bin/dflowfm_parallel.sh %d %s"%(ndom,templatefile)
    # # print command
    # # os.system(command)
        # subprocess.call(['sh', './run_hydrax.sh'])
        
    command="cd "+rundir+"; sh run_partition_cartesius_parallel.sh %d"%(nodes)
    print (command)
    os.system(command)
        # # subprocess.call(['sh', './run_hydrax.sh'])
        # 
        #     raise RuntimeError('No dia files found after run in folder %s'%rundir)
    while not os.path.exists(os.path.join(rundir,'sim.done')):
        print "Python program sleeping until simulation is done."
        time.sleep(100)
#default settings for this run
nodes=1
ndom=24*nodes
tstart='201301010000'
tstop ='201312310000'
tinit=7#time to start and ignore before tstart [days]
timap=15*24*60. #increment between maps [minutes]
#tblock=1 #length of one part of the computation [days]  Update: This will be updated on a per month basis based on the month.
cleanup=0 # remove original model output (to save diskspace, several 100 Gb/year)
#boundary forcing type :GTSM or FES 
bforcingtyp='GTSM'
for arg in sys.argv:
   print "arg = %s"%arg
   if '=' in arg:
       (key,value)=arg.split('=')
       if key.startswith('ndom'):
           ndom=int(value)
       if key.startswith('tstart'):
           tstart=value
       if key.startswith('tstop'):
           tstop=value
       # if key.startswith('tblock'):
       #     tblock=int(value)
       if key.startswith('tinit'):
           tinit=int(value)
#show arguments
print "ndom = %d"%ndom
print "tstart = %s"%tstart
print "tstop = %s"%tstop
# print "tblock = %d"%tblock Update:based on the number of days based on the month.
print "tinit = %d"%tinit

#folder for current script
base_path=os.path.dirname(os.path.realpath(os.sys.argv[0]))
#define foldernames


# spyderdir="spiderweb_from_ibtracks"
templatedir="canadamodeltemplate"
templatefilenorestart="canada_model_norestart_template.mdu"
templatefile="canada_model_template.mdu"
templateforcefileb="boundaryforcing_template.ext"
modeloutputdir="output"
restartdir="restart_%s"%tstart
# fasticedir="fasticeconfig"
bforcingdir=bforcingtyp+"boundaryforcing"


runssavedir="modelrunsdata"
os.mkdir(runssavedir)
#compute times for runs
dt_spinup=datetime.timedelta(days=tinit)
tf=datetime.datetime.strptime(tstart,"%Y%m%d%H%M")
tl=datetime.datetime.strptime(tstop,"%Y%m%d%H%M")
month0=int( tf.strftime("%m"))
year0=int( tf.strftime("%Y"))
tblock = monthrange(year0, month0)[1]
print(month0,year0,tblock)
ti=datetime.timedelta(days=tblock)
t0=tf-dt_spinup
dt_map=datetime.timedelta(minutes=timap)
#now for each run
tf_current=t0
tl_current=tf+ti
tinit=dt_spinup
trestart_current=dt_spinup+ti
t_all=[]
done=0
while done==0:
    if (tl_current>=tl):
        done=1
        tl_current=tl
    t_all.append([tf_current,tl_current,tinit,trestart_current])
    tf_current=tl_current
    month_current=int( tf_current.strftime("%m"))
    year_current=int( tf_current.strftime("%Y"))
    tblock = monthrange(year_current, month_current)[1]
    print(month_current,year_current,tblock)
    ti=datetime.timedelta(days=tblock)
    tl_current=tl_current+ti
    tinit=dt_map
    trestart_current=ti


# for the first time we partition and create the different .netnc and .mdu files.
# then replace all the .mdu file with template .mdu file. 
# Then we run the this file.
# Next time, 
# Then, we copy this file for all the model files. 
# finally, replace those mdu files with correct restart files.    


for times in t_all:
    print times[0].strftime("%Y%m%d%H%M") +' - '+times[1].strftime("%Y%m%d%H%M")
    key_values={}    
    refdate=times[0].date()
    t_ref=datetime.datetime.combine(refdate,datetime.time(0))
    refdate_str=t_ref.strftime("%Y%m%d")
    print "REFDATE = "+refdate_str
    key_values['REFDATE']=refdate_str
    tstart=(times[0]-t_ref).total_seconds()/3600.
    print "TSTART = %f"%tstart
    key_values['TSTART']=str(tstart)
    tstop=(times[1]-t_ref).total_seconds()/3600.
    print "TSTOP = %f"%tstop
    key_values['TSTOP']=str(tstop)
    tfmap=(times[2]).total_seconds()
    timap=dt_map.total_seconds()
    print "TFMAP = %f"%tfmap
    print "TIMAP = %f"%timap
    key_values['TFMAP']=str(tfmap)
    key_values['TIMAP']=str(timap)
    key_values['TMAP']=str(tfmap)+" "+str(timap)    
    tirestart=(times[3]).total_seconds()
    print "TIRESTART = %f"%tirestart
    key_values['TIRESTART']=str(tirestart)
    idom=ndom
    rundir="model_"+times[0].strftime("%Y%m%d%H%M")
    frstrundir="model_"+t_all[0][0].strftime("%Y%m%d%H%M")
    #create new folder and copy contents of template folder there for first sim.
    if times[0]<tf:
                #
        if len(glob.glob(rundir))>0:
            print "Model dir already exists "+rundir
        else:
            print "copying "+templatedir+" to "+rundir
            copy_tree(templatedir, rundir)
        frstrundir=rundir
        #month update to change 201212 to 201301 and 20139 to 201309  #month for fast ice.       
        month=int( times[0].strftime("%m"))
        if month==12:  #updating for 12th month.
            month='01'
        elif month<9:
            month=month+1
            month='0'+str(month)
        else: 
            month=month+1
            month=str(month)                
        print(month)
    else:
        if len(glob.glob(rundir))>0:
            print "Model dir already exists "+rundir
        else:
            print "copying "+frstrundir+" to "+rundir
            copy_tree(frstrundir, rundir)
            remove_tree(os.path.join(rundir,'output'))
        #month for fastice.
        month=(times[0].strftime("%m"))            
        print(month)
    mdufile="canada_model.mdu"
    print "mdufile = "+mdufile
    for key in key_values.keys():
    	print "#"+str(idom)+"#" + key + " " +str(key_values[key])
    templates.replace_all(os.path.join(rundir,templatefilenorestart),\
                              os.path.join(rundir,mdufile),key_values,'%')
    ## Below commented block deals with replacing the fastice key in ext file with correct fast ice polygon.
    # # Key_values for fast ice polygon.
    # extfile="gtsm_forcing.ext"
    # # getting the correct fastice polygon.
    #     #filenaame.
    # print "Searching and Copying fast ice polygons to "+rundir

    # for d in os.listdir(fasticedir):
    #     if d[11:13]==month:
    #         ficefile=d
    #         print(d)
    #         shutil.copy(os.path.join(fasticedir,ficefile),os.path.join(rundir,ficefile))
    #         if d.split('.')[1]=='pol':
    #             ficepol=d
    # print(ficepol)
    # key_valuesext={}
    # key_valuesext['FASTICEPOLYGON']=ficepol
    # templates.replace_all(os.path.join(rundir,templateforcefile),\
    #                           os.path.join(rundir,extfile),key_valuesext,'%')

    # Key_values for boundary forcing. 
    bextfile="boundaryforcing.ext"
    # getting the correct boundary file. (left or right based on the month. )
        #filenaame.
    print "Searching and Copying the correct bc file to "+rundir

    for d in os.listdir(bforcingdir):
        if bforcingtyp=='GTSM':
            if d[24:26]==month:
                lbcfile=d
                print(d)
                shutil.copy(os.path.join(bforcingdir,lbcfile),os.path.join(rundir,lbcfile))
            elif d[25:27]==month:
                rbcfile=d
                print(d)
                shutil.copy(os.path.join(bforcingdir,rbcfile),os.path.join(rundir,rbcfile))
        elif bforcingtyp=='FES':
            if d[23:25]==month:
                rbcfile=d
                print(d)
                shutil.copy(os.path.join(bforcingdir,lbcfile),os.path.join(rundir,lbcfile))
            elif d[24:26]==month:
                rbcfile=d
                print(d)
                shutil.copy(os.path.join(bforcingdir,rbcfile),os.path.join(rundir,rbcfile))

    
    key_valuesbext={}
    key_valuesbext['LEFTBOUNDARYDATA']=lbcfile
    key_valuesbext['RIGHTBOUNDARYDATA']=rbcfile
    templates.replace_all(os.path.join(rundir,templateforcefileb),\
                              os.path.join(rundir,bextfile),key_valuesbext,'%')


    # #partitioning the grid`for the first time only.
    if times[0]<tf:
        runpartitioncartesius(rundir,mdufile,nodes)

    while not os.path.exists(os.path.join(rundir,'sim.done')):
        print "Python program sleeping until simulation is done."
        time.sleep(100)

    #Removing the dia file.

    os.system("rm -rf "+rundir+"/output/*.dia")

    # # now, replace all the mdu files by template file with restart file option. 


    for idom in range(ndom):
    	dommdu="canada_model_%4.4d"%idom+"_template.mdu"
    	shutil.copy2(os.path.join(rundir,templatefile),os.path.join(rundir,dommdu))
    	# print "Domain mdu file = "+dommdu
    	if times[0]<tf:
	        restartfile=""
	        restarttime=""
        else:
            restartfile=os.path.join("..",os.path.join(restartdir,"canada_model_%4.4d_"%idom+times[0].strftime("%Y%m%d")+"_"+times[0].strftime("%H%M")+"00_rst.nc"))
            restarttime=times[0].strftime("%Y%m%d%H%M")
            # restartfile=os.path.join("..",os.path.join(restartdir,"gtsm_model_merged_%s_%s00_rst.nc"%(times[0].strftime("%Y%m%d"),times[0].strftime("%H%M"))))

           
            # restartfile=os.path.join("..",os.path.join(restartdir,"gtsm_coarse_"+times[0].strftime("%Y%m%d")+"_"+times[0].strftime("%H%M")+"00_rst.nc"))

        print "RESTARTFILE = "+restartfile
        print "RESTARTTIME = "+restarttime
        netfilen ="gtsm__canada_2_%4.4d"%idom+"_net.nc" 
        print "NETFILE = "+netfilen
        key_values['RESTARTFILE']=restartfile
        key_values['RESTARTTIME']=restarttime
        key_values['NETFILE']=netfilen
        # change keys in new mdu files
        mdufile="canada_model_%4.4d"%idom+".mdu"
        print "mdufile = "+dommdu
        # for key in key_values.keys():
        # 	print "#"+str(idom)+"#" + key + " " +str(key_values[key])

        templates.replace_all(os.path.join(rundir,dommdu),\
                              os.path.join(rundir,mdufile),key_values,'%')


    #start the run  by submitting it to cluster.
                # runmodelh6(rundir,mdufile)
    runmodelcartesius(rundir,mdufile,nodes)





   #  # # # process the output
   #  # for idom in range(ndom):
   #  #     runoutputdir=os.path.join(rundir,modeloutputdir)
   #  #     # mapfile=os.path.join(runoutputdir,"gtsm_model_%4.4d_map.nc"%idom)
   #  #     # avgfile=os.path.join(outputdir,"gtsm_%s_%4.4d_avg_map.nc"%(times[0].strftime("%Y%m%d%H%M"),idom))
   #  #     mapfile=os.path.join(runoutputdir,"gtsm_coarse_map.nc")
   #  #     # avgfile=os.path.join(outputdir,"gtsm_%s_%4.4d_avg_map.nc"%(times[0].strftime("%Y%m%d%H%M"),idom))
   #  #     # print mapfile+" ==> "+avgfile
   #  #     # if len(glb.glob(avgfile))==0:
   #  #     #     time_average.process_file(mapfile,avgfile)
   #  # save restart files and output his files
   #  #first remove previous restart files and output files
    if os.path.isdir(restartdir):
        print "rm -rf "+restartdir
        shutil.rmtree(restartdir)
   #  # if os.path.isdir(runssavedir):
   #  #     print "rm -rf "+runssavedir
   #  #     shutil.rmtree(runssavedir)
    os.mkdir(restartdir)

    # merging all the resart files.
    # 
    for idom in range(ndom):
        runoutputdir=os.path.join(rundir,modeloutputdir)
        #names like gtsm_fine_0002_20041231_000000_rst.nc
        #inirestartfile="gtsm_fine_%4.4d_%s_%s00_rst.nc"%(idom,times[0].strftime("%Y%m%d"),times[0].strftime("%H%M"))
        nextrestartfile="canada_model_%4.4d_%s_%s00_rst.nc"%(idom,times[1].strftime("%Y%m%d"),times[1].strftime("%H%M"))  
	# nextrestartfile="gtsm_fine_%s_%s00_rst.nc"%(times[1].strftime("%Y%m%d"),times[1].strftime("%H%M"))
        srcfile=os.path.join(runoutputdir,nextrestartfile)
        destfile=os.path.join(restartdir,nextrestartfile)
        shutil.copy(srcfile,destfile)
        originalhisfile="canada_model_0000_his.nc"
        nexthisfile="canada_model_his_%s%s.nc"%(times[0].strftime("%Y"),month)
        srcfile=os.path.join(runoutputdir,originalhisfile)
        destfile=os.path.join(runssavedir,nexthisfile)
        shutil.copy(srcfile,destfile)
        print("copy done")
    #remove model output
    if cleanup==1:
        if os.path.isdir(rundir):
            print "rm -rf "+rundir
            shutil.rmtree(rundir)
        

# sys.stdout.close()
