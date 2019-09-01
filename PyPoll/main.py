# Import os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes_count = 0
candidatelist = []
individual_candidate = []
candidate_vote_count = [0, 0, 0, 0]
candidate_vote_percent = [0, 0, 0, 0]
winning_candidate = []


# Open and read CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

# Total number of votes

    for row in csvreader:
        total_votes_count = total_votes_count + 1

        candidatelist.append(str(row[2]))
    for row[2] in candidatelist:
        if row[2] not in individual_candidate:
           individual_candidate.append(row[2])
        if row[2] == individual_candidate[0]:
           candidate_vote_count[0] += 1
        elif row[2] == individual_candidate[1]:
            candidate_vote_count[1] += 1
        elif row[2] == individual_candidate[2]:
            candidate_vote_count[2] += 1
        elif row[2] == individual_candidate[3]:
            candidate_vote_count[3] += 1

# Total percentage per individual candidate

    candidate_vote_percent[0] = round(100 * (candidate_vote_count[0] / total_votes_count), 4)
    candidate_vote_percent[1] = round(100 * (candidate_vote_count[1] / total_votes_count), 4)
    candidate_vote_percent[2] = round(100 * (candidate_vote_count[2] / total_votes_count), 4)
    candidate_vote_percent[3] = round(100 * (candidate_vote_count[3] / total_votes_count), 4)


# Choose winning candidate

if candidate_vote_count[0] == max(candidate_vote_count[0], candidate_vote_count[1], candidate_vote_count[2], candidate_vote_count[3]):
   winning_candidate = individual_candidate[0]

elif candidate_vote_count[1] == max(candidate_vote_count[0], candidate_vote_count[1], candidate_vote_count[2], candidate_vote_count[3]):
     winning_candidate = individual_candidate[1]

elif candidate_vote_count[2] == max(candidate_vote_count[0], candidate_vote_count[1], candidate_vote_count[2], candidate_vote_count[3]):
     winning_candidate = individual_candidate[2]

elif candidate_vote_count[3] == max(candidate_vote_count[0], candidate_vote_count[1], candidate_vote_count[2], candidate_vote_count[3]):
     winning_candidate = individual_candidate[3]




    
    

print("Election Results")
print("------------------------------") 
print("Total Votes: " + str(total_votes_count))
print("Election Results")
print(f"{individual_candidate[0]}: {candidate_vote_percent[0]}% ({candidate_vote_count[0]})")
print(f"{individual_candidate[1]}: {candidate_vote_percent[1]}% ({candidate_vote_count[1]})")
print(f"{individual_candidate[2]}: {candidate_vote_percent[2]}% ({candidate_vote_count[2]})")
print(f"{individual_candidate[3]}: {candidate_vote_percent[3]}% ({candidate_vote_count[3]})")
print("-----------------------------")
print(f"Winner: {winning_candidate}")

# Export text file

output_path = os.path.join("output", "Elections Results.txt")
with open(output_path, 'w', newline='') as text_file:

  print("Election Results", file=text_file)
  print("------------------------------", file=text_file) 
  print("Total Votes:  + {total_votes_count} ", file=text_file)
  print("Election Results")
  print(f"{individual_candidate[0]}: {candidate_vote_percent[0]}% ({candidate_vote_count[0]})", file=text_file)
  print(f"{individual_candidate[1]}: {candidate_vote_percent[1]}% ({candidate_vote_count[1]})", file=text_file)
  print(f"{individual_candidate[2]}: {candidate_vote_percent[2]}% ({candidate_vote_count[2]})",file=text_file)
  print(f"{individual_candidate[3]}: {candidate_vote_percent[3]}% ({candidate_vote_count[3]})", file=text_file)
  print("-----------------------------")
  print(f"Winner: {winning_candidate}", file=text_file)

csvfile.close()

    
    
