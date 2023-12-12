import pandas as pd
import os
import numpy as np
import scipy.stats as stats

# REMEMBER TO UPDATE
n_lines = 3
n_markers = 4
housekeeping_gene = 'GAPDH 3'
control = 'H1 CTRL'

# get data
filename = "Data.xlsx"
path = r'C:/Users/magnu/OneDrive/Dokumenter/Test/'
file_path = os.path.join(path, filename)
df = pd.read_excel(file_path)

# get house keeping gene
dfr = df.loc[df['Target'] == housekeeping_gene].reset_index()

# add repetition order column
dfr['sample_index'] = np.arange(n_lines).repeat(n_lines)
repeated_df = pd.concat([dfr] * n_markers, ignore_index=True)
# add index according to number of repetition
repeated_df['index1'] = np.sort(np.repeat(np.arange(n_lines), n_markers * n_lines))
# sort according to repetition order and index
repeated_df.sort_values(['sample_index', 'index1'], inplace=True)
repeated_df.reset_index(inplace=True)

# get other genes
dfm = df.loc[df['Target'] != housekeeping_gene].reset_index()

# subtract house keeping gene
dfm['Cq'] = dfm['Cq'] - repeated_df['Cq']


# averaging
dfm_average = dfm.groupby(['Sample', 'Target'])['Cq'].mean().reset_index()
# calculate std
dfm_std = dfm.groupby(['Sample', 'Target'])['Cq'].std().reset_index()
# add std to same dataframe
dfm_average['std'] = dfm_std['Cq']

# calculate ddCT
# get control line
dfc = dfm_average.loc[dfm_average['Sample'] == control].reset_index()
# repeat
dfc_repeat = pd.concat([dfc] * n_lines, ignore_index=True)

# sort both by target and sample to get the same order
dfc_repeat.groupby(['Target', 'Sample'])
dfc_repeat.reset_index()
dfm_average.groupby(['Target', 'Sample'])
dfm_average.reset_index()

# calculate ddCT
dfm_average['ddCT'] = dfm_average['Cq'] - dfc_repeat['Cq']

# calculate fold change including upper and lower bound
dfm_average['Fold change'] = 2**-(dfm_average['ddCT'])
dfm_average['Lower bound'] = dfm_average['Fold change'] - 2**-(dfm_average['ddCT'] + dfm_average['std'])
dfm_average['Upper bound'] = 2**-(dfm_average['ddCT'] - dfm_average['std']) - dfm_average['Fold change']


# calculate p-values
print(dfm)
dfm_average['p-values'] = np.arange(12)

# maybe make function for every sample ? 

# export 
# dfm_average.to_csv('result.csv', index=False)


print(dfm_average)
