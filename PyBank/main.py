# Import modules for file pathing and csv files 
import os 
import csv

# Find the path to the budget_data.csv file 
filePath = os.path.join("Resources", "budget_data.csv")

# Read the csv file and store the header and first row
with open(filePath,'r') as budgetData:
    csvReader = csv.reader(budgetData,delimiter=",")
    header = next(csvReader)
    firstRow = next(csvReader)

    # set different variables/lists that will be manipulated in the loop 
    monthCounter = 1 # Hold 1 as we need to account for the firstRow that will be skipped over in the loop
    totalProfit = int(firstRow[1]) # Hold the first revenue that will be skipped over in the loop
    monthlyChanges = [] # empty list to add the monthly changes
    months = [] # empty list to add the months (parallel list to monthly changes)
    previousRevenue = int(firstRow[1]) # setting a variable for the previous revenue

    # loop through the file
    for row in csvReader:

    # calculate different variables 
        monthCounter += 1 # add 1 to the total months
        totalProfit += int(row[1]) # add profit to the totalProfit
        netChange = int(row[1]) - previousRevenue # calculating the first net change
        monthlyChanges.append(netChange) # append first net change to the monthlyChanges list
        months.append(row[0]) # populate a list that includes all the months where a change occured
        previousRevenue = int(row[1]) # update the previous revenue value
      
# Outside the loop      
# Calculate the average net change 
averageChange = sum(monthlyChanges)/len(monthlyChanges)
# Calculate the index of the max and lowest value 
greatestIncreaseIndex = monthlyChanges.index(max(monthlyChanges))
greatestDecreaseIndex = monthlyChanges.index(min(monthlyChanges))


# Generate the outputs
output = (
f"Financial Analysis"
f"\n----------------------------"
f"\nTotal Months: {monthCounter}"
f"\nTotal: ${totalProfit}"
f"\nAverage Change: ${averageChange:.2f}"
f"\nGreatest Increase in Profits: {months[greatestIncreaseIndex]} (${monthlyChanges[greatestIncreaseIndex]})"
f"\nGreatest Decrease in Profits: {months[greatestDecreaseIndex]} (${monthlyChanges[greatestDecreaseIndex]})"
)

print(output)

# create the file path for the outputs of the analysis
outputFile = os.path.join("analysis", "budget_analysis.csv")

# export the output to the text file
with open(outputFile, "w") as textFile:
    textFile.write(output)
