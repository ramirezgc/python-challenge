import os
import csv

filename = "election_data.csv"
path ="Resources"

file = os.path.join(path,filename)

Total_Votes = 0
Khan_Votes = 0
Khan_Percent = 0
Correy_Votes = 0
Correy_Percent = 0
Li_Votes = 0
Li_Percent = 0
OTooley_Votes = 0
OTooley_Percent = 0



with open(file) as csvFile:
    csvFile.readline()
    reader = csv.reader(csvFile)

    for row in reader:
        Total_Votes += 1

        if row[2] == "Khan":
            Khan_Votes += 1
        elif row[2] == "Correy":
            Correy_Votes += 1
        elif row[2] == "Li":
            Li_Votes +=1
        elif row[2] == "O'Tooley":
            OTooley_Votes +=1

Khan_Percent = (Khan_Votes / Total_Votes)*100
Correy_Percent =  (Correy_Votes / Total_Votes)*100
Li_Percent = (Li_Votes / Total_Votes)*100
OTooley_Percent = (OTooley_Votes / Total_Votes)*100

Dictionary_of_candidates = {
    Khan_Votes: "Khan",
    Correy_Votes: "Correy",
    Li_Votes: "Li",
    OTooley_Votes: "O'Tooley"
}

Winner = max(Khan_Votes, Correy_Votes, Li_Votes,OTooley_Votes)

Output = f"""
Election Results
----------------------------
Total Votes: {Total_Votes}
____________________________
Khan: {Khan_Percent:.3f}% ({Khan_Votes})
Correy: {Correy_Percent:.3f}% ({Correy_Votes})
Li: {Li_Percent:.3f}% ({Li_Votes})
O'Tooley: {OTooley_Percent:.3f}% ({OTooley_Votes})
____________________________

Winner: {Dictionary_of_candidates [Winner]}

"""

print(Output)

with open('analysis.txt', 'w') as Output_File:
    Output_File.write(Output)