# Import modules for file pathing and csv files 
import os 
import csv

# Find the path to the election_data.csv file 
filePath = os.path.join("Resources", "election_data.csv")

# Read the csv file and set the header 
with open(filePath,'r') as electionData:
    csvReader = csv.reader(electionData,delimiter=",")
    header = next(csvReader)

    # set initial variables/lists/dictionaries that will be manipulated later on 
    voteCounter = 0 # initializing to 0
    candidates = [] # an empty list to add the names of the candidates 
    candidateVotes = {} # am epty dictionary that will hold each candidate and its corresponding votes
    winningCount = 0 # initialize the winning count to 0
    winningCandidate = "" # variable to hold the winning candidate 

    # loop through the file
    for row in csvReader:
        
        voteCounter += 1 # add 1 to the voteCounter for each row to get total number of votes 
        # check to see if the candidate is in the list of candidates
        if row[2] not in candidates: # if it isn't....
            candidates.append(row[2]) # add candidate name to candidate list
            candidateVotes[row[2]] = 1 # start the count at 1 for the votes of that candidate 
        else: # if it is...
            candidateVotes[row[2]] += 1 # add vote to the candidate's count

# empty variable for voting results
voterOutput = ""

# create a loop to get the vote count and the % of votes 
for candidate in candidateVotes:
    votes = candidateVotes.get(candidate)
    votePct = (int(votes)/int(voteCounter))*100
    voterOutput += f"{candidate}: {votePct:.3f}% ({votes})\n" # create a variable that will hold the output

    # update the winningCount number by comparing to number the votes
    if votes > winningCount:
        winningCount = votes
        # update the winning candidate 
        winningCandidate = candidate

# Generate the outputs
output = (
f"Election Results"
f"\n-------------------------"
f"\nTotal Votes: {voteCounter}"
f"\n-------------------------"
f"\n{voterOutput}"
f"-------------------------"
f"\n{winningCandidate}"
f"\n-------------------------"
)

print(output)

# create the file path for the outputs of the analysis
outputFile = os.path.join("analysis", "election_analysis.csv")

# export the output to the text file
with open(outputFile, "w") as textFile:
    textFile.write(output)
