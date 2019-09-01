# Import os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

profit = []
monthly_changes = []
date = []

count = 0
total_profit = 0
total_change_profit = 0
initial_profit = 0

# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

# Total number of months in dataset

    for row in csvreader:
        count = count + 1


# Append for date and profits

        date.append(row[0])
        profit.append(row[1])

# Average change of Profit/Losses over entire period

        total_profit = total_profit + int(row[1])
        final_profit = int(row[1])
      
        monthly_change_profit = final_profit - initial_profit
        monthly_changes.append(monthly_change_profit)
      
        total_change_profit = initial_profit - monthly_change_profit
        initial_profit = final_profit
        average_change_profit = (total_change_profit/count)

# Greatest increase and decrease in profits and losses
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

# Date of increase and decrease 
        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

print("Financial Analysis")    
print("-------------------------")    
print("Total Months: " + str(count))
print("Total: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(int(average_change_profit)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits))
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits))

# Export text file

output_path = os.path.join("output", "Financial Analysis.txt")
with open(output_path, 'w', newline='') as text_file:

   #print("Financial Analysis", file=text_file)
   #print("-------------------------", file=text_file)
  # print("Total Months: " + str(count), file=text_file)
  # print("Total: " + "$" + str(total_profit), file=text_file)
  # print("Average Change:  " + "$" + str(int(average_change_profit), file=text_file)
   #print("Greatest Increase in Profits: "+ str(increase_date) + " ($" + str(greatest_increase_profits), file=text_file)
  # print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits), file=text_file)


 csvfile.close()











   

