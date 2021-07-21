#!/bin/bash
# script for downloading data from CMEMS ocean products
# Created by: Amey Vasulkar
# Date: 26-05-2021
#set parameters
server=https://nrt.cmems-du.eu/motu-web/Motu
id=ARCTIC_ANALYSISFORECAST_PHY_TIDE_002_015-TDS
outfname="CMEMSTidal.nc"
prid=dataset-topaz6-arc-15min-3km-be
# id=GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS
# prid=global-analysis-forecast-phy-001-024
# outfname="CMEMSIcedaily.nc"
lon0=-179.98
lon1=179.91
lat0=41.569
lat1=90.0
date0="2019-01-01 00:00:00"
date1="2019-01-01 02:00:00"
outdir="."
name="avasulkar"
pwd="Euler;27183"
python -m motuclient --motu $server --service-id $id  --product-id $prid --longitude-min $lon0 --longitude-max $lon1 --latitude-min $lat0 --latitude-max $lat1 \
--date-min $date0 --date-max $date1 --variable latitude --variable longitude --variable model_depth \
--variable vxo --variable vyo --variable zos --out-dir $outdir --out-name $outfname --user $name --pwd $pwd

# python -m motuclient --motu $server --service-id $id  --product-id $prid --longitude-min $lon0 --longitude-max $lon1 --latitude-min $lat0 \
# --latitude-max $lat1 --date-min $date0 --date-max $date1 --depth-min 0.493 --depth-max 0.4942 --variable siconc --variable sithick --variable usi --variable vsi --variable zos \
# --out-dir $outdir --out-name $outfname --user $name --pwd $pwd