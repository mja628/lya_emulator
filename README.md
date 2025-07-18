Code for generating and using Lyman-alpha forest emulators 
====

This is the code repository for [arXiv:1812.04654](https://arxiv.org/abs/1812.04654), Bird et al 2019.
It handles creating simulation suites with carefully chosen points, generating simulation parameter files,
generating flux power spectra using `fake_spectra` and making an interpolator from these flux power spectra.
It also has a python likelihood function which can be fed to cobaya for: testing the convergence of the emulator with mock data, or sampling against BOSS DR14/DR9 data.

To adapt this to your own survey you want to subclass the Emulator class in `coarse_grid.py` and specify your
own parameter set and limits. An example of how to do this can be found in the `KnotEmulator` class. You may also
want to add your cluster (if it is not XSEDE's Stampede) to `clusters.py` in `SimulationRunner`

Useful submodules:
- `lyaemu.coarse_grid`: handles the emulator generation.
- `lyaemu.likelihood`: handles the likelihood sampling using cobaya.
- `lyaemu.latin_hypercube`: generates points on a unit cube in a maximin latin hypercube
- `lyaemu.gpemulator`: fits the interpolation using GPy.
- `lyaemu.mean_flux`: models for the redshift evolution of the forest mean flux.
- `lyaemu.bayesian_opt`: perform Bayesian optimization (acquisition function) on an emulator.

Other files:
- `coarse_grid_plot.py`: Makes a few useful plots which show the accuracy of the emulator, as well as the emulator's own error estimate.
- `flux_power.py`: generates the flux power spectra, using native bins as a fraction of the simulation box
- `linear_theory.py`: linear biasing model for the flux power spectrum
- `linear_emulator.py`: emulates the linear biasing model about. For testing purposes, only lightly maintained.
- `lyman_data.py`: loads flux power spectrum data, BOSS DR14 by default (DR9 available).
- `matter_power.py`: simple sub-emulator for reading and emulating the matter power spectrum
- `plot_latin_hypercube.py`: Small script for visualising latin hypercubes
- `quadratic_emulator.py`: Subclass of Emulator that varies one parameter at a time, for quadratic polynomial interpolation.
- `tempdens.py`: Prints the IGM thermal parameters, T0 and gamma.

- `plots`: Contains scripts for making the plots in the paper. Data not included.
- `plots/make_emulators.py` gives an example of how to generate an emulator
- `lyaemu/tests`: Some simple unit tests.

Dependencies:
- Python 3
- GPy
- numpy
- scipy
- h5py
- matplotlib for the plots
- cobaya for the sampling
- fake_spectra module for generating flux power spectra from a simulation snapshot.
- SimulationRunner (not on pip: at https://github.com/sbird/SimulationRunner) for setting up MP-Gadget simulations.
