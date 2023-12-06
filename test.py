# Take data from same folder and output figures in same folder
import csv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# intialize data
genes = ['GAPDH3', 'NANOG', 'NESTIN', 'OCT3/4', 'PAX6', 'SOX2'] 
genes = ['OCT3/4', 'NANOG', 'NESTIN', 'PAX6', 'SOX2']
lines = ['H1', 'A4', 'D5']

#with open(r'C:\Users\magnu\OneDrive - University of Copenhagen\3. år Bachelorprojekt\Code\qPCR\qPCR-Analysis\qPCR_result.csv', 'r') as csvfile: 
#    reader = csv.reader(csvfile)
#    for row in reader:
#        print(row)



# data analysis

# data from excel
# x = np.arange(5) 
x = np.arange(3) 
# H1 = [1, 1, 1, 1, 1] 
# A4 = [0.797, 0.657, 0.773, 0.277, 0.820]
# D5 = [0.775, 0.796, 1.06, 0.766, 3.351] 
H1 = [1, 1, 1] 
A4 = [0.797, 0.657, 0.773]
D5 = [0.775, 0.796, 1.06] 
# genes = ['OCT3/4', 'NANOG', 'SOX2', 'NESTIN', 'PAX6']
genes = ['OCT3/4', 'NANOG', 'SOX2']
H1_SEM = [0.165521162, 0.208918424, 0.164274383, 0.224433163, 0.177988335]
A4_SEM = [0.658869052, 0.137559583, 0.368063766, 1.143525544, 0.48671598]
D5_SEM = [0.119229838, 0.105311676, 0.203592049, 0.181296401, 0.088446656]
width = 0.2
error_width = 2
error_capsize = 6


# plot data in grouped manner of bar type 
plt.bar(x-0.2, H1, width, color='midnightblue') 
# plt.errorbar(x-0.2, H1, yerr=H1_SEM, color='midnightblue', capsize=error_capsize)
plt.bar(x, A4, width, color='mediumblue') 
plt.bar(x+0.2, D5, width, color='cornflowerblue') 
plt.xticks(x, genes) 
plt.xlabel("Pluripotency Markers") 
plt.ylabel("Fold change") 
plt.legend(["H1 CTRL", "H1 A4", "H1 D5"]) 
plt.ylim([0, 1.5])
plt.show() 

# Export 


# more changes
