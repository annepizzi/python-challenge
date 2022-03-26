#1) The total number of votes cast
#2) A complete list of candidates who received votes
#3) The percentage of votes each candidate won and the total number of votes each candidate won
#4) The winner of the election based on popular vote.

import os
import csv

#define the path and open document from computer.
election_data = os.path.join("/Users/annepizzini/Desktop/python-challenge/PyPoll/Resources","election_data.csv")

#variables
TotalVotes = []
Candidates = {}
Votes = []
Winner = 0

# Open and read csv
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
#(checked and working) Print statment for starting analysis including "Election Results" and "--------------"
    print("Election Results")
    print("-----------------------------------------")
    for row in csv_reader:
#1) create a list of all grab all the TotalVotes and create a list
        TotalVotes.append(int(row[0]))
        Votes.append(row[2])
    #print total votes
    print(f"Total Votes: {len(TotalVotes)}")
#2)Create a dictionary of Candidates
    for Vote in Votes:
        if Vote in Candidates.keys():
            Candidates[Vote] += 1
        else:
            Candidates[Vote] = 1

#3) The percentage of votes each candidate won and the total number of votes each candidate won

    for key, VoteValue in Candidates.items():
        #do a check with a variable called winner, Winner = 0, the code only works if the if statement is true
        if VoteValue > Winner:
            Winner = VoteValue
            WinnerName = key
        print(f'{key} : {round(VoteValue/len(TotalVotes)*100, 2)} % ({VoteValue})')
    print("-----------------------------------------")
#4) The winner of the election based on popular vote.
    print(WinnerName)

    file = open("output.txt" , "w")

    file.write("Election Results")
    file.write("\n")
    file.write("-----------------------------------------")
    file.write("\n")
    file.write(f'{key} : {round(VoteValue/len(TotalVotes)*100, 2)} % ({VoteValue})')
    file.write("\n")
    file.write("-----------------------------------------")
    file.write("\n")
    file.write(f'{key} : {round(VoteValue/len(TotalVotes)*100, 2)} % ({VoteValue})')
    file.write("\n")
    file.write("-----------------------------------------")
    file.write("\n")
    file.write(WinnerName)
