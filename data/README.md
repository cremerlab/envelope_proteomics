# `data`
This folder houses the data used in the work. The subdirectory `sources` houses the literature data files from which the two important data files `complex_abundance_densities.csv` and `envelope_complexes.csv` were generated.

These two files are the meat of the project:

* `complex_abundance_densities.csv`: This file shows the per-protein cell mass and compartment density for each protein detected in the mass spectrometry data. Each protein has *at least one* annotated complex membership as well as information about the total subunit abundance within each complex. Some proteins can be found in multiple complexes. 

* `envelope_complexes.csv`: This file serves as a lookup table of every protein within the cell envelope (including inner membrane, outer membrane, periplasm, and lipo-polysaccharide associated proteins).  