import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import csv 
filename = 'result.csv'
df = pd.read_csv(filename)

# Get name of control line
control = 'H1 CTRL'

width = 0.6 # bar width
error_width = 2
error_capsize = 6 

# get the right order so control line is first in plot
dfc = df.loc[df['Sample'] == control].reset_index() # get control
dfm = df.loc[df['Sample'] != control].reset_index() # get other lines
df_combined = pd.concat([dfc, dfm]) # concatenate

# pivot data for plotting
dfp = df_combined.pivot_table(index='Target', columns='Sample', values='Fold change', sort=False)

# error bars
# errors should be positive, and defined in the order of lower, upper. Should be shape(line, 2, target)
df_lower = df_combined.pivot_table(index='Target', columns='Sample', values='Lower bound', sort=False) # output is shape(target, line)
df_upper = df_combined.pivot_table(index='Target', columns='Sample', values='Upper bound', sort=False)
# getting the right dimensions
error = np.stack((df_lower.to_numpy().T, df_upper.to_numpy().T), axis=1) #.T transposes and then stack in axis=1 to get (X, 2, Y)
print(np.shape(error))

# significance


# plotting
fig, ax = plt.subplots()
ax.set_ylim(0, 5)
dfp.plot.bar(yerr=error, ax=ax, capsize=4, rot=0, width=width)
plt.xlabel("Markers")
plt.ylabel("Fold change")
plt.title("qPCR")
plt.show()

