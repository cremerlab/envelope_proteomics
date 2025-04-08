# `processing`

This folder houses scripts used for processing and standardizing data sets. Right now, it houses a single python file `data_standardization.py` that uses literature data to add localization information, COG classification, GO classification, complex annotation, total protein mass and densities for individual proteins of the *E. coli* proteome. 

To compute masses, we assumed that the total cellular protein mass scaled exponentially with the growth rate. Using measurements of the total protein as a function of the growth rate, we computed this fit and incorporated that information into the data file. 

To compute densities, we assumed that the total cell volume scaled exponentially with the growth rate, the total cell surface area scales linearly with the growth rate, and the periplasmic width is fixed at a value of 25 nm.  Using literature measurements of cell size as a function of growth rate, we computed these fits and incorporated the compartment size into the data file. We computed the total mass density of each monomer using the appropriate compartment size based on its localization.  