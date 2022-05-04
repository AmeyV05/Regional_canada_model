After a lot of experimentation we noted the following things.

1. Bottom friction and bathymetry needed to be calibrated together. There is a clear dependence of it. 
2. The initial idea was only viscosity calibration for sea ice as fast ice is neglible. And it turns out this viscosity should also be added in the paramter mix so for september we should calibrate bf, bathy, vis all together in a simultaneous manner.
3. But calibration of viscosity and fast ice friction for march gave weird results. With viscosity calibration running to zero almost always. Even dflowfm used to take a lot of time for convergence. 
4. LAteron we analysed and studied the cause and it was noted that horizontal shear shouldn't exceed vertical shear. So when the viscostiy was high this horizontal shear was extremely high (much higher than the vertical shear from fast ice friction) this meant that we dissipating way more energy. (which explains the extremely low amplitudes in march)
5. Thus ,the idea was to have a sort of limit where in we switch from horizontal to vertical shear from fast ice. This limit was on the visocity and determined from dimensional analysis. The details are found in jupyter notebook named new ice parametertization.
6. Thus the new idea was september calibration of fast ice, viscosity, bf and bathyemtry coefficients and for march only fast ice and viscosity coefficient.s

