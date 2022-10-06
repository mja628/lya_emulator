from distutils.core import setup

setup(
    name="lyaemu",
    version='1.0.0',
    author="Simeon Bird and Keir Rogers",
    author_email="spb@ias.edu",
    url="http://github.com/sbird/lya_emulator",
    description="Module for easily generating emulators for the lyman alpha forest from simulations",
    packages = ['lyaemu', 'lyaemu.tests', 'lyaemu.SimulationRunner.SimulationRunner', 'lyaemu.meanT'],
    requires=['numpy', 'fake_spectra','scipy', "GPy", "cobaya", "h5py"],
    package_data = {
            'lyaemu': ['data/boss_dr14_data/*.dat','data/*'],
           },
    classifiers = ["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: MIT License",
                   "Programming Language :: Python :: 3",
                   "Topic :: Scientific/Engineering :: Astronomy",
                   "Topic :: Scientific/Engineering :: Visualization"]
)
