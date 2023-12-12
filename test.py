# Take data from same folder and output figures in same folder
import csv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#with open(r'C:\Users\magnu\OneDrive - University of Copenhagen\3. år Bachelorprojekt\Code\qPCR\qPCR-Analysis\qPCR_result.csv', 'r') as csvfile: 
#    reader = csv.reader(csvfile)
#    for row in reader:
#        print(row)


# DATA ANALYSIS

# data from excel
x = np.arange(3)
H1_CTRL = [1, 1, 1] 
A4 = [0.797, 0.657, 0.773]
D5 = [0.775, 0.796, 1.06] 

genes = ['OCT3/4', 'NANOG', 'SOX2']

H1_SD = [0.286691063, 0.361857326, 0.284531578]
A4_SD = [1.141194673, 0.238260186, 0.637505143]
D5_SD = [0.206512137, 0.182405174, 0.352631773]

width = 0.6 # bar width
error_width = 2
error_capsize = 6

# combining data
values = []
SD = []

for i in range(len(genes)):
    values.append(H1_CTRL[i])
    values.append(A4[i])
    values.append(D5[i])
    SD.append(H1_SD[i])
    SD.append(A4_SD[i])
    SD.append(D5_SD[i])

# print(values)
# print(SEM)

markers = ['OCT3/4']*3 + ['NANOG']*3 + ['SOX2'] * 3
cell_line = ['H1', 'A4', 'D5'] * 3
errors = []

# errors should be positive, and defined in the order of lower, upper 
# ie. error = [[lower, lower], [upper, upper]]

# Probably easier long term
# https://pandas.pydata.org/docs/user_guide/visualization.html

H1_error = [[0.18, 0.221837871, 0.178991865], [0.22, 0.285079244, 0.218014728]]
A4_error = [[0.45, 0.100017331, 0.276251922], [0.9, 0.117977374, 0.429747618]]
D5_error = [[0.229849966, 0.094512722, 0.229849966], [0.29349262, 0.107250592, 0.29349262]]

errors = [H1_error] + [A4_error] + [D5_error]
# print('Error shape:', np.shape(errors))

data = {
    'marker': markers,
    'cell line': cell_line,
    'normalized value': values,
}

df = pd.DataFrame(data)
print(df)
# pivot the data for plotting
dfp = df.pivot_table(index='marker', columns='cell line', values='normalized value', sort=False)
# print('DF data:\n', dfp, '\nwith shape', dfp.shape)

# Significance 
#https://stackoverflow.com/questions/11517986/indicating-the-statistically-significant-difference-in-bar-graph 
bars = np.arange(len(values))

# PLOTTING 
colors = ['midnightblue', 'mediumblue', 'cornflowerblue']
fig, ax = plt.subplots()
ax.set_ylim(0, 1.8)
dfp.plot.bar(yerr=errors, ax=ax, capsize=4, rot=0, width=width, color=colors)
plt.xlabel("Markers")
plt.ylabel("Fold change")
plt.title("qPCR")
plt.show()

# EXPORT 

