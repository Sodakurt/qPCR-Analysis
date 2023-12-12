import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import csv 
filename = 'result.csv'
df = pd.read_csv(filename)
# print(df)

# renaming control to get right order
control = 'H1 CTRL'

width = 0.6 # bar width
error_width = 2
error_capsize = 6 

# get the right order so control line is first
dfc = df.loc[df['Sample'] == control].reset_index() # get control
dfm = df.loc[df['Sample'] != control].reset_index() # get other lines
df_combined = pd.concat([dfc, dfm]) # concatenate

# print(df_combined['Lower bound'])


# pivot data for plotting
dfp = df_combined.pivot_table(index='Target', columns='Sample', values='Fold change', sort=False)
print(np.shape(dfp))

# error bars
# errors should be positive, and defined in the order of lower, upper 
# groups (cell lines) x 2 x bars (target)
# eg. (4, 2, 3)
df_lower = df_combined.pivot_table(index='Target', columns='Sample', values='Lower bound', sort=False)
df_upper = df_combined.pivot_table(index='Target', columns='Sample', values='Upper bound', sort=False)

error = np.stack((df_lower.to_numpy().T, df_upper.to_numpy().T), axis=1)

# significance


# plotting
fig, ax = plt.subplots()
ax.set_ylim(0, 5)
dfp.plot.bar(yerr=error, ax=ax, capsize=4, rot=0, width=width)
plt.xlabel("Markers")
plt.ylabel("Fold change")
plt.title("qPCR")
plt.show()

