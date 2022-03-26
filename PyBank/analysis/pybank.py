#1)The total number of months included in the dataset
#2)The net total amount of "Profit/Losses" over the entire period
#3)The changes in "Profit/Losses" over the entire period,
#4)average of those changes in profit/losses
#5)The greatest increase in profits (date and amount) over the entire period. The greatest decrease in profits (date and amount) over the entire period
#6) export a text file with the results.
import os
import csv

#define the path and open document from computer.
budget_data = os.path.join("/Users/annepizzini/Desktop/python-challenge/PyBank/Resources","budget_data.csv")

#variables
TotalMonths = []
TotalProfit = []
Change = []
IncreaseProfit = []
DecreaseProfit = []
IncreaseMonth = []
DecreaseMonth = []
Average = []

# Open and read csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        #grab all the months for TotalMonths and create a list
        TotalMonths.append(row[0])
        #add a placement for the total profit/loss
        TotalProfit.append(int(row[1]))

#(checked and working) Print statment for starting analysis including "Financial Analysis" and "--------------"
    print("Financial Analysis")
    print("-----------------------------------------")

#1)(checked and working)find the total number of months included in the dataset
    print(f"Total Months: {len(TotalMonths)}")

#2(checked and working)The total amount of "Profit/Losses" over the entire period.
    print(f"Total Profits: {sum(TotalProfit)}")

#3) (checked and working) The changes in "Profit/Losses" over the entire period and average of those changes
    #3.a) first, define a new list (profit). Use range(len(TotalProfit)to find length.
    for profit in range(len(TotalProfit)-1):
    #3.b) find profit change between months use our new list of profits and use an append
        Change.append(TotalProfit[profit+1]-TotalProfit[profit])
#4) Find the average (sum of all the differences added together and then divided by the total months)
    print(f"Average Sum: $ {round(sum(Change))/len(TotalMonths)}")

#5) the greatest increase in profits (max) is using month-to-month profit change (Change) and then the average of those changes
    #find the mac increase value and find the min decrease
    IncreaseProfit = max(Change)
    DecreaseProfit = min(Change)
    #print(f"Increase: {Increase}")
    #print(f"Decrease: {Decrease}")

    #5.a) Relate the max/min to a month, add one to loop through
    IncreaseMonth = Change.index(max(Change))+1
    DecreaseMonth = Change.index(min(Change))+1
    #print outcome
    print(f"Greatest Increase in Profits : {TotalMonths[IncreaseMonth]} (${(int(IncreaseProfit))})")
    print(f"Greatest Decrease in Profits : {TotalMonths[DecreaseMonth]} (${(int(DecreaseProfit))})")

#6) export text file with the results

    file = open("output.txt" , "w") 

    file.write("Financial Analysis")
    file.write("/n")
    file.write("-----------------------------------------")
    file.write("/n")
    file.write(f"Total Months: {len(TotalMonths)}")
    file.write("/n")
    file.write(f"Total Profits: {sum(TotalProfit)}")
    file.write("/n")
    file.write(f"Average Sum: $ {round(sum(Change))/len(TotalMonths)}")
    file.write("/n")
    file.write(f"Greatest Increase in Profits : {TotalMonths[IncreaseMonth]} (${(int(IncreaseProfit))})")
    file.write("/n")
    file.write(f"Greatest Decrease in Profits : {TotalMonths[DecreaseMonth]} (${(int(DecreaseProfit))})")
