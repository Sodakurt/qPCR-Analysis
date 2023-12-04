# Take data from same folder and output figures in same folder
import csv
import os

# intialize data
genes = ['GAPDH3', 'NANOG', 'NESTIN', 'OCT3/4', 'PAX6', 'SOX2'] 
lines = ['H1', 'A4', 'D5']

with open(r'C:\Users\magnu\OneDrive - University of Copenhagen\3. år Bachelorprojekt\Code\qPCR\qPCR-Analysis\qPCR_result.csv', 'r') as csvfile: 
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)




# data analysis


# setting up figures


# Export 


# more changes
