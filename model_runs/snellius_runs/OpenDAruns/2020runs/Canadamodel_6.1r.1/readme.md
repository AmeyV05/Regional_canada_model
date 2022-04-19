About the experiment

In this experiment, we are trying to re-calibrate (after Xiaohui's calibration) the bathymetry and bottom friction in the canadian region.

Here, the approach is that:
we run for the month of September the calibration of bathymetry and bf.

Now we have different bathymetry and bottom friction polygons which are based on sensitivity and velocity analysis. 

Again, the idea is to optimize bathymetry first and then bottom friction. with 4.1 having bathymetry and 4.2 bf.

After 4.* and 5 it is realised that the parameters nicely converge to certain values but there is still room for improvement.

After analysing the region and the flow of velocity. 

1. The outside of hudson strait near labrador sea there are a lot of Tg which are not accurate in our model. 
There was also no parameter here. So, we add a parameter here. It is hypothesized that adjusting the flow outside the 
hudson strait can affect the flow in ungava bay. 
2. Also, certain parameters were addes at the top right (don't know the region name) and near the Kei..** region next to the 
highly sensitive bay above hudson bay.

So a new v4 bathymetry was created and we do optimization for this bathymetry.

The sea ice is modelled as fast ice and drifting sea ice separately. With the two separate regions for them.

In september we assume almost no fast ice. And so, we are left with only drifting sea ice. 

We use only CHS TG observations of the 154 TG. 


Please note that the observations are not available through stochObserver, but we point to another folder for the same. 

In snellius we would likewise need such a folder. 