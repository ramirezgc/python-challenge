import os
import csv

filename = "budget_data.csv"
path ="Resources"

file = os.path.join(path,filename)

#Calculate the Total Month using a row count
#Calculate the net total by sum of the profit/loss column
#Average profit/loss over the entire period 
#Greatest increase in profits with date and amount
#Greatest decrease in losses with date and amount


Total_Months = 0
Net_Total = 0
Last_Budget = 0
Change = 0
Greatest_Increase = 0
Greatest_Decrease = 0
Greatest_Increase_Date = ""
Greatest_Decrease_Date = ""

with open(file) as csvFile:
    csvFile.readline()
    reader = csv.reader(csvFile)
    Change_Count = 0
    Net_Difference = 0
    for row in reader:
        Total_Months += 1
        Begin_Budget = int(row[1])
        Net_Total += Begin_Budget
        if Last_Budget != 0:
            Net_Difference = Begin_Budget-Last_Budget
            Change += Net_Difference
            Change_Count += 1
        Last_Budget = Begin_Budget

        if Net_Difference > Greatest_Increase:
            Greatest_Increase = Net_Difference
            Greatest_Increase_Date = row[0]

        if Net_Difference < Greatest_Decrease:
            Greatest_Decrease = Net_Difference
            Greatest_Decrease_Date = row[0]


Output = f"""
Financial Analysis
----------------------------
Total Months: {Total_Months}
Total: ${Net_Total}
Average  Change: ${Change/Change_Count:.2f}
Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase:,})
Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease:,})
"""

print(Output)

with open('analysis.txt', 'w') as Output_File:
    Output_File.write(Output)
