import numpy as np
import csv
import pandas as pd
from numpy import *

def readdata(filename):
   reader = np.genfromtxt(filename, dtype=[('mystring','S5'),('myfloat','f8')], delimiter=",",skip_header=1)
   return reader

def remove_nan(data):
    for i in data:
        if isnan(i[1]):
            i[1] = 0

def writetofile(filename, data):
    csvfile = file(filename, 'wb') ## write to a csv file
    writer = csv.writer(csvfile)
    writer.writerows(data)
    csvfile.close()
    
raw_data = readdata('population.csv')
remove_nan(raw_data)
writetofile("population_cleaned.csv",raw_data)