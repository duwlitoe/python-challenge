# Import os module
import os

# Module for reading CSV files
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")





# Add total number of months of data included
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']



    

