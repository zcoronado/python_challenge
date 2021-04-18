# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
import os
import csv
import numpy as np 


# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
filepath = os.path.join("election_data.csv")
with open(filepath, 'r') as open_file: 
    csv_reader = csv.reader(open_file)

    next(csv_reader)

    voter_id = []
    voter_county = []
    voter_candidate = []
    unique_candidates = []
    
    cand_votes={}
    cand_opt=[]
    total_votes = 0 

    for row in csv_reader: 
        voter_id.append(row[0])
        voter_county.append(row[1])
        voter_candidate.append(row[2])
        total_votes = total_votes + 1 

        cand_name=row[2]
        if cand_name not in cand_opt: 
            cand_opt.append(cand_name)
            cand_votes[cand_name]= 0 
        
        cand_votes[cand_name] += 1 
   
print(cand_votes)

for cand in cand_votes:
    x = cand_votes.get(cand)
    per_x = float(x)/float(total_votes) *100
    print(per_x)

# The total number of votes cast

# A complete list of candidates who received votes



    # unique_candidates = np.unique(voter_candidate)
    # print(unique_candidates)

# The percentage of votes each candidate won 
    # for row in csv_reader: 
    #     total_votes += 1
        
    #     if voter_candidate in unique_candidates:
    #         candidate_index = unique_candidates.index(voter_candidate)
    #         candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
    #     else:
    #         #if candidate was not found in candidates_unique list then append to list and add 1 to vote count
    #         candidates_unique.append(voter_candidate)
    #         candidate_vote_count.append(1)


#     khan_votes = "Khan"
#     khan_total_votes = len("Khan")
#     khan_percent = khan_total_votes/(total_votes)
#     print(khan_percent)
    


# # The total number of votes each candidate won
#     count_dictionary = {}
#     for name in voter_candidate:
#         if name in count_dictionary:
#             count_dictionary[name] +=1 
#         else:
#             count_dictionary[name] = 1
#     print(count_dictionary)

    
        
# # The winner of the election based on popular vote.

# # As an example, your analysis should look similar to the one below:

# # Election Results
# # -------------------------
# # Total Votes: 3521001
# # -------------------------
# # Khan: 63.000% (2218231)
# # Correy: 20.000% (704200)
# # Li: 14.000% (492940)
# # O'Tooley: 3.000% (105630)
# # -------------------------
# # Winner: Khan
# # -------------------------
# # In addition, your final script should both print the analysis to the terminal and export a text file with the results.