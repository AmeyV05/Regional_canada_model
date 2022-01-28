% OpenDA version 3.0.2.-1 April 24 2021
% opening :/p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model_12dom/././stochObserver/noosObservations.xml
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
% opening :/p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model_12dom/././algorithm/dudAlgorithm.xml
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
%  Algorithm  outerLoop@maxIterations=10
%  Algorithm  outerLoop@absTolerance=0.01
%  Algorithm  outerLoop@relTolerance=0.01
%  Algorithm  outerLoop@relToleranceLinearCost=0.001
%  Algorithm  lineSearch@maxIterations=5
%  Algorithm  lineSearch@maxRelStepSize=10.0
%  Algorithm  lineSearch/backtracking@startIterationNegativeLook=3
%  Algorithm  lineSearch/backtracking@shorteningFactor=0.5
%  Algorithm  constraints@parameterConstraint=false
%  Algorithm  constraints/lowerbounds@Lbounds=null
%  Algorithm  constraints/upperbounds@Ubounds=null
% Application initializing finished
% Initializing Algorithm
% Evaluating with parameters 
% Params - containing:
%    vi_1= 0
%    vi_2= 0
% ========================================================================
% prepare no 1
% Create new BBModelInstance with number: 2
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2
evaluatedParameters{1}	=[0.0, 0.0];
% ========================================================================
% evaluate no. 1
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model_12dom/././stochModel/././work2/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8714806722945511	3.973058861073131E-15	0.8716321682839263	2877	-1.3971565390321268	1.5413906825969592
% whalecove_jan.waterlevel		0.7115388733115251	8.425335082384855E-16	0.7116625654242906	2877	-1.079851162364157	1.3956871725246556
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 0
costObserved{1}	=728321.8314415957;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 0
costTotal{1}	=728321.8314415957;
% SimulationKwadraticCostFunction: evaluation 1 : cost = 7.283E5
% Evaluating with parameters 
% Params - containing:
%    vi_1= 1E3
%    vi_2= 0
% ========================================================================
% prepare no 2
% Create new BBModelInstance with number: 3
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2
evaluatedParameters{2}	=[1000.0, 0.0];
% ========================================================================
% evaluate no. 2
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model_12dom/././stochModel/././work3/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8462597705314839	1.7986371940448276E-15	0.846406882183274	2877	-1.3607517110482301	1.505086328056311
% whalecove_jan.waterlevel		0.6617389184514286	-5.628364527915375E-15	0.6618539534663698	2877	-1.0064417011852642	1.3057923921857282
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 1
costObserved{2}	=664042.6689607897;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 1
costTotal{2}	=664042.6689607897;
% SimulationKwadraticCostFunction: evaluation 2 : cost = 6.64E5
% Evaluating with parameters 
% Params - containing:
%    vi_1= 0
%    vi_2= 1E3
% ========================================================================
% prepare no 3
% Create new BBModelInstance with number: 4
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2
evaluatedParameters{3}	=[0.0, 1000.0];
% ========================================================================
% evaluate no. 3
% NetcdfDataObject: station_id variable found in netcdf file /p/1230882-emodnet_hrsm/fromAmey/Regional_canada_model/model_development/Openda_models/basic_test_model_12dom/././stochModel/././work4/output/canada_model_0000_his.nc
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'churchill_jan.waterlevel'.
% Getting model values at observed coordinates for scalar observation exchangeItem with id 'whalecove_jan.waterlevel'.
% 
% -------------------------------------------------------------------------------------------------------------------------------------------
% RESIDUAL STATISTICS:
% -------------------------------------------------------------------------------------------------------------------------------------------
% ObsID		RMS		Bias		STD		Num of data		Min		Max
% -------------------------------------------------------------------------------------------------------------------------------------------
% churchill_jan.waterlevel		0.8306054734822005	-3.3409147844054576E-15	0.8307498638307009	2877	-1.348952796074247	1.447951207229495
% whalecove_jan.waterlevel		0.6764056785073326	6.504074622631917E-15	0.6765232631546373	2877	-1.0264325477971492	1.3146255871697092
% -------------------------------------------------------------------------------------------------------------------------------------------
%
%  resultItem id: costObserved, outputLevel: Essential, context: initialization node 2
costObserved{3}	=660231.2763727412;
%  resultItem id: costTotal, outputLevel: Essential, context: initialization node 2
costTotal{3}	=660231.2763727412;
% SimulationKwadraticCostFunction: evaluation 3 : cost = 6.602E5
% Algorithm initialized
% Algorithm starting next step
% ======================================================
% DUD outer iteration no.1
% ======================================================
% -----------------------------------------------------
%  resultItem id: costs, outputLevel: Essential, context: any
costs{1}	=[660231.2763727412,664042.6689607897,728321.8314415957];
% -----------------------------------------------------
% RHS norm: 1149.1138119200737
% Start search until improvement,
% % Reducing stepsize! Relative step was:[12.260734371113964,-8.11787294767279]
%  resultItem id: linearCost, outputLevel: Normal, context: outer iteration 1
linearCost{1}	=440820.8939760024;
% Next try p=
%   Params - containing:
%      vi_1= 1E4
%      vi_2= -2.379E3
% ========================================================================
% prepare no 4
% Create new BBModelInstance with number: 5
% Instance initialization done
%  resultItem id: evaluatedParameters, outputLevel: Essential, context: any
%  Params: 
vi_1, vi_2
evaluatedParameters{4}	=[10000.0, -2378.966787830971];
