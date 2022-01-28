% OpenDA version 3.0.2.-1 April 24 2021
% opening :/gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochObserver/noosObservations.xml
% NoosStochObserver[i]=TimeSeries(
%   Location = 
%   Position = (0.0,0.0)
%   Height   = NaN
%   Quantity = 
%   Unit     = m
%   Source   = 
%   Id       = churchill_jan.waterlevel
%   relativestandarddeviation  = 0.0
%   timezone  = GMT
%   analtime  = 
%   standarddeviation  = 0.05
%   status  = assimilation
%   Values   = 
%   (58849.0=202001010000,1.354)
%   (58849.01041666667=202001010015,1.475)
%   (58849.02083333333=202001010030,1.616)
%   (58849.03125=202001010045,1.774)
%   (58849.04166666667=202001010100,1.946)
%   ...
%   (58879.95833333333=202001312300,1.097)
%   (58879.96875=202001312315,1.055)
%   (58879.97916666667=202001312330,1.039)
%   (58879.98958333333=202001312345,1.048)
%   (58880.0=202002010000,1.082)
%
%   Values.length()=2977
%)
% NoosStochObserver[i]=TimeSeries(
%   Location = 
%   Position = (0.0,0.0)
%   Height   = NaN
%   Quantity = 
%   Unit     = m
%   Source   = 
%   Id       = whalecove_jan.waterlevel
%   relativestandarddeviation  = 0.0
%   timezone  = GMT
%   analtime  = 
%   standarddeviation  = 0.05
%   status  = assimilation
%   Values   = 
%   (58849.0=202001010000,2.537)
%   (58849.01041666667=202001010015,2.665)
%   (58849.02083333333=202001010030,2.789)
%   (58849.03125=202001010045,2.91)
%   (58849.04166666667=202001010100,3.025)
%   ...
%   (58879.95833333333=202001312300,1.598)
%   (58879.96875=202001312315,1.722)
%   (58879.97916666667=202001312330,1.848)
%   (58879.98958333333=202001312345,1.974)
%   (58880.0=202002010000,2.1)
%
%   Values.length()=2977
%)
% Starting Algorithm: 
%	className: org.openda.algorithms.Dud
%	dir.: ././algorithm
%	config.: dudAlgorithm.xml
%  Algorithm  Dud initialisation (stoch. obs. and stoch. model have been set)
%  Algorithm  configString = dudAlgorithm.xml
% opening :/gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././algorithm/dudAlgorithm.xml
%  Algorithm  Retrieving initial parameters from model
% Create new BBModelInstance with number: 0
% Instance initialization done
%  Algorithm  Starting optimizer
%  Algorithm  costFunction@class=org.openda.algorithms.SimulationKwadraticCostFunction
% Create new BBModelInstance with number: 1
% Instance initialization done
% CostFunction = SimulationKwadraticCostFunction
%  Algorithm  costFunction@weakParameterConstraint=false
%  Algorithm  costFunction@factor=0.5
%  Algorithm  costFunction@biasRemoval=true
%  Algorithm  costFunction@stdRemoval=false
%  Algorithm  costFunction@tryParallel=false
%  Algorithm  outerLoop@maxIterations=40
%  Algorithm  outerLoop@absTolerance=0.01
%  Algorithm  outerLoop@relTolerance=0.001
%  Algorithm  outerLoop@relToleranceLinearCost=0.001
%  Algorithm  lineSearch@maxIterations=40
%  Algorithm  lineSearch@maxRelStepSize=10.0
%  Algorithm  lineSearch/backtracking@startIterationNegativeLook=3
%  Algorithm  lineSearch/backtracking@shorteningFactor=0.5
%  Algorithm  constraints@parameterConstraint=true
%  Algorithm  constraints/lowerbounds@Lbounds=[25.0,25.0,25.0,25.0,25.0,25.0]
%  Algorithm  constraints/upperbounds@Ubounds=null
% Application initializing finished
% Initializing Algorithm
% WARN: Initial parameter [0]=0.0 is smaller than lowerbound[0]=25.0. Parameter is set equal to lowerbound.
% WARN: Initial parameter [1]=0.0 is smaller than lowerbound[1]=25.0. Parameter is set equal to lowerbound.
% WARN: Initial parameter [2]=0.0 is smaller than lowerbound[2]=25.0. Parameter is set equal to lowerbound.
% WARN: Initial parameter [3]=0.0 is smaller than lowerbound[3]=25.0. Parameter is set equal to lowerbound.
% WARN: Initial parameter [4]=0.0 is smaller than lowerbound[4]=25.0. Parameter is set equal to lowerbound.
% WARN: Initial parameter [5]=0.0 is smaller than lowerbound[5]=25.0. Parameter is set equal to lowerbound.
% Evaluating with parameters 
% Params - containing:
%    vi_1= 25
%    vi_2= 25
%    vi_3= 25
%    vi_4= 25
%    vi_5= 25
%    vi_6= 25
% ========================================================================
% prepare no 1
% Create new BBModelInstance with number: 2
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{1}	=[25.0, 25.0, 25.0, 25.0, 25.0, 25.0];
% ========================================================================
% evaluate no. 1
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work2/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8669368848540492	2.875182188687153E-15	0.8670875909629412	2877	-1.382755877972413	1.5320984322163176
% whalecove_jan.waterlevel		0.7079444798550419	-3.4787168805283653E-15	0.708067547127568	2877	-1.0722666188207501	1.3855816997913568
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 0
costObserved{1}	=720840.9515842126;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 0
costTotal{1}	=720840.9515842126;
% SimulationKwadraticCostFunction: evaluation 1 : cost = 7.208E5
% Evaluating with parameters 
% Params - containing:
%    vi_1= 1.025E3
%    vi_2= 25
%    vi_3= 25
%    vi_4= 25
%    vi_5= 25
%    vi_6= 25
% ========================================================================
% prepare no 2
% Create new BBModelInstance with number: 3
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{2}	=[1025.0, 25.0, 25.0, 25.0, 25.0, 25.0];
% ========================================================================
% evaluate no. 2
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work3/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8680650535016219	4.095749889417022E-15	0.8682159557284893	2877	-1.38478691855948	1.5341270348633307
% whalecove_jan.waterlevel		0.7080920587507946	2.500495470403319E-15	0.7082151516780605	2877	-1.072439512748418	1.3862515880461594
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 1
costObserved{2}	=722087.4704669196;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 1
costTotal{2}	=722087.4704669196;
% SimulationKwadraticCostFunction: evaluation 2 : cost = 7.221E5
% Evaluating with parameters 
% Params - containing:
%    vi_1= 25
%    vi_2= 1.025E3
%    vi_3= 25
%    vi_4= 25
%    vi_5= 25
%    vi_6= 25
% ========================================================================
% prepare no 3
% Create new BBModelInstance with number: 4
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{3}	=[25.0, 1025.0, 25.0, 25.0, 25.0, 25.0];
% ========================================================================
% evaluate no. 3
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work4/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.866944708566682	1.2660499818656357E-15	0.8670954160356296	2877	-1.3819245249095706	1.5298130777778727
% whalecove_jan.waterlevel		0.708236845100845	-2.9350979112441333E-15	0.7083599631974029	2877	-1.0711400186120734	1.3868325073008494
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 2
costObserved{3}	=721086.9969929329;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 2
costTotal{3}	=721086.9969929329;
% SimulationKwadraticCostFunction: evaluation 3 : cost = 7.211E5
% Evaluating with parameters 
% Params - containing:
%    vi_1= 25
%    vi_2= 25
%    vi_3= 1.025E3
%    vi_4= 25
%    vi_5= 25
%    vi_6= 25
% ========================================================================
% prepare no 4
% Create new BBModelInstance with number: 5
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{4}	=[25.0, 25.0, 1025.0, 25.0, 25.0, 25.0];
% ========================================================================
% evaluate no. 4
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work5/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8634260768860225	-5.29012055515421E-15	0.8635761726849635	2877	-1.3872590750411362	1.5215259279635645
% whalecove_jan.waterlevel		0.7011825194203435	1.7852472972146316E-15	0.7013044112108202	2877	-1.0538561011587229	1.3748181184583905
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 3
costObserved{4}	=711862.7361840989;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 3
costTotal{4}	=711862.7361840989;
% SimulationKwadraticCostFunction: evaluation 4 : cost = 7.119E5
% Evaluating with parameters 
% Params - containing:
%    vi_1= 25
%    vi_2= 25
%    vi_3= 25
%    vi_4= 1.025E3
%    vi_5= 25
%    vi_6= 25
% ========================================================================
% prepare no 5
% Create new BBModelInstance with number: 6
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{5}	=[25.0, 25.0, 25.0, 1025.0, 25.0, 25.0];
% ========================================================================
% evaluate no. 5
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work6/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8756502743498203	7.163188228340167E-15	0.8758024951722386	2877	-1.4210892081583717	1.5760188567535458
% whalecove_jan.waterlevel		0.6794441401478629	2.1640133261724426E-15	0.6795622529936309	2877	-1.0379593290282478	1.3347247101654296
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 4
costObserved{5}	=706825.8150633778;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 4
costTotal{5}	=706825.8150633778;
% SimulationKwadraticCostFunction: evaluation 5 : cost = 7.068E5
% Evaluating with parameters 
% Params - containing:
%    vi_1= 25
%    vi_2= 25
%    vi_3= 25
%    vi_4= 25
%    vi_5= 1.025E3
%    vi_6= 25
% ========================================================================
% prepare no 6
% Create new BBModelInstance with number: 7
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{6}	=[25.0, 25.0, 25.0, 25.0, 1025.0, 25.0];
% ========================================================================
% evaluate no. 6
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work7/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8718874044711765	6.138210599526683E-16	0.872038971165841	2877	-1.4057334728117354	1.5015102054844014
% whalecove_jan.waterlevel		0.7084377324962319	1.9857704890158256E-15	0.708560885514545	2877	-1.0541508703973768	1.3583649633400068
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 5
costObserved{6}	=726196.0371341928;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 5
costTotal{6}	=726196.0371341928;
% SimulationKwadraticCostFunction: evaluation 6 : cost = 7.262E5
% Evaluating with parameters 
% Params - containing:
%    vi_1= 25
%    vi_2= 25
%    vi_3= 25
%    vi_4= 25
%    vi_5= 25
%    vi_6= 1.025E3
% ========================================================================
% prepare no 7
% Create new BBModelInstance with number: 8
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{7}	=[25.0, 25.0, 25.0, 25.0, 25.0, 1025.0];
% ========================================================================
% evaluate no. 7
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work8/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8057970045654177	1.778416823527973E-15	0.805937082272615	2877	-1.308548181636766	1.417072501018914
% whalecove_jan.waterlevel		0.6581354680780617	3.8376420097296915E-15	0.6582498766783312	2877	-1.0026099621117974	1.2771467245434323
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 6
costObserved{7}	=622842.3669153972;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 6
costTotal{7}	=622842.3669153972;
% SimulationKwadraticCostFunction: evaluation 7 : cost = 6.228E5
% Algorithm initialized
% Algorithm starting next step
% ======================================================
% DUD outer iteration no.1
% ======================================================
% -----------------------------------------------------
%  resultItem id: costs, outputLevel: Essential, context: any
costs{1}	=[622842.3669153972,706825.8150633778,711862.7361840989,720840.9515842126,721086.9969929329,722087.4704669196,726196.0371341928];
% -----------------------------------------------------
% RHS norm: 1116.1024746101025
% Start search until improvement,
%  resultItem id: linearCost, outputLevel: Normal, context: outer iteration 1
linearCost{1}	=375361.3509413382;
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 4.266E3
%      vi_5= 25
%      vi_6= 5.905E3
% ========================================================================
% prepare no 8
% Create new BBModelInstance with number: 9
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{8}	=[24.99999999999856, 24.999999999999808, 24.999999999998238, 4266.008587447881, 24.999999999998987, 5904.759551636561];
% ========================================================================
% evaluate no. 8
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work9/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7919511708325225	-5.008011149873481E-15	0.7920888416151068	2877	-1.7479186235857835	2.7475070562625623
% whalecove_jan.waterlevel		0.5979526869291805	-8.855221243775357E-17	0.5980566335074424	2877	-0.9997414850057779	1.1536165901330773
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: outer iteration 1
costObserved{8}	=566615.9854826956;
%  resultItem id: costTotal, outputLevel: Essential, context: outer iteration 1
costTotal{8}	=566615.9854826956;
% SimulationKwadraticCostFunction: evaluation 8 : cost = 5.666E5
% Error estimate for this outer iteration
% stop criterion 1, imain                            > maxit :	 1 < 40
% stop criterion 2, |new - previous cost|            < abstol:	 56226.3814327016 > 0.01
% stop criterion 3, |new - previous cost|/|new cost| < reltol:	 0.0992319010993006 > 0.001
% stop criterion 4, linearized cost relative error: 0.7728052747343043 < 0.001
% Algorithm starting next step
% ======================================================
% DUD outer iteration no.2
% ======================================================
% -----------------------------------------------------
%  resultItem id: costs, outputLevel: Essential, context: any
costs{2}	=[566615.9854826956,622842.3669153972,706825.8150633778,711862.7361840989,720840.9515842126,721086.9969929329,722087.4704669196];
% -----------------------------------------------------
% RHS norm: 1064.5336870974968
% Start search until improvement,
% % Reducing stepsize! Relative step was:[8.243217770133754,5.095992571293576,-9.044965131034221E-15,-11.229570756863595,-1.820484153478951E-16,-3.2412584902596997E-15]
%  resultItem id: linearCost, outputLevel: Normal, context: outer iteration 2
linearCost{2}	=361478.6091915146;
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 836.664
%      vi_5= 25
%      vi_6= 2.199E3
% ========================================================================
% prepare no 9
% Create new BBModelInstance with number: 10
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{9}	=[24.99999999999838, 25.000000000000004, 24.999999999993495, 836.663773971921, 25.000000000000888, 2199.4035609169982];
% ========================================================================
% evaluate no. 9
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work10/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7941741857801672	-1.9382282237523363E-15	0.7943122430060319	2877	-1.333313850736392	1.4167176974404403
% whalecove_jan.waterlevel		0.6183582390757658	1.8309464187848956E-15	0.6184657329034492	2877	-0.9896930901425554	1.2020886484987117
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: outer iteration 2
costObserved{9}	=582925.9726053484;
%  resultItem id: costTotal, outputLevel: Essential, context: outer iteration 2
costTotal{9}	=582925.9726053484;
% SimulationKwadraticCostFunction: evaluation 9 : cost = 5.829E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 2.551E3
%      vi_5= 25
%      vi_6= 4.052E3
% ========================================================================
% prepare no 10
% Create new BBModelInstance with number: 11
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{10}	=[24.99999999999847, 24.999999999999908, 24.99999999999586, 2551.336180709902, 24.99999999999994, 4052.0815562767802];
% ========================================================================
% evaluate no. 10
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work11/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7924838656893893	7.440879509768017E-16	0.7926216290742963	2877	-1.4878504704039957	1.9160362776941566
% whalecove_jan.waterlevel		0.60120075298717	2.6617163334519134E-15	0.6013052642009943	2877	-0.9922973467535858	1.153221761700759
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 1
costObserved{10}	=569342.7773020536;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 1
costTotal{10}	=569342.7773020536;
% SimulationKwadraticCostFunction: evaluation 10 : cost = 5.693E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 3.409E3
%      vi_5= 25
%      vi_6= 4.978E3
% ========================================================================
% prepare no 11
% Create new BBModelInstance with number: 12
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{11}	=[24.99999999999851, 24.999999999999858, 24.99999999999705, 3408.6723840788914, 24.99999999999946, 4978.420553956669];
% ========================================================================
% evaluate no. 11
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work12/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.790865470580169	-5.074662478427028E-15	0.7910029526273759	2877	-1.4194085263484226	1.7291695249680872
% whalecove_jan.waterlevel		0.5970066611274647	-2.0729945537922845E-15	0.5971104432509997	2877	-1.003080278020977	1.1615317816543582
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 2
costObserved{11}	=564976.7130006632;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 2
costTotal{11}	=564976.7130006632;
% SimulationKwadraticCostFunction: evaluation 11 : cost = 5.65E5
% Error estimate for this outer iteration
% stop criterion 1, imain                            > maxit :	 2 < 40
% stop criterion 2, |new - previous cost|            < abstol:	 1639.272482032422 > 0.01
% stop criterion 3, |new - previous cost|/|new cost| < reltol:	 0.0029014868123077805 > 0.001
% stop criterion 4, linearized cost relative error: 1.0795076324828379 < 0.001
% Algorithm starting next step
% ======================================================
% DUD outer iteration no.3
% ======================================================
% -----------------------------------------------------
%  resultItem id: costs, outputLevel: Essential, context: any
costs{3}	=[564976.7130006632,566615.9854826956,622842.3669153972,706825.8150633778,711862.7361840989,720840.9515842126,721086.9969929329];
% -----------------------------------------------------
% RHS norm: 1062.9926744814973
% Start search until improvement,
% % Reducing stepsize! Relative step was:[-0.7005441595444918,9.555537301286915,6.6846810119263536,-1.0276361587251146E-14,-13.442148508784959,-1.1245205209370787E-15]
%  resultItem id: linearCost, outputLevel: Normal, context: outer iteration 3
linearCost{3}	=361383.5585612415;
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 891.461
%      vi_5= 25
%      vi_6= 1.293E3
% ========================================================================
% prepare no 12
% Create new BBModelInstance with number: 13
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{12}	=[25.000000000001588, 24.999999999999343, 24.999999999994927, 891.4614026144874, 25.00000000000083, 1293.4288647788385];
% ========================================================================
% evaluate no. 12
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work13/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8063632049800754	-3.3370929717474462E-15	0.806503381114116	2877	-1.3046962904958328	1.4412214499953302
% whalecove_jan.waterlevel		0.6246622022180398	6.339872203608987E-16	0.6247707919106849	2877	-0.9771891075475345	1.2332000724115162
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: outer iteration 3
costObserved{12}	=598660.2487988276;
%  resultItem id: costTotal, outputLevel: Essential, context: outer iteration 3
costTotal{12}	=598660.2487988276;
% SimulationKwadraticCostFunction: evaluation 12 : cost = 5.987E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 2.15E3
%      vi_5= 25
%      vi_6= 3.136E3
% ========================================================================
% prepare no 13
% Create new BBModelInstance with number: 14
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{13}	=[25.000000000000046, 24.9999999999996, 24.99999999999599, 2150.0668933466873, 25.000000000000146, 3135.9247093677536];
% ========================================================================
% evaluate no. 13
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work14/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8000770832326596	-3.158389348667523E-15	0.8002161666032436	2877	-1.3518803146366842	3.629258185642859
% whalecove_jan.waterlevel		0.6071322033239677	4.0446162044571743E-16	0.607237745646074	2877	-0.9781603707037462	1.1839246476553302
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 1
costObserved{13}	=580424.8827111498;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 1
costTotal{13}	=580424.8827111498;
% SimulationKwadraticCostFunction: evaluation 13 : cost = 5.804E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 2.779E3
%      vi_5= 25
%      vi_6= 4.057E3
% ========================================================================
% prepare no 14
% Create new BBModelInstance with number: 15
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{14}	=[24.999999999999282, 24.99999999999973, 24.99999999999652, 2779.3696387127893, 24.9999999999998, 4057.1726316622107];
% ========================================================================
% evaluate no. 14
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work15/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.792866074487979	1.4298187200195711E-15	0.7930039043150933	2877	-1.3999662011518794	1.8912666230004511
% whalecove_jan.waterlevel		0.6028891288308652	8.448103328007051E-16	0.6029939335476636	2877	-0.9822920860609455	1.1869927026645657
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 2
costObserved{14}	=570861.195163933;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 2
costTotal{14}	=570861.195163933;
% SimulationKwadraticCostFunction: evaluation 14 : cost = 5.709E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 3.094E3
%      vi_5= 25
%      vi_6= 4.518E3
% ========================================================================
% prepare no 15
% Create new BBModelInstance with number: 16
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{15}	=[24.99999999999889, 24.999999999999797, 24.99999999999679, 3094.0210113958406, 24.99999999999963, 4517.796592809441];
% ========================================================================
% evaluate no. 15
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work16/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.791609020548307	5.216665857968317E-15	0.7917466318523526	2877	-1.4433216588578666	2.513820981671631
% whalecove_jan.waterlevel		0.5994150456934118	-1.9471728916753417E-15	0.5995192464844108	2877	-1.0107566375381154	1.1725580681064964
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 3
costObserved{15}	=567311.739385187;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 3
costTotal{15}	=567311.739385187;
% SimulationKwadraticCostFunction: evaluation 15 : cost = 5.673E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 3.251E3
%      vi_5= 25
%      vi_6= 4.748E3
% ========================================================================
% prepare no 16
% Create new BBModelInstance with number: 17
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{16}	=[24.999999999998703, 24.999999999999822, 24.99999999999692, 3251.3466977373655, 24.999999999999545, 4748.108573383055];
% ========================================================================
% evaluate no. 16
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work17/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7885208923789274	3.803462536242086E-15	0.7886579668506065	2877	-1.8409278054011635	1.7777094812389418
% whalecove_jan.waterlevel		0.5967098606968898	-7.219431216037853E-16	0.596813591225391	2877	-1.0026650404148008	1.1645971464906162
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 4
costObserved{16}	=562642.1480955298;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 4
costTotal{16}	=562642.1480955298;
% SimulationKwadraticCostFunction: evaluation 16 : cost = 5.626E5
% Error estimate for this outer iteration
% stop criterion 1, imain                            > maxit :	 3 < 40
% stop criterion 2, |new - previous cost|            < abstol:	 2334.5649051334476 > 0.01
% stop criterion 3, |new - previous cost|/|new cost| < reltol:	 0.004149289051727897 > 0.001
% stop criterion 4, linearized cost relative error: 1.1654453259536623 < 0.001
% Algorithm starting next step
% ======================================================
% DUD outer iteration no.4
% ======================================================
% -----------------------------------------------------
%  resultItem id: costs, outputLevel: Essential, context: any
costs{4}	=[562642.1480955298,564976.7130006632,566615.9854826956,622842.3669153972,706825.8150633778,711862.7361840989,720840.9515842126];
% -----------------------------------------------------
% RHS norm: 1060.7941818237218
% Start search until improvement,
% % Reducing stepsize! Relative step was:[-0.5719288034624318,-0.344541122844209,10.026854692880068,6.926694516811683,-1.3759103946106941E-14,-13.942877919148225]
%  resultItem id: linearCost, outputLevel: Normal, context: outer iteration 4
linearCost{4}	=359210.44076164573;
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 937.372
%      vi_5= 25
%      vi_6= 1.361E3
% ========================================================================
% prepare no 17
% Create new BBModelInstance with number: 18
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{17}	=[25.000000000001616, 25.000000000000195, 24.99999999999332, 937.3719814368487, 25.0000000000007, 1360.6382098244212];
% ========================================================================
% evaluate no. 17
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work18/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8059743336414377	9.03492775386483E-16	0.8061144421750708	2877	-1.3159204948165752	1.4579934171503404
% whalecove_jan.waterlevel		0.6238414216205582	3.931100236997942E-15	0.6239498686307855	2877	-0.9749847296073604	1.2107048726601894
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: outer iteration 4
costObserved{17}	=597709.8379438616;
%  resultItem id: costTotal, outputLevel: Essential, context: outer iteration 4
costTotal{17}	=597709.8379438616;
% SimulationKwadraticCostFunction: evaluation 17 : cost = 5.977E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 2.094E3
%      vi_5= 25
%      vi_6= 3.054E3
% ========================================================================
% prepare no 18
% Create new BBModelInstance with number: 19
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{18}	=[25.00000000000016, 25.000000000000007, 24.99999999999512, 2094.3593395871085, 25.00000000000012, 3054.373391603738];
% ========================================================================
% evaluate no. 18
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work19/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7952786748099613	-6.717554030394313E-15	0.7954169240373966	2877	-1.3419611481415128	2.426114733777046
% whalecove_jan.waterlevel		0.6074047476467169	1.964357496109237E-15	0.6075103373472361	2877	-0.9947814919144466	1.193600108871218
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 1
costObserved{18}	=576210.5648702042;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 1
costTotal{18}	=576210.5648702042;
% SimulationKwadraticCostFunction: evaluation 18 : cost = 5.762E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 2.673E3
%      vi_5= 25
%      vi_6= 3.901E3
% ========================================================================
% prepare no 19
% Create new BBModelInstance with number: 20
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{19}	=[24.99999999999943, 24.999999999999915, 24.99999999999602, 2672.8530186622365, 24.999999999999833, 3901.2409824933966];
% ========================================================================
% evaluate no. 19
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work20/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7911351752264334	3.727216018462043E-15	0.7912727041584123	2877	-1.7597856585892833	1.4453603197137672
% whalecove_jan.waterlevel		0.6005779454354229	5.648693318649478E-16	0.6006823483819624	2877	-0.9803885532026053	1.1886222775920843
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 2
costObserved{19}	=567683.1575574066;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 2
costTotal{19}	=567683.1575574066;
% SimulationKwadraticCostFunction: evaluation 19 : cost = 5.677E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 2.962E3
%      vi_5= 25
%      vi_6= 4.325E3
% ========================================================================
% prepare no 20
% Create new BBModelInstance with number: 21
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{20}	=[24.99999999999907, 24.999999999999865, 24.99999999999647, 2962.099858199801, 24.999999999999687, 4324.674777938226];
% ========================================================================
% evaluate no. 20
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work21/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.79051600234965	-1.5142238591475676E-15	0.7906534236461848	2877	-1.5098389661333673	1.777441154973617
% whalecove_jan.waterlevel		0.6005432638452026	-1.1736488517155585E-17	0.6006476607627822	2877	-1.007483855182157	1.1607645592829483
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 3
costObserved{20}	=567095.6900941029;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 3
costTotal{20}	=567095.6900941029;
% SimulationKwadraticCostFunction: evaluation 20 : cost = 5.671E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 3.107E3
%      vi_5= 25
%      vi_6= 4.536E3
% ========================================================================
% prepare no 21
% Create new BBModelInstance with number: 22
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{21}	=[24.999999999998884, 24.999999999999847, 24.999999999996692, 3106.7232779685833, 24.99999999999962, 4536.391675660641];
% ========================================================================
% evaluate no. 21
% NetcdfDataObject: station_id variable found in netcdf file /gpfs/work1/0/einf220/AV/canada_model/OpenDAruns/basic_test_model/././stochModel/././work22/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7894616133169094	-6.263869631317753E-15	0.7895988513211298	2877	-1.3328558449013945	1.6678487964810662
% whalecove_jan.waterlevel		0.6012740812737098	3.276946856228813E-15	0.6013786052347375	2877	-1.0095946363584907	1.1644116065493626
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 4
costObserved{21}	=566642.5038985619;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 4
costTotal{21}	=566642.5038985619;
% SimulationKwadraticCostFunction: evaluation 21 : cost = 5.666E5
% Cost is worse! Reducing stepsize.
% Start looking in negative direction
% Error running algorithm step.
% Error message: Vector.axpy: x.getSize(6) != internal length (0)
% Error type :RuntimeException
% Stacktrace :java.lang.RuntimeException: Vector.axpy: x.getSize(6) != internal length (0)
%	at org.openda.utils.VectorDouble.axpy(VectorDouble.java:276)
%	at org.openda.utils.Vector.axpy(Vector.java:290)
%	at org.openda.algorithms.BaseDudCoreOptimizer.next(BaseDudCoreOptimizer.java:911)
%	at org.openda.algorithms.BaseDud.next(BaseDud.java:301)
%	at org.openda.application.ApplicationRunnerSingleThreaded.runSingleThreaded(ApplicationRunnerSingleThreaded.java:86)
%	at org.openda.application.OpenDaApplication.runApplicationBatch(OpenDaApplication.java:114)
%	at org.openda.application.OpenDaApplication.main(OpenDaApplication.java:102)
%
% Application Done
