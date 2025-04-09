#%%
import numpy as np 
import pandas as pd 
import scipy.stats

# Load localization data
lcz = pd.read_csv('../../data/sources/gene_localization_annotation.csv')
lcz['name'] = lcz['name'].str.lower()

# Load annotated complexes
ann = pd.read_csv('../../data/sources/Belliveau2021_annotated_complexes.csv')
ann.rename(columns={'gene_name':'name'}, inplace=True)
ann['name'] = ann['name'].str.lower()
ann = ann[['name', 'go_terms', 'cog_class', 'cog_category', 'cog_letter',
            'gene_product', 'complex', 'complex_annotation', 'n_subunits']]

# Merge to create a mapper.
mapper = pd.merge(ann, lcz, on='name', how='inner')
mapper.drop_duplicates(inplace=True)

#%% 
# Load mass spectrometry data 
mass_spec = pd.read_csv('../../data/sources/collated_literature_mass_spectrometry.csv')
mass_spec.loc[mass_spec['source']=='This Study', 'source'] = 'Chure et al. 2025'
mass_spec = mass_spec[['strain', 'carbon_source', 'growth_rate_hr', 'replicate', 'name', 'mass_frac', 'source']]

# Merge with annotation
merged = pd.merge(mass_spec, mapper, on='name', how='inner')

#%%
# Load the total protein and size data to compute masses and densities
prot_data = pd.read_csv('../../data/sources/collated_literature_total_protein.csv')
size_data = pd.read_csv('../../data/sources/collated_literature_size_data.csv')

# Compute empirical fits as a function of growth rate
prot_fit = scipy.stats.linregress(prot_data['growth_rate_hr'], np.log(prot_data['fg_protein_per_cell']))
vol_fit = scipy.stats.linregress(size_data['growth_rate_hr'], np.log(size_data['volume_um3']))
sa_fit = scipy.stats.linregress(size_data['growth_rate_hr'], size_data['surface_area_um2'])

# As a function of the growth rate, compute the quantities
tot_prot = np.exp(prot_fit[1] + prot_fit[0] * merged['growth_rate_hr'])
tot_vol = np.exp(vol_fit[1] + vol_fit[0] * merged['growth_rate_hr'])
tot_sa = sa_fit[1] + sa_fit[0] * merged['growth_rate_hr']
W_PERI = 0.025

# Compute the compartment size
compartment_size = []
local_group = []
for i, (localization, growth_rate_hr) in enumerate(zip(merged['localization'].values,
                                        merged['growth_rate_hr'].values)):
    if localization == 'CP':
        compartment_size.append(tot_vol[i] - tot_sa[i] * W_PERI)
        local_group.append('cytoplasm')
    elif localization in ['LPI', 'IM', 'OM', 'LPO']:
        compartment_size.append(tot_sa[i])
        local_group.append('envelope')
    elif localization == 'PE':
        compartment_size.append(tot_sa[i] * W_PERI)
        local_group.append('envelope')
    else:  # Corresponds to the extracellular localization
        compartment_size.append(np.inf)
        local_group.append('extracellular')

# Compute the per-protein total mass
merged['monomer_mass_fg_per_cell'] = merged['mass_frac'] * tot_prot
merged['monomer_density_fg_per_compartment_size'] = merged['monomer_mass_fg_per_cell'] / np.array(compartment_size)
merged['localization_group'] = local_group
merged.to_csv('../../data/complex_abundance_densities.csv', index=False)

#%%
# Generate a list of all the proteins and complexes within each localization group
grouping = merged[['name', 'gene_product', 'complex_annotation', 'localization',
                   'go_terms', 'localization_group']]
grouping = grouping[grouping['localization_group'] == 'envelope']
grouping.drop_duplicates(inplace=True)
grouping.to_csv('../../data/envelope_complexes.csv', index=False)
