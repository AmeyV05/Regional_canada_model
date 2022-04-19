About the experiment

In this experiment, we are trying to re-calibrate (after Xiaohui's calibration) the bathymetry and bottom friction in the canadian region.

Here, the approach is that:
we run for the month of September the calibration of bathymetry and bf.

Now we have different bathymetry and bottom friction polygons which are based on sensitivity and velocity analysis. 

Again, the idea is to optimize bathymetry first and then bottom friction. with 4.1 having bathymetry and 4.2 bf.

now after runs on 4.1 and 4.2 and also 5 versions. IT is seen that, 4 Tg were extremely inaccurate which could be due to inaccuracies
in the wl computation from gtsm. (the grid might be on land or cutcells issue)

So, we have a reduced version 'r''with 4.1r for bathymetry only.

Further, with 40% limits we converge to a nice distribution of parameter values which are optimal. changing limits doesn't affect the conversion.

And so does changin the outer iterations.



The sea ice is modelled as fast ice and drifting sea ice separately. With the two separate regions for them.

In september we assume almost no fast ice. And so, we are left with only drifting sea ice. 

We use only CHS TG observations of the 154 TG. 


Please note that the observations are not available through stochObserver, but we point to another folder for the same. 

In snellius we would likewise need such a folder. 