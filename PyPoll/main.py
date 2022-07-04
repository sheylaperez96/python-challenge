# Import modules for file pathing and csv files 
import os 
import csv

# Find the path to the election_data.csv file 
filePath = os.path.join("Resources", "election_data.csv")

# Read the csv file
with open(filePath,'r') as electionData:
    csvReader = csv.reader(electionData,delimiter=",")
    header = next(csvReader)

    # set initial variables/lists that will be manipulated in the loop
    voteCounter = 0 # initializing to 0
    candidates = [] # an empty list to add the names of the candidates 
    charlesVotes = 0 # store Charles' votes
    dianaVotes = 0 # store Diana's votes
    raymonVotes = 0 # store Raymon's votes

    # loop through the file
    for row in csvReader:
        
        # calculate the different variables
        voteCounter += 1 # add 1 to the voteCounter for each row
        # adding unique values to the candidate list
        if row[2] not in candidates: 
            candidates.append(row[2])
        if row[2] == candidates[0]:
            charlesVotes += 1 
        elif row[2] == candidates[1]:
            dianaVotes += 1
        else:
            raymonVotes += 1
        

# Generate the outputs
output = (
f"Election Results"
f"\n-------------------------"
f"\nTotal Votes: {voteCounter}"
f"\n-------------------------"
f"\n{candidates[0]}: {((charlesVotes/voteCounter)*100):.3f}% ({charlesVotes})" # % of votes won by Charles
f"\n{candidates[1]}: {((dianaVotes/voteCounter)*100):.3f}% ({dianaVotes})" # % of votes won by Diana
f"\n{candidates[2]}: {((raymonVotes/voteCounter)*100):.3f}% ({raymonVotes})" # % of votes won by Raymon
f"\n-------------------------"
f"\nWinner: {candidates[1]}" # Diana is the winner (she's at index 1 in the list)
f"\n-------------------------"
)

print(output)

# create the file path for the outputs of the analysis
outputFile = os.path.join("analysis", "election_analysis.csv")

# export the output to the text file
with open(outputFile, "w") as textFile:
    textFile.write(output)
