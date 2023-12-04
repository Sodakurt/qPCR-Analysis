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
x = np.arange(5) 
H1 = [1, 1, 1, 1, 1] 
A4 = [0.797, 0.657, 0.277, 0.820, 0.773]
D5 = [0.775, 0.796, 0.766, 3.351, 1.06] 
width = 0.2

# plot data in grouped manner of bar type 
plt.bar(x-0.2, H1, width, color='cyan') 
plt.bar(x, A4, width, color='orange') 
plt.bar(x+0.2, D5, width, color='green') 
plt.xticks(x, genes) 
plt.xlabel("Genes") 
plt.ylabel("Fold change") 
plt.legend(["H1 CTRL", "H1 A4", "H1 D5"]) 
plt.show() 

# Export 


# more changes
