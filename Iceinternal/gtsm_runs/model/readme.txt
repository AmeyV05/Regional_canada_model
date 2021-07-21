Model gtsm4.1 (1.25eu grid and 5km grid available)
SVN location: https://repos.deltares.nl/repos/global_tide_surge_model/trunk/gtsm4.1

Contains (same as EM74):
- grid: step11_global_*_net.nc:
	- resolutions (defined by the *_net.nc file, the illegalcells_*.pol and the selected_*_obs.xyn (should be edited in the mdu file):
		- 1.25eu (default): 25km base grid, refined up to 2.5km at the coast and up to 1.25km in Europe
		- 5km: 50km base grid, refined up to 5km at the coast
	- grid is equal to gtsm3 and gtsm4.0, but improved bathymetry w.r.t. gtsm3 (new bathy sets, derived in EM04_bathy_new)
	- the origin of the 5km bathymetry is unknown
- external forcing file: gtsm_forcing.ext:
	- Uniform Chezy value of 62.5 (was 77 in gtsm4.0)
	- IT friction coefficient sample file: itfrictioncoeff_1_dmin500_gebco_January_withoutNaN_BVnew.asc
	- asc file provides faster (80 instead of 190 seconds) and less memory intensive interpolation (bilinear instead of triangulation), so partitioning on Cartesius is not necessary anymore
- gtsm_model.mdu:
	Doodsoneps = 0.00 (was 0.03 in gtsm3, with the new setting nodal factors are included)
	Conveyance2D = 2 (was 3 in gtsm3, MIA showed that 2 was more stable)
	Advectype = 33 (faster and equal results)
	UnifFrictCoef = 0.028 (was a Chezy value in  gtsm3 and gtsm4.0)
	UnifFrictType = 1 (Manning, was Chezy in gtsm3 and gtsm4.0)
	further improvements: removed unused keywords, updated some comments, added default values for Doodsonstart and Doodsonstop
- added new submit script for h6c7 with dummy dimr.xml file and also an sbatch script for cartesius:
	- CAUTION: minimum D-FlowFM version is dimrset 2.16.05 (OSS 68758) due to asc interpolation fix and reduction of filesize of *.dia and *.o* files

Calibration:
- calibration is result of PhD Xiaohui Wang paper 3 (with removal of SA/SSA, the calibrated results in EX8_second_loop, 110 boxes for bathymetry, 19 boxes for bottom friction)
- depthcorrection_110_new.xyz
- friction_correction_19.xyz
- comment these files in extfile if you want to use the uncalibrated model

Used for:
- now using gtsm4.0_1.25eu (so update to this gtsm4.1 version): PhD Amey, GLOSSIS, SEADRIF, ?LAT EMODnet?

Todo for next version:
- decide on Conveyance2D and Limtypmom (with new grid)
- smagorinsky back to default setting (0.2)?
- update mdu order/comments to correspond with diafile (any missing parameters?)
