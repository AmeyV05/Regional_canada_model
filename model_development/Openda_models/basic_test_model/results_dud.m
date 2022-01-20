% OpenDA version 3.0.2.-1 April 24 2021
% opening :/p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochObserver/noosObservations.xml
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
% opening :/p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././algorithm/dudAlgorithm.xml
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
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work2/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8669369767298699	8.314922643644362E-15	0.8670876828547349	2877	-1.3827560207703558	1.5320986472384528
% whalecove_jan.waterlevel		0.7079445456466593	1.246615657923833E-15	0.7080676129306221	2877	-1.072266717099089	1.385581837527711
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 0
costObserved{1}	=720841.0968466504;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 0
costTotal{1}	=720841.0968466504;
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
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work3/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.86806514166288	-4.0984197372667674E-15	0.8682160439050732	2877	-1.384787060457879	1.5341272484141675
% whalecove_jan.waterlevel		0.7080921244191429	-3.2157978537006304E-15	0.7082152173578246	2877	-1.0724396142933377	1.38625173183817
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 1
costObserved{2}	=722087.612048632;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 1
costTotal{2}	=722087.612048632;
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
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work4/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8669448308549139	7.104058552358239E-15	0.867095538345118	2877	-1.381924814446926	1.529813476407096
% whalecove_jan.waterlevel		0.7082369658548281	-2.2453826992174797E-15	0.7083600839723779	2877	-1.0711402300417903	1.3868327398787095
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 2
costObserved{3}	=721087.2174166718;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 2
costTotal{3}	=721087.2174166718;
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
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work5/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8634080077034135	5.157387104187672E-15	0.8635581003612532	2877	-1.3824675938743347	1.516794054730214
% whalecove_jan.waterlevel		0.7011420782646207	1.3330265710709277E-16	0.7012639630249096	2877	-1.053821953196247	1.3685508896254934
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 3
costObserved{4}	=711812.150406446;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 3
costTotal{4}	=711812.150406446;
% SimulationKwadraticCostFunction: evaluation 4 : cost = 7.118E5
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
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work6/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8763622938039594	-2.7406869091903263E-15	0.8765146384020334	2877	-1.4331632858921928	1.583204891804647
% whalecove_jan.waterlevel		0.6792083392574298	6.356352076630767E-15	0.679326411112168	2877	-1.0376621813253892	1.3250816131157523
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 4
costObserved{5}	=707359.2658531971;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 4
costTotal{5}	=707359.2658531971;
% SimulationKwadraticCostFunction: evaluation 5 : cost = 7.074E5
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
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work7/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8718893914240641	-9.780045696905493E-16	0.872040958464135	2877	-1.4057351994591307	1.5015150200346643
% whalecove_jan.waterlevel		0.7084392729496098	-1.7423128911842056E-15	0.7085624262357131	2877	-1.0541536925134825	1.3583684483528704
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 5
costObserved{6}	=726199.2866684716;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 5
costTotal{6}	=726199.2866684716;
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
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work8/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8059050104888899	5.750716743080364E-15	0.806045106971562	2877	-1.3089457464660084	1.4181125026236725
% whalecove_jan.waterlevel		0.6581822970917958	-2.1462866206523046E-15	0.6582967138327013	2877	-0.9990145502278982	1.280941161035014
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 6
costObserved{7}	=622977.997457131;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 6
costTotal{7}	=622977.997457131;
% SimulationKwadraticCostFunction: evaluation 7 : cost = 6.23E5
% Algorithm initialized
% Algorithm starting next step
% ======================================================
% DUD outer iteration no.1
% ======================================================
% -----------------------------------------------------
%  resultItem id: costs, outputLevel: Essential, context: any
costs{1}	=[622977.997457131,707359.2658531971,711812.150406446,720841.0968466504,721087.2174166718,722087.612048632,726199.2866684716];
% -----------------------------------------------------
% RHS norm: 1116.2239895801658
% Start search until improvement,
%  resultItem id: linearCost, outputLevel: Normal, context: outer iteration 1
linearCost{1}	=377271.0143370925;
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 4.192E3
%      vi_5= 25
%      vi_6= 5.907E3
% ========================================================================
% prepare no 8
% Create new BBModelInstance with number: 9
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{8}	=[24.99999999999949, 24.999999999997957, 25.000000000000288, 4192.454002575784, 24.999999999998977, 5907.005036596438];
% ========================================================================
% evaluate no. 8
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work9/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8037304217081416	2.6341775982707816E-15	0.8038701401658174	2877	-2.690717181503811	3.005555052322199
% whalecove_jan.waterlevel		0.5954909663648337	-4.272894971873997E-15	0.5955944850038357	2877	-0.9948036608125727	1.164560778338008
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: outer iteration 1
costObserved{8}	=575740.6838684512;
%  resultItem id: costTotal, outputLevel: Essential, context: outer iteration 1
costTotal{8}	=575740.6838684512;
% SimulationKwadraticCostFunction: evaluation 8 : cost = 5.757E5
% Error estimate for this outer iteration
% stop criterion 1, imain                            > maxit :	 1 < 40
% stop criterion 2, |new - previous cost|            < abstol:	 47237.313588679885 > 0.01
% stop criterion 3, |new - previous cost|/|new cost| < reltol:	 0.08204616229530336 > 0.001
% stop criterion 4, linearized cost relative error: 0.8077494054550236 < 0.001
% Algorithm starting next step
% ======================================================
% DUD outer iteration no.2
% ======================================================
% -----------------------------------------------------
%  resultItem id: costs, outputLevel: Essential, context: any
costs{2}	=[575740.6838684512,622977.997457131,707359.2658531971,711812.150406446,720841.0968466504,721087.2174166718,722087.612048632];
% -----------------------------------------------------
% RHS norm: 1073.0709984604478
% Start search until improvement,
% % Reducing stepsize! Relative step was:[7.391487105746569,4.707104379640315,3.0490969851330772E-15,-10.416687499523672,-6.301682150073057E-15,-1.3221081581498619E-15]
%  resultItem id: linearCost, outputLevel: Normal, context: outer iteration 2
linearCost{2}	=366353.2829551506;
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 1.982E3
%      vi_5= 25
%      vi_6= 3.506E3
% ========================================================================
% prepare no 9
% Create new BBModelInstance with number: 10
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{9}	=[24.999999999999048, 24.999999999995204, 25.00000000000275, 1982.3914291341366, 25.00000000000063, 3505.588453554249];
% ========================================================================
% evaluate no. 9
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work10/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7932906854746297	2.4615726124110893E-15	0.7934285891150399	2877	-1.3320155897154913	2.251586649554927
% whalecove_jan.waterlevel		0.6058328400076073	-2.348056644951857E-15	0.605938156451689	2877	-0.9925124952112024	1.2005126170626785
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: outer iteration 2
costObserved{9}	=573296.0738898588;
%  resultItem id: costTotal, outputLevel: Essential, context: outer iteration 2
costTotal{9}	=573296.0738898588;
% SimulationKwadraticCostFunction: evaluation 9 : cost = 5.733E5
% Error estimate for this outer iteration
% stop criterion 1, imain                            > maxit :	 2 < 40
% stop criterion 2, |new - previous cost|            < abstol:	 2444.6099785923725 > 0.01
% stop criterion 3, |new - previous cost|/|new cost| < reltol:	 0.0042641317286642175 > 0.001
% stop criterion 4, linearized cost relative error: 0.9883249423416618 < 0.001
% Algorithm starting next step
% ======================================================
% DUD outer iteration no.3
% ======================================================
% -----------------------------------------------------
%  resultItem id: costs, outputLevel: Essential, context: any
costs{3}	=[573296.0738898588,575740.6838684512,622977.997457131,707359.2658531971,711812.150406446,720841.0968466504,721087.2174166718];
% -----------------------------------------------------
% RHS norm: 1070.7904313075073
% Start search until improvement,
% % Reducing stepsize! Relative step was:[-0.546462199382395,10.767627338272666,6.306614692029319,7.440787862813753E-15,-13.469295997801346,-3.027002966065833E-14]
%  resultItem id: linearCost, outputLevel: Normal, context: outer iteration 3
linearCost{3}	=362220.4971973156;
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 529.167
%      vi_5= 25
%      vi_6= 1.21E3
% ========================================================================
% prepare no 10
% Create new BBModelInstance with number: 11
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{10}	=[25.000000000001418, 24.99999999998445, 25.00000000000191, 529.16668045117, 24.999999999999616, 1210.0047896103551];
% ========================================================================
% evaluate no. 10
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work11/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8020902318114126	-3.88580769124236E-15	0.8022296651426382	2877	-1.3174194019705625	1.4430245067833758
% whalecove_jan.waterlevel		0.6312636386484871	-4.4321100609034936E-15	0.6313733759180957	2877	-0.9844179849225401	1.2241369710436412
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: outer iteration 3
costObserved{10}	=599476.1868406147;
%  resultItem id: costTotal, outputLevel: Essential, context: outer iteration 3
costTotal{10}	=599476.1868406147;
% SimulationKwadraticCostFunction: evaluation 10 : cost = 5.995E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 1.256E3
%      vi_5= 25
%      vi_6= 2.358E3
% ========================================================================
% prepare no 11
% Create new BBModelInstance with number: 12
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{11}	=[25.00000000000023, 24.999999999989825, 25.00000000000233, 1255.7790547926527, 25.000000000000124, 2357.7966215823008];
% ========================================================================
% evaluate no. 11
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work12/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7950757239890794	-5.8451507523038515E-15	0.7952139379360574	2877	-1.3093400270744926	1.4133513897426466
% whalecove_jan.waterlevel		0.6130370806540724	-8.360825053121967E-16	0.6131436494650735	2877	-0.9807753170548692	1.2275326200828265
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 1
costObserved{11}	=579980.1086994917;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 1
costTotal{11}	=579980.1086994917;
% SimulationKwadraticCostFunction: evaluation 11 : cost = 5.8E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 1.619E3
%      vi_5= 25
%      vi_6= 2.932E3
% ========================================================================
% prepare no 12
% Create new BBModelInstance with number: 13
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{12}	=[24.99999999999964, 24.999999999992514, 25.00000000000254, 1619.0852419633948, 25.000000000000377, 2931.6925375682754];
% ========================================================================
% evaluate no. 12
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work13/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7950453781747748	-8.649222831003112E-17	0.7951835868465147	2877	-1.3022335853868379	1.7305167721849788
% whalecove_jan.waterlevel		0.6097998303085899	-1.7809104885246896E-15	0.6099058363642027	2877	-1.0051206232977437	1.2168883996711224
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 2
costObserved{12}	=577674.5483753989;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 2
costTotal{12}	=577674.5483753989;
% SimulationKwadraticCostFunction: evaluation 12 : cost = 5.777E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 1.801E3
%      vi_5= 25
%      vi_6= 3.219E3
% ========================================================================
% prepare no 13
% Create new BBModelInstance with number: 14
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{13}	=[24.999999999999346, 24.999999999993857, 25.000000000002643, 1800.7383355487655, 25.0000000000005, 3218.6404955612625];
% ========================================================================
% evaluate no. 13
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work14/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7929269351157021	-7.72710888330419E-16	0.7930647755226736	2877	-1.434887544137646	2.3037460939769003
% whalecove_jan.waterlevel		0.6063687388872132	-2.3249089285692914E-15	0.6064741484905973	2877	-0.982985471311739	1.188244343792966
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 3
costObserved{13}	=573337.8653294736;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 3
costTotal{13}	=573337.8653294736;
% SimulationKwadraticCostFunction: evaluation 13 : cost = 5.733E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 1.892E3
%      vi_5= 25
%      vi_6= 3.362E3
% ========================================================================
% prepare no 14
% Create new BBModelInstance with number: 15
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{14}	=[24.999999999999197, 24.999999999994532, 25.000000000002697, 1891.564882341451, 25.00000000000057, 3362.1144745577553];
% ========================================================================
% evaluate no. 14
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work15/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7917807358383976	-1.2315452477262845E-15	0.7919183769929955	2877	-1.366940319665993	1.4256171930268002
% whalecove_jan.waterlevel		0.605387794805266	1.8404331877941438E-15	0.6054930338838197	2877	-0.9962156694835891	1.1724335681527256
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 4
costObserved{14}	=571608.7559990847;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 4
costTotal{14}	=571608.7559990847;
% SimulationKwadraticCostFunction: evaluation 14 : cost = 5.716E5
% Error estimate for this outer iteration
% stop criterion 1, imain                            > maxit :	 3 < 40
% stop criterion 2, |new - previous cost|            < abstol:	 1687.3178907741094 > 0.01
% stop criterion 3, |new - previous cost|/|new cost| < reltol:	 0.0029518755146165244 > 0.001
% stop criterion 4, linearized cost relative error: 1.1240319385169337 < 0.001
% Algorithm starting next step
% ======================================================
% DUD outer iteration no.4
% ======================================================
% -----------------------------------------------------
%  resultItem id: costs, outputLevel: Essential, context: any
costs{4}	=[571608.7559990847,573296.0738898588,575740.6838684512,622977.997457131,707359.2658531971,711812.150406446,720841.0968466504];
% -----------------------------------------------------
% RHS norm: 1069.2135015973981
% Start search until improvement,
% % Reducing stepsize! Relative step was:[-0.563268247466781,-0.07273044951796133,13.004182885729586,7.343468701988715,8.751350035173177E-15,-15.530498292082513]
%  resultItem id: linearCost, outputLevel: Normal, context: outer iteration 4
linearCost{4}	=357037.27117437933;
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 689.694
%      vi_5= 25
%      vi_6= 1.213E3
% ========================================================================
% prepare no 15
% Create new BBModelInstance with number: 16
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{15}	=[25.000000000001727, 25.000000000011088, 25.000000000000064, 689.6943130674226, 24.999999999998856, 1213.3653412095882];
% ========================================================================
% evaluate no. 15
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work16/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8050421646288333	3.571578796601749E-15	0.8051821111165708	2877	-1.3242144697694627	1.4369657427936904
% whalecove_jan.waterlevel		0.6281860255196108	-8.898589330674778E-16	0.6282952277847585	2877	-0.9776817196950234	1.2334069198722175
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: outer iteration 4
costObserved{15}	=599975.6616836269;
%  resultItem id: costTotal, outputLevel: Essential, context: outer iteration 4
costTotal{15}	=599975.6616836269;
% SimulationKwadraticCostFunction: evaluation 15 : cost = 6E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 1.291E3
%      vi_5= 25
%      vi_6= 2.288E3
% ========================================================================
% prepare no 16
% Create new BBModelInstance with number: 17
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{16}	=[25.000000000000462, 25.00000000000281, 25.00000000000138, 1290.6295977044365, 24.999999999999712, 2287.7399078836715];
% ========================================================================
% evaluate no. 16
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work17/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7963401424732782	-1.5240629938628736E-15	0.7964785762235591	2877	-1.36053747085983	1.433969858248489
% whalecove_jan.waterlevel		0.6127236741192783	-5.277625125116314E-15	0.6128301884484824	2877	-0.9873577760119576	1.1865694682246533
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 1
costObserved{16}	=580916.8910901746;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 1
costTotal{16}	=580916.8910901746;
% SimulationKwadraticCostFunction: evaluation 16 : cost = 5.809E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 1.591E3
%      vi_5= 25
%      vi_6= 2.825E3
% ========================================================================
% prepare no 17
% Create new BBModelInstance with number: 18
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{17}	=[24.99999999999983, 24.99999999999867, 25.00000000000204, 1591.0972400229439, 25.00000000000014, 2824.927191220714];
% ========================================================================
% evaluate no. 17
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work18/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7940335224606914	-9.288088961140195E-16	0.7941715552340005	2877	-1.3554152204601329	1.4209052462808835
% whalecove_jan.waterlevel		0.6087594574896842	8.210120951146482E-16	0.6088652826895259	2877	-0.9916353976100648	1.1874724777571628
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 2
costObserved{17}	=576019.8852525696;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 2
costTotal{17}	=576019.8852525696;
% SimulationKwadraticCostFunction: evaluation 17 : cost = 5.76E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 1.741E3
%      vi_5= 25
%      vi_6= 3.094E3
% ========================================================================
% prepare no 18
% Create new BBModelInstance with number: 19
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{18}	=[24.999999999999517, 24.9999999999966, 25.000000000002366, 1741.3310611821973, 25.000000000000355, 3093.5208328892345];
% ========================================================================
% evaluate no. 18
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work19/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7952783404096118	1.3842280186665556E-15	0.7954165895789157	2877	-1.3420666788273212	1.475279637345066
% whalecove_jan.waterlevel		0.6092611580497213	2.450839010903483E-16	0.6093670704639162	2877	-0.9774271542762628	1.206390392544769
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 3
costObserved{18}	=577509.8752428059;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 3
costTotal{18}	=577509.8752428059;
% SimulationKwadraticCostFunction: evaluation 18 : cost = 5.775E5
% Cost is worse! Reducing stepsize.
% Next try p=
%   Params - containing:
%      vi_1= 25
%      vi_2= 25
%      vi_3= 25
%      vi_4= 1.816E3
%      vi_5= 25
%      vi_6= 3.228E3
% ========================================================================
% prepare no 19
% Create new BBModelInstance with number: 20
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2, vi_3, vi_4, vi_5, vi_6
evaluatedParameters{19}	=[24.999999999999357, 24.999999999995566, 25.000000000002533, 1816.4479717618242, 25.000000000000462, 3227.8176537234945];
% ========================================================================
% evaluate no. 19
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model/././stochModel/././work20/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.7935286150339904	-8.341607569614662E-15	0.7936665600354728	2877	-1.7764356424908794	1.4681744721110705
% whalecove_jan.waterlevel		0.6064645761696791	-6.0687132402703625E-15	0.6065700024331729	2877	-0.988522962060332	1.1989604894058055
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: inner iteration 4
costObserved{19}	=573953.9881682076;
%  resultItem id: costTotal, outputLevel: Essential, context: inner iteration 4
costTotal{19}	=573953.9881682076;
% SimulationKwadraticCostFunction: evaluation 19 : cost = 5.74E5
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
